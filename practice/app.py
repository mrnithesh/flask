from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'secretkey'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<name>')
def greet(name):
    return render_template('greet_user.html', username=name)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['username']
        return redirect(url_for('greet', name=name))
    return render_template('form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username =="admin" and password == "pass":
            session["user"] = username
            flash("user logged in sucessfully!","success")
            return redirect(url_for('admin'))
        else:
            flash("Invalid credentials!", "error")
            return redirect(url_for("login"))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user")
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))

@app.route('/profile/<username>')
def profile(username):
    username = username.lower()
    return render_template('profile.html', username=username, is_admin=username == 'admin')

@app.route('/admin')
def admin():
    users = ['admin', 'user1', 'user2']
    return render_template('admin.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)