# Secure Coding Review Report

## Reviewer

Felicity Avor

## Project

Secure Authentication System

## Programming Language

Python

---

# Objective

The objective of this review was to analyze a Python login application, identify security vulnerabilities, evaluate their risks, and recommend secure coding improvements.

---

# Scope

The review covered:

- User Registration
- User Login
- Password Storage
- Authentication
- Input Validation

---

# Methodology

A manual secure code review was performed by inspecting the application's source code and identifying security weaknesses based on secure coding best practices.

---

# Vulnerabilities Identified

## 1. Hardcoded Credentials

**Severity:** High

### Description

The original application stored administrator credentials directly in the source code.

### Risk

Anyone with access to the source code could view the credentials.

### Recommendation

Store passwords securely using bcrypt and remove hardcoded credentials.

---

## 2. Plain-Text Password Storage

**Severity:** High

### Description

Passwords were stored in plain text.

### Risk

Compromised passwords could immediately be used by attackers.

### Recommendation

Hash passwords using bcrypt before storage.

---

## 3. Weak Password Policy

**Severity:** Medium

### Description

Users could create weak passwords.

### Risk

Weak passwords increase the likelihood of successful brute-force attacks.

### Recommendation

Require passwords to meet minimum strength requirements.

---

## 4. Unlimited Login Attempts

**Severity:** Medium

### Description

The application allowed unlimited login attempts.

### Risk

Attackers could perform brute-force attacks.

### Recommendation

Limit login attempts and temporarily block access after repeated failures.

---

## 5. Password Visibility

**Severity:** Low

### Description

Passwords were visible during input.

### Risk

Attackers nearby could observe passwords.

### Recommendation

Use the getpass module to hide password input.

---

# Security Improvements Implemented

- bcrypt password hashing
- SQLite database storage
- Password strength validation
- Hidden password input
- Login attempt limitation
- Duplicate username prevention

---

# Conclusion

The vulnerable login application contained multiple security weaknesses that could expose user credentials and increase the risk of unauthorized access.

The secure version successfully mitigated these vulnerabilities by implementing secure authentication practices, password hashing using bcrypt, password strength validation, secure password input, and SQLite database storage.