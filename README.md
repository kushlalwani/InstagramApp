# 📸 InstaApp – Instagram Follower Tracker

InstaApp is a web-based tool to track your Instagram followers and following using Selenium for scraping, SQLAlchemy for data storage, and Flask for visualization.

---

## 🚀 Features

- 🔐 Secure login via headless Selenium browser  
- 👥 Scrapes all followers and followings  
- 🔄 Identifies:
  - People who don’t follow you back
  - People you don’t follow back  
- 📊 View all data in a simple Flask web app  
- 🧠 Stores everything in an SQLite database  

---

## 🧱 Project Structure

```
InstaApp/
├── backend/
│   ├── app.py             # Flask app and routes
│   ├── models.py          # SQLAlchemy models
│   ├── scraper.py         # Data scraping logic
│   ├── script.py          # Selenium scraping utilities
├── templates/             # HTML templates for Flask
│   ├── index.html
│   ├── followers.html
│   ├── following.html
├── instagram.db           # SQLite database (created after running)
├── .env                   # IG credentials (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/InstaApp.git
cd InstaApp
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root

```
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
```

---

## ▶️ Run the App

First, run the scraper:

```bash
python backend/scraper.py
```

Then, start the Flask web app:

```bash
flask --app backend.app --debug run
```

Visit [http://localhost:5000](http://localhost:5000) to explore your follower data.

---

## ✅ To-Do

- [ ] Add daily snapshot tracking
- [ ] Schedule scraping (e.g., APScheduler or cron)
- [ ] Add user authentication
- [ ] Deploy online with Render or Fly.io

---

## 💡 Tech Stack

- Python 3
- Flask
- SQLAlchemy
- Selenium
- WebDriver Manager
- SQLite
- Dotenv