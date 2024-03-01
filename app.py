"""Blogly application."""

import os

from flask import Flask, redirect, render_template, request
from models import db, connect_db, User, Post, Tag, PostTag


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
    current_user_posts = Post.query.filter_by(user_id=user_id).all()

    for post in current_user_posts:
        db.session.delete(post)

    db.session.delete(current_user)
    db.session.commit()

    return redirect('/users')

@app.get('/users/<int:user_id>/posts/new')
def show_add_post_form(user_id):
    current_user = User.query.get_or_404(user_id)
    return render_template('add-post.html', user = current_user)



@app.post('/users/<int:user_id>/posts/new')
def add_post(user_id):
    """Adds post to the database and reirects to the users route."""
    current_user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'], content=request.form['content'], user_id=user_id)


    db.session.add(new_post)
    db.session.commit()



    return redirect(f"/users/{current_user.id}")

@app.get('/posts/<int:post_id>')
def show_post(post_id):
    """Shows the post and enables the user to edit or delete it"""

    post = Post.query.get_or_404(post_id)

    return render_template('show-post.html', post = post)

@app.get('/posts/<int:post_id>/edit')
def show_edit(post_id):
    """Shows the edit form to the user"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit-post.html', post = post)

@app.post('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Edits the post"""
    current_post = Post.query.get_or_404(post_id)

    current_post.title = request.form['title']
    current_post.content = request.form['content']

    db.session.commit()

    return redirect(f'/posts/{post_id}/')

@app.post('/posts/<int:post_id>/delete')
def delete_post(post_id):
    """Deletes the post"""
    current_post = Post.query.get_or_404(post_id)


    db.session.delete(current_post)
    db.session.commit()

    return redirect(f'/users/{current_post.user_id}')

@app.get('/tags')
def get_tags():
    """Lists all tags"""

    tags = Tag.query.all()
    return render_template('list-tag.html', tags = tags)

@app.get('/tags/<int:tag_id>')
def show_tag(tag_id):
    """Shows detail about a tag"""

    tag = Tag.query.get_or_404(tag_id)

    return render_template('show-tag.html', tag = tag)

@app.get('/tags/new')
def form_tag():
    """Shows the form to add a new tag."""

    return render_template('add-tag.html')

@app.post('/tags/new')
def submit_tag():
    """Adds a new tag"""
    new_tag = Tag(name=request.form['name'])

    db.session.add(new_tag)
    db.session.commit()

    return redirect("/tags")

@app.get('/tags/<int:tag_id>/edit')
def show_edit_tag(tag_id):
    """Edits the tag"""

    tag = Tag.query.get_or_404(tag_id)
    return render_template('edit-tag.html', tag = tag)


@app.post('/tags/<int:tag_id>/edit')
def edit_tag(tag_id):
    """Edits the tag"""
    current_tag = Tag.query.get_or_404(tag_id)

    current_tag.name = request.form['name']

    db.session.commit()

    return redirect(f'/tags')

@app.post('/tags/<int:tag_id>/delete')
def delete_tags(tag_id):
    """Deletes the tag"""
    current_tag = Tag.query.get_or_404(tag_id)


    db.session.delete(current_tag)
    db.session.commit()

    return redirect(f'/tags')