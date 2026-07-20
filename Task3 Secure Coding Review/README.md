# Secure Authentication System using Python, SQLite and bcrypt

##  Project Overview

This project was developed as part of the **CodeAlpha Cyber Security Internship**.

The application demonstrates secure coding practices by implementing a secure user authentication system. It improves upon a vulnerable login application by using modern security techniques such as password hashing, secure password input, password strength validation, and protection against brute-force attacks.

---

## Objectives

- Demonstrate secure password storage
- Prevent plain-text password storage
- Implement password strength validation
- Protect user credentials using bcrypt
- Limit login attempts
- Store user information securely using SQLite

---

## Technologies Used

- Python 3
- SQLite3
- bcrypt
- getpass
- bandit


---

## Security Features

 Password hashing using bcrypt

  Password masking using getpass

  Password strength validation

  SQLite database for secure storage

  Login attempt limitation

  Prevention of duplicate usernames

---

##  Installation

Clone the repository

bash
git clone <repository-url>


Install the required package

bash
pip install -r requirements.txt


Run the application

bash
python secure_app.py


---

## How It Works

### Registration

- User creates a username
- User creates a strong password
- Password is hashed using bcrypt
- Username and password hash are stored in SQLite

### Login

- User enters credentials
- Password is verified using bcrypt
- User is granted or denied access

---

## Skills Demonstrated

- Secure Coding
- Authentication
- Password Hashing
- SQLite Database Management
- Cybersecurity Best Practices
- Python Programming

---

##  Author

**Felicity Avor**

CodeAlpha Cyber Security Internship