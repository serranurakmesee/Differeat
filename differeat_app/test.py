from components.user_management import UserManagement

# Create an instance of UserManagement
user_management = UserManagement(db_file="database/users.db")

# Test account creation
user_management.create_account("John Doe", "john@example.com", "password123")

# Test login
user = user_management.login("john@example.com", "password123")
if user:
    print(f"Logged in as {user['name']} ({user['email']})")

# Test account update
user_management.update_account(user['id'], "John Smith", "john.smith@example.com", "newpassword456")

# Test login after account update
user = user_management.login("john.smith@example.com", "newpassword456")
if user:
    print(f"Logged in as {user['name']} ({user['email']})")

# Test account deletion
user_management.delete_account(user['id'])

# Test login after account deletion
user = user_management.login("john.smith@example.com", "newpassword456")
if not user:
    print("Login unsuccessful. User account has been deleted.")
