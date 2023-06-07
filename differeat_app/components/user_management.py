from database.user_database import UserDatabase

class UserManagement:
    def __init__(self, db_file):
        self.user_db = UserDatabase(db_file)

    def create_account(self, name, email, password):
        # Check if the email is already registered
        if self.user_db.get_user_by_email(email):
            print("An account with this email already exists.")
            return

        # Create a new user account
        user_id = self.user_db.generate_user_id()
        user = {
            "id": user_id,
            "name": name,
            "email": email,
            "password": password
        }
        self.user_db.save_user(user)
        print("Account created successfully.")

    def login(self, email, password):
        # Retrieve the user with the given email from the database
        user = self.user_db.get_user_by_email(email)

        # Check if the user exists and the password matches
        if user and user["password"] == password:
            print("Login successful.")
            return user

        print("Invalid email or password.")
        return None

    def update_account(self, user_id, name, email, password):
        # Retrieve the user from the database
        user = self.user_db.get_user_by_id(user_id)

        # Check if the user exists
        if user:
            # Update the user's information
            user["name"] = name
            user["email"] = email
            user["password"] = password
            self.user_db.update_user(user)
            print("Account updated successfully.")
        else:
            print("User not found.")

    def delete_account(self, user_id):
        # Delete the user from the database
        if self.user_db.delete_user(user_id):
            print("Account deleted successfully.")
        else:
            print("User not found.")
