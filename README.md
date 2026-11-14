
# 📰 Newsify – Python News Application

Newsify is a desktop-based news application developed using Python. It fetches the latest news headlines through the NewsAPI and displays them in an interactive graphical user interface built with Tkinter.

The project demonstrates practical implementation of API integration, Object-Oriented Programming (OOP), GUI development, multithreading, and image caching.

## ✨ Features

- **Live News Fetching:** Retrieves top headlines using NewsAPI.
- **Interactive GUI:** Displays news in a simple and user-friendly Tkinter interface.
- **News Details:** Shows article titles and descriptions.
- **Image Loading:** Fetches and displays images associated with news articles.
- **Fallback Image:** Displays a default image when an article image cannot be loaded.
- **Image Caching:** Stores downloaded images to avoid unnecessary repeated downloads.
- **Multithreading:** Downloads images in a background thread to keep the GUI responsive.
- **News Navigation:** Navigate between articles using Previous and Next buttons.
- **Read More:** Opens the complete news article in the default web browser.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| NewsAPI | Fetching news headlines |
| Requests | Making HTTP API requests |
| Pillow (PIL) | Image processing and display |
| Threading | Background image downloading |
| Webbrowser | Opening complete news articles |

## 📂 Project Structure

```text
Newsify/
│
├── main.py
├── no_image.png
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Newsify.git
```

### 2. Navigate to the project directory

```bash
cd Newsify
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure NewsAPI

- Get an API key from [NewsAPI](https://newsapi.org/).
- Create a `.env` file in the project directory.
- Add your API key:

```env
NEWS_API_KEY=YOUR_API_KEY
```

### 5. Run the application

```bash
python main.py
```

## 📸 Application Preview

Add screenshots of your application here after uploading them to your GitHub repository.

Example:

```markdown
![Newsify Application](C:\Users\HP\OneDrive\Documents\Desktop\Python\NewsApplicationNew\Newsify.png)
```

## 🎯 Learning Objectives

This project was developed to gain practical experience with:

- Consuming RESTful APIs.
- Understanding Object-Oriented Programming concepts.
- Building desktop applications using Tkinter.
- Handling HTTP requests and JSON responses.
- Working with images using Pillow.
- Implementing multithreading in Python.
- Improving application performance using caching.
- Handling exceptions and network failures.

## 🚀 Future Improvements

- Add category-based news filtering.
- Implement a search functionality.
- Add a refresh news option.
- Improve the user interface.
- Add support for multiple countries.
- Add a loading indicator while fetching news.

## 👨‍💻 Author

**Himanshu Kumar Gupta**

- GitHub: [Himanshu_Gupta21](https://github.com/Himanshu_Gupta21)
- LinkedIn: [Himanshu Gupta](https://www.linkedin.com/in/himanshu-gupta-69234126b/)

---

⭐ If you find this project interesting, feel free to explore the repository!
