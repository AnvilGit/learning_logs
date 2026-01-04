# Learning Log

Learning Log is a Django-based web application that allows users to record topics they’re learning about and make journal-style entries under each topic.
Each user has private topics, entries, and full CRUD functionality.

---

## 🚀 Features

### 🔐 User Accounts

* Register, log in, log out
* Each user can only access their own topics and entries
* Login required for all CRUD operations

### 🗂 Topics

* View all topics belonging to the logged-in user
* Add a new topic
* Edit or delete existing topics
* Topic ownership enforced for security

### ✍️ Entries

* Add new entries under a topic
* Edit or delete entries
* Entries displayed from newest → oldest
* Access restricted to the topic owner

---

## 📁 Project Structure

```
learning_log/
│
├── learning_logs/        # Main app: topics, entries, views, forms, templates
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── templates/
│
├── users/                # User registration, login system
│
├── learning_log/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3            # SQLite database on Development, PostgreSQL on production 
└── manage.py
```

---

## ⚙️ Requirements

* Python 3.x
* Django 5.x (project built on Django 5.1.4)
* django-bootstrap3 (for UI styling)

Install packages:

```
pip install -r requirements.txt
```

---

## 🛠 Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/learning-log.git
cd learning-log
```

### 2. Create a Virtual Environment

```
python -m venv myenv
source venv/bin/activate        # macOS/Linux
myenv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 6. Start Development Server

```
python manage.py runserver
```

Live Application URL:

The Application is deployed in https://learning-logs-sopi.onrender.com/
 

---

## 🔑 URL Overview

| URL                         | Description            |
| --------------------------- | ---------------------- |
| `/`                         | Home page              |
| `/topics/`                  | List of user topics    |
| `/topics/<id>/`             | Single topic + entries |
| `/new_topic/`               | Add new topic          |
| `/new_entry/<topic_id>/`    | Add new entry          |
| `/edit_entry/<entry_id>/`   | Edit entry             |
| `/delete_entry/<entry_id>/` | Delete entry           |
| `/delete_topic/<topic_id>/` | Delete topic           |
| `/users/login/`             | Login                  |
| `/users/logout/`            | Logout                 |
| `/users/register/`          | Register               |

---

## 🧩 Key Code Highlights

### Topic model

```python
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
```

### Entry model

```python
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(default='Pls enter data')
    date_added = models.DateTimeField(auto_now_add=True)
```

### Topic protection in views

```python
if topic.owner != request.user:
    raise Http404
```

---

## 🧪 Running Tests (optional)

If you add tests:

```
python manage.py test
```

---

## 📜 License

MIT License (or whichever you prefer).

---

## 🙌 Credits

Based on the "Learning Log" project from the book **Python Crash Course**
with additional CRUD enhancements (topic/entry deletion, validation, templates, navigation, etc.).

---
