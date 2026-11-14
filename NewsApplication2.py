
# We will learn 3 things here
# 1. How to fetch data by API
# 2. OOP
# 3. GUI

import requests
from tkinter import *
from PIL import ImageTk, Image
import io
import webbrowser
import threading
from pathlib import Path


class NewsApp:

    def __init__(self):
        # Fetch data using API
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=us&apiKey=67940d52be9e4d0880f051b3cae803b6',
            timeout=15
        ).json()

        # Store articles
        self.articles = self.data['articles']

        # Image cache
        self.image_cache = {}

        # Track current news index
        self.current_index = 0

        # Initial GUI Load
        self.load_gui()

        # Load the first news item
        self.load_news_item(0)

        # Run GUI event loop only once
        self.root.mainloop()


    def load_gui(self):

        self.root = Tk()
        self.root.geometry('350x600')
        self.root.title('Newsify')
        self.root.resizable(0, 0)
        self.root.configure(background='black')


    def clear(self):

        for i in self.root.pack_slaves():
            i.destroy()


    def load_news_item(self, index):

        # Clear the screen
        self.clear()

        # Update current index
        self.current_index = index

        # Get current article
        article = self.articles[index]

        # Get image URL
        img_url = article.get('urlToImage')

        # Create image label
        label = Label(self.root, bg='black')
        label.pack()

        # Display downloaded image or fallback image
        def show_image(raw_data):

            # Avoid displaying an old article's image
            if self.current_index != index:
                return

            try:

                im = Image.open(
                    io.BytesIO(raw_data)
                ).resize((350, 250))

                photo = ImageTk.PhotoImage(im)

                label.config(image=photo)
                label.image = photo

            except Exception as e:

                print("Image display error:", e)

        # Background image downloading
        def download_image():

            try:

                # Check whether image URL exists
                if not img_url:
                    raise ValueError("Image URL is missing")

                # Check cache first
                if img_url in self.image_cache:

                    raw_data = self.image_cache[img_url]

                else:

                    response = requests.get(
                        img_url,
                        headers={'User-Agent': 'Mozilla/5.0'},
                        timeout=10
                    )

                    response.raise_for_status()

                    raw_data = response.content

                    # Save image in cache
                    self.image_cache[img_url] = raw_data

                # Update GUI through main thread
                self.root.after(
                    0,
                    lambda: show_image(raw_data)
                )

            except Exception as e:

                print("Image loading error:", e)

                # Load default image
                try:

                    fallback_path = Path(__file__).with_name('no_image.png')
                    fallback_data = fallback_path.read_bytes()

                    self.root.after(
                        0,
                        lambda: show_image(fallback_data)
                    )

                except Exception as fallback_error:

                    print("Fallback image error:", fallback_error)

        # Start background thread
        threading.Thread(
            target=download_image,
            daemon=True
        ).start()


        # Display title
        heading = Label(
            self.root,
            text=article['title'],
            bg='black',
            fg='white',
            wraplength=350,
            justify='center'
        )

        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))


        # Display description
        details = Label(
            self.root,
            text=article['description'],
            bg='black',
            fg='white',
            wraplength=350,
            justify='center'
        )

        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))


        # Create buttons frame
        frame = Frame(self.root, bg='black')
        frame.pack(side=BOTTOM, fill=X)


        # Previous button
        # Hide Prev on the first news item
        if index > 0:

            prev = Button(
                frame,
                text='Prev',
                width=16,
                height=3,
                command=lambda: self.load_news_item(index - 1)
            )

            prev.pack(side=LEFT)


        # Read More button
        # Always visible
        read = Button(
            frame,
            text='Read More',
            width=16,
            height=3,
            command=lambda: self.open_link(article['url'])
        )

        read.pack(side=LEFT)


        # Next button
        # Hide Next on the last news item
        if index < len(self.articles) - 1:

            next = Button(
                frame,
                text='Next',
                width=16,
                height=3,
                command=lambda: self.load_news_item(index + 1)
            )

            next.pack(side=LEFT)


    def open_link(self, url):

        webbrowser.open(url)


# Create object
obj = NewsApp()
