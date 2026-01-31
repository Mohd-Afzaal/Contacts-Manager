# Contacts Manager (Flask CRUD App)

A simple **Contacts Manager** web application built using **Flask**, **SQLAlchemy**, and **SCSS**.  
This project helped me practice full **CRUD operations**, basic **search functionality**, session-based user separation, and frontend styling with SCSS.

---

## Features

- Create, view, update, and delete contacts
- Search contacts by **name, email, or phone number**
- Session-based contact isolation (each user sees only their own contacts)
- Styled UI using **SCSS**
- Flash messages for validation and errors
- Responsive, card-based contact layout

---

## Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, Jinja2, SCSS
- **Database:** SQLite
- **Styling:** SCSS (compiled to CSS)
- **Sessions:** Flask session with UUID-based user IDs

---

## Project Structure
```
contacts-manager/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files (venv, db, compiled CSS)
│
├── templates/             # Jinja2 HTML templates
│   ├── index.html         # Contact list + search
│   ├── add.html           # Add new contact form
│   └── update.html        # Update contact form
│
├── static/                # Static assets
│   └── styles.scss        # SCSS source file (compiled locally)
│
└── venv/                  # Virtual environment (ignored)

```
---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/contacts-manager.git
cd contacts-manager
2. Create and activate virtual environment
python -m venv venv
Windows

venv\Scripts\activate
Linux / macOS

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt

SCSS Compilation
This project uses SCSS for styling.

Run this in a separate terminal while developing:

sass --watch static:static
Compiled CSS files are intentionally ignored in Git.

Run the App
python app.py
Then open your browser at:

http://127.0.0.1:5000
Search Functionality
Search works across name, email, and phone

Handles empty results gracefully

Clear search option included

Learning Outcomes
Understanding Flask routing and request handling

Working with SQLAlchemy ORM

Handling form validation and errors

Using sessions for user-specific data

Writing cleaner SCSS and structured UI components

Proper Git hygiene (.gitignore, no venv uploads)

Future Improvements
User authentication (login / register)

Pagination for large contact lists

Contact categories or tags

Export contacts to CSV

Switch to PostgreSQL for production

📄 License
This project is licensed under the MIT License.

✨ Author
Aish
Learning Flask by building real projects instead of tutorials.

