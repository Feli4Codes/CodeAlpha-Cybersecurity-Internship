"""
Secure Login System with SQLite Database

This application demonstrates secure coding practices by:
- Using bcrypt to hash passwords
- Validating password strength
- Hiding password input
- Limiting login attempts
- Persisting data in SQLite
 Creates SQLite database and users table if they don't exist.
    """
import sqlite3
from getpass import getpass
from datetime import datetime


# ==========================================
# DATABASE INITIALIZATION
# ==========================================

def initialize_database():
    connection = sqlite3.connect("secure_users.db")
    cursor = connection.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash BLOB NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP,
        login_attempts INTEGER DEFAULT 0
    )
    """)
    
    connection.commit()
    connection.close()
    print("[DATABASE] Initialized secure_users.db\n")


def get_db_connection():
    """
    Returns a database connection.
    """
    return sqlite3.connect("secure_users.db")


def hash_password(password):
    """
    Hashes the password using bcrypt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def check_password_strength(password):
    """
    Checks whether the password meets basic security requirements.
    """

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."

    if not any(not char.isalnum() for char in password):
        return False, "Password must contain at least one special character."

    return True, "Password is strong."


# ==========================================
# DATABASE OPERATIONS
# ==========================================

def user_exists(username):
    """
    Checks if username already exists in database.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    connection.close()
    return result is not None


def create_user_in_db(username, password_hash):
    """
    Inserts new user into database with hashed password.
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        connection.commit()
        connection.close()
        return True, "Account created successfully!"
    except sqlite3.IntegrityError:
        return False, "Username already exists!"


def get_user_by_username(username):
    """
    Retrieves user data from database by username.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, username, password_hash, login_attempts FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    connection.close()
    return result


def update_login_attempts(username, attempts):
    """
    Updates login attempts counter in database.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET login_attempts = ? WHERE username = ?",
        (attempts, username)
    )
    connection.commit()
    connection.close()


def update_last_login(username):
    """
    Updates last login timestamp in database.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET last_login = ? WHERE username = ?",
        (datetime.now(), username)
    )
    connection.commit()
    connection.close()


# ==========================================
# MAIN PROGRAM
# ==========================================

# Initialize database
initialize_database()

# Main menu
while True:
    print("=" * 40)
    print("    SECURE LOGIN SYSTEM")
    print("=" * 40)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        # ==========================================
        # USER REGISTRATION
        # ==========================================
        print("\n" + "=" * 40)
        print("        USER REGISTRATION")
        print("=" * 40)
        
        username = input("Create a username: ").strip()
        
        # Check if username already exists
        if user_exists(username):
            print("✗ Username already exists! Try a different one.\n")
            continue
        
        while True:
            password = getpass("Create a password: ")
            
            valid, message = check_password_strength(password)
            
            if valid:
                break
            
            print(f"\n✗ {message}")
            print("Please try again.\n")
        
        # Hash the password
        password_hash = hash_password(password)
        
        # Store in database
        success, msg = create_user_in_db(username, password_hash)
        print(f"✓ {msg}\n")
    
    elif choice == "2":
        # ==========================================
        # USER LOGIN
        # ==========================================
        print("\n" + "=" * 40)
        print("           USER LOGIN")
        print("=" * 40)
        
        login_username = input("Username: ").strip()
        
        # Get user from database
        user_data = get_user_by_username(login_username)
        
        if user_data is None:
            print("✗ User not found!\n")
            continue
        
        user_id, db_username, stored_hash, current_attempts = user_data
        
        MAX_ATTEMPTS = 3
        
        if current_attempts >= MAX_ATTEMPTS:
            print(f"✗ Account locked! Maximum login attempts exceeded.\n")
            continue
        
        # Login attempts loop
        while current_attempts < MAX_ATTEMPTS:
            login_password = getpass("Password: ")
            
            # Verify password
            if bcrypt.checkpw(login_password.encode(), stored_hash):
                print("\n✓ Login Successful!")
                print(f"Welcome back, {login_username}!")
                
                # Update database
                update_login_attempts(login_username, 0)
                update_last_login(login_username)
                print()
                break
            
            current_attempts += 1
            update_login_attempts(login_username, current_attempts)
            
            remaining = MAX_ATTEMPTS - current_attempts
            if remaining > 0:
                print(f"\n✗ Invalid password.")
                print(f"Attempts remaining: {remaining}\n")
            else:
                print(f"\n✗ Account locked! Maximum login attempts exceeded.\n")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("✗ Invalid choice. Please try again.\n")

else:
    print("\n Too many failed login attempts.")
    print("Access temporarily blocked.")