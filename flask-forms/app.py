from flask import Flask, render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

users = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        if email in users:
            flash("Email already registered. Try logging in.")
            return redirect(url_for("login"))
        users[email] = {"name": form.name.data, "password": form.password.data}
        flash(f"Account created! Welcome, {form.name.data}.")
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.get(form.email.data)
        if user and user["password"] == form.password.data:
            flash(f"Welcome back, {user['name']}!")
            return redirect(url_for("home"))
        flash("Invalid email or password.")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
