import hashlib

users = {
    "admin": hashlib.md5("admin123".encode()).hexdigest(),
    "felicity": hashlib.md5("password".encode()).hexdigest()
}

username = input("Username: ")
password = input("Password: ")

hashed = hashlib.md5(password.encode()).hexdigest()

if username in users:
    if users[username] == hashed:
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("User not found")