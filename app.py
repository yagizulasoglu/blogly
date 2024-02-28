"""Blogly application."""

import os

from flask import Flask
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.get("/")
def redirect_to_users():
    """Redirects to the users route"""

    redirect ("/users")


@app.get("/users")
def users():
    """Lists all of the users"""

    users = User.query.all()
    return render_template("list.html", users=users)

@app.get("/users/new")
def new_user_form():
    """Shows the form for creating a new user"""

    return render_template("create-user.html")

@app.post("/users/new")
def new_user_info():
    """Sends the info about the new user to the server"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.get("/users/<int:user_id>")
def show_user(user_id):
    """Show info on an user."""

    user = User.query.get_or_404(user_id)
    return render_template("user-profile.html" user=user)