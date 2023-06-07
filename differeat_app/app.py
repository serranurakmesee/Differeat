from flask import Flask, render_template, request, redirect

from components.user_management import UserManagement

app = Flask(__name__)
user_management = UserManagement(db_file="users.db")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new user account
        user_management.create_account(name, email, password)
        return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Attempt to login
        user = user_management.login(email, password)
        if user:
            return redirect('/dashboard')
        else:
            return render_template('login.html', message='Invalid email or password.')
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Get all users from the user database
    users = user_management.get_all_users()
    return render_template('dashboard.html', users=users)

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Update the user account
        user_management.update_account(user_id, name, email, password)
        return redirect('/dashboard')
    else:
        user = user_management.get_user_by_id(user_id)
        if user:
            return render_template('update.html', user=user)
        else:
            return redirect('/dashboard')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # Delete the user account
    user_management.delete_account(user_id)
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
