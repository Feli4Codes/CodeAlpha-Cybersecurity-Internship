# Secure Code Review Report

## Application

Python Login System

---

## Tool Used

Bandit Static Analyzer

---

## Findings

### High Severity

Use of MD5 hashing

Recommendation:

Replace MD5 with bcrypt.

---

### Medium Severity

Hardcoded user credentials.

Recommendation:

Store credentials securely in a database or secret manager.

---

### Medium Severity

Weak passwords.

Recommendation:

Enforce password complexity.

---

### Low Severity

Password visible during input.

Recommendation:

Use getpass.

---

### Medium Severity

Unlimited login attempts.

Recommendation:

Implement rate limiting and account lockout.

---

## Overall Risk

Medium

---

## Conclusion

The application functions correctly but contains several security weaknesses. Replacing insecure hashing, avoiding hardcoded credentials, enforcing strong password policies, hiding password input, and adding protections against brute-force attacks significantly improve its security.