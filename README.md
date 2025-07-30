# Django Signals & Python Custom Class – Assignment Submission


## Project Overview

This project demonstrates key concepts in **Django Signals** and **Python Custom Classes**

## 🛠️ Installation & Setup Guide

### 1. Clone the Repository

```bash
git clone [https://github.com/<your-username>/django-signals-assignment.git](https://github.com/sriramkrish68/Django_signals)
cd Django_signals
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
I’ve created a Django project named signals_demo and an app called core. I added 'core' to the INSTALLED_APPS in settings.
In the core app, I defined a basic model called BlogPost with a title and content field.

### 3. Install Django

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run shell to test the behaviors

```bash
python manage.py shell
```


---

## 📘 Models Created

| Model      | Fields             | Used For                               |
| ---------- | ------------------ | -------------------------------------- |
| `BlogPost` | `title`, `content` | Used in Signal questions               |

---

## ❓ Django Signals :

---

### ✅ Q1: Are Django signals synchronous?

> **Yes**, Django signals are synchronous by default.
> We demonstrate this using a `time.sleep()` in the signal, which delays the main thread during `Book.objects.create()`.

---

### ✅ Q2: Do Django signals run in the same thread as the caller?

> **Yes**, the signal executes in the **same thread** as the one that triggers it.
> We compare thread IDs before and inside the `post_save` signal.

---

### ✅ Q3: Do Django signals run in the same database transaction as the caller?

> **No**, not by default.
> Django runs in **autocommit mode**, so signals run **outside** transactions unless you explicitly use `transaction.atomic()`.

---

