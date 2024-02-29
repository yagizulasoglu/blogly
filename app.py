"""Blogly application."""

import os

from flask import Flask, redirect, render_template, request
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

    return redirect ("/users")


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
    return render_template("user-profile.html", user=user)


@app.get('/users/<int:user_id>/edit')
def show_edit_user(user_id):
    """Shows the edit page to the user"""
    user = User.query.get_or_404(user_id)
    return render_template('edit-profile.html', user = user)



@app.post('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Edits the current user"""
    current_user = User.query.get_or_404(user_id)

    current_user.first_name = request.form['first_name']
    current_user.last_name = request.form['last_name']
    current_user.image_url = request.form['image_url']

    db.session.add(current_user)
    db.session.commit()

    return redirect('/users')


@app.post('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Deletes the specified user"""
    current_user = User.query.get_or_404(user_id)

    db.session.delete(current_user)
    db.session.commit()

    return redirect('/users')



