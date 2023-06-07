import sqlite3

class UserDatabase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        # Create the users table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                password TEXT
            )
        """)
        self.connection.commit()

    def generate_user_id(self):
        # Generate a new unique user ID
        self.cursor.execute("SELECT MAX(id) FROM users")
        result = self.cursor.fetchone()
        if result[0] is not None:
            return result[0] + 1
        return 1

    def save_user(self, user):
        # Save the user to the database
        self.cursor.execute("""
            INSERT INTO users (id, name, email, password) VALUES (?, ?, ?, ?)
        """, (user["id"], user["name"], user["email"], user["password"]))
        self.connection.commit()

    def get_user_by_id(self, user_id):
        # Retrieve the user with the given ID from the database
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result is not None:
            user = {
                "id": result[0],
                "name": result[1],
                "email": result[2],
                "password": result[3]
            }
            return user
        return None

    def get_user_by_email(self, email):
        # Retrieve the user with the given email from the database
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = self.cursor.fetchone()
        if result is not None:
            user = {
                "id": result[0],
                "name": result[1],
                "email": result[2],
                "password": result[3]
            }
            return user
        return None

    def update_user(self, user):
        # Update the user in the database
        self.cursor.execute("""
            UPDATE users SET name = ?, email = ?, password = ? WHERE id = ?
        """, (user["name"], user["email"], user["password"], user["id"]))
        self.connection.commit()

        if self.cursor.rowcount > 0:
            return True
        return False

    def delete_user(self, user_id):
        # Delete the user from the database
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()

        if self.cursor.rowcount > 0:
            return True
        return False

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            user = {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "password": row[3]
            }
            users.append(user)
        return users
