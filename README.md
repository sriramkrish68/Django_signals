# Django Signals & Python Custom Class – Assignment Submission


## Project Overview

This project demonstrates key concepts in **Django Signals** and **Python Custom Classes**

## Installation & Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/sriramkrish68/Django_signals.git
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

## Models Created

| Model      | Fields             | Used For                               |
| ---------- | ------------------ | -------------------------------------- |
| `BlogPost` | `title`, `content` | Used in Signal questions               |

---

## Django Signals :

---

### Q1: Are Django signals synchronous?

**Yes**, Django signals are synchronous by default.
We demonstrate this using a `time.sleep()` in the signal, which delays the main thread during `User.objects.create_user()`.
I have created a new user. The post_save signal was triggered immediately, and it had a 3-second delay inside it.
The total time taken shows around 3 seconds, proving that the main thread waited for the signal to finish.
So yes, Django signals are synchronous by default.
---

### Q2: Do Django signals run in the same thread as the caller?

**Yes**, the signal executes in the **same thread** as the one that triggers it.
We compare thread IDs before and inside the `post_save` signal.

---

### Q3: Do Django signals run in the same database transaction as the caller?

**No**, not by default.
By default Django signals do not run in the same database transaction as the caller.
This is because Django runs in autocommit mode. That means each .save() or .create() is immediately committed, and signals like post_save are triggered after the save operation, outside any explicit transaction context unless wrapped in transaction.atomic().

---

