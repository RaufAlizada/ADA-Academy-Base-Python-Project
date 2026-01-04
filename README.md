# RUMECOS University Cabinet (Tkinter)

A desktop GUI application built with **Python and Tkinter** that simulates a simple university management system. The project includes authentication and role-based access with separate panels for **teachers** and **students**. User data is stored locally using JSON files.

---

## ✨ Features

### Authentication

* Register as **teacher** or **student**
* Login using username and password
* Basic input validation:

  * Age must be numeric and **18+**
  * Username length ≥ 4 characters
  * Password length ≥ 6 characters

### Teacher Cabinet

* Add students (name, surname, group)
* Manage student status:

  * Passed students
  * Failed students
* Delete students from lists
* Logout and exit controls

### Student Cabinet

* Access external resources:

  * Python quizzes (W3Schools)
  * Send email to manager
  * ADA University social media links
* Image-based UI elements
* Logout and exit controls

---

## 🛠 Technologies Used

* **Python 3**
* **Tkinter** – GUI framework
* **JSON** – Local data storage

---

## 📦 Requirements

Make sure Python 3 is installed on your system.

Install required libraries:

```bash
pip install pillow
```

---

## 🚀 Installation & Run

Clone the repository:

```bash
git clone https://github.com/RaufAlizada/ADA-Academy-Base-Python-Project.git
```

Navigate into the project directory:

```bash
cd ADA-Academy-Base-Python-Project/UNIVERSITY STUDENT SYSTEM
```

Run the application:

```bash
python "ADA University.py"
```

---

## 📁 Project Files

The following files must remain in the same directory:

* `ADA University.py` – Main application
* `teachers.json` – Stores teacher accounts (auto-created)
* `students.json` – Stores student accounts (auto-created)

---

## ⚙️ How It Works (Overview)

* On startup, the application loads existing users from JSON files
* Registration saves new users into the corresponding JSON file
* Login checks credentials and opens the correct panel based on role
* Teacher panel manages student lists during runtime

---

## 📌 Notes

* Data is stored locally (no database or backend server)
* JSON files are created automatically after first registration
* Designed as an educational Tkinter project

---

👨‍💻 *Developed as a Python GUI learning project*
