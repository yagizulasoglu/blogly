"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'data:image/webp;base64,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7ZkHLLrZNJZm9+HN0zow5iSs041umvLX2hkuH3YpvSZS/GB0vis22tC9ObW9pNPT3T06dzZEMx5Mq+4KQ9+8yGlvdKJpcLzyvmOzp94g+gvC/gjUX4IAUSQtH3maEZaT2F3Qg5CQKw0qKFjhlX/hYzbsjAAQTcRLjbwviiPzefxqwUfsTf+qat6bMCtySQUW0j5XvUlUYDDOibum2tscG7SK83I1dVwE1PUCt2rAUWSMhaOGxgGHmm4N37vVRTqBikqVNxc+l70e4+t118a6ghquQGF25vLB7jCplIpHnZYBvF02tlWh/wqCumDBUWt+cBgrebNrVdkej7stNcnIFbXvM68OfPQGuTLVHhJVUhMAlzk/P0h99YNyN+5JPNPiSMBJq/IufUuOjgZvi4t9OuhwvGjf3+hfly0SGmITOC/CAYAARVhJRkoAAABFeGlmAABJSSoACAAAAAEADgECACoAAAAaAAAAAAAAAE9mZi1sZWFzaCBkb2cgcGFyayBpbiBOb3J0aGVybiBDYWxpZm9ybmlhLlhNUCDNAgAAaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwAJPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KCQk8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOklwdGM0eG1wQ29yZT0iaHR0cDovL2lwdGMub3JnL3N0ZC9JcHRjNHhtcENvcmUvMS4wL3htbG5zLyIgeG1sbnM6R2V0dHlJbWFnZXNHSUZUPSJodHRwOi8veG1wLmdldHR5aW1hZ2VzLmNvbS9naWZ0LzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGx1cz0iaHR0cDovL25zLnVzZXBsdXMub3JnL2xkZi94bXAvMS4wLyIgcGhvdG9zaG9wOkNyZWRpdD0iR2V0dHkgSW1hZ2VzL2lTdG9ja3Bob3RvIiBHZXR0eUltYWdlc0dJRlQ6QXNzZXRJRD0iMTA1NjUwODUxOCIgPgo8ZGM6Y3JlYXRvcj48cmRmOlNlcT48cmRmOmxpPnloZWxmbWFuPC9yZGY6bGk+PC9yZGY6U2VxPjwvZGM6Y3JlYXRvcj48ZGM6ZGVzY3JpcHRpb24+PHJkZjpBbHQ+PHJkZjpsaSB4bWw6bGFuZz0ieC1kZWZhdWx0Ij5PZmYtbGVhc2ggZG9nIHBhcmsgaW4gTm9ydGhlcm4gQ2FsaWZvcm5pYS48L3JkZjpsaT48L3JkZjpBbHQ+PC9kYzpkZXNjcmlwdGlvbj4KCQk8L3JkZjpEZXNjcmlwdGlvbj4KCTwvcmRmOlJERj4KAA=='

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User in the blog"""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    first_name = db.Column(
        db.String(50),
        nullable=False,
    )

    last_name = db.Column(
        db.String(50),
        nullable=False,
    )

    image_url = db.Column(
        db.Text,
        default = DEFAULT_IMAGE_URL
    )

class Post(db.Model):
    """Posts in the blog"""

    __tablename__ = "posts"

    user = db.relationship('User', backref='posts')

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    title = db.Column(
        db.String(50),
        nullable=False,
    )

    content = db.Column(
        db.Text,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now(),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False,
        )

class PostTag(db.Model):
    """Tag on one post"""
    __tablename__ = "post_tags"

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id'),
        primary_key=True,
        )

    tag_id = db.Column(
        db.Integer,
        db.ForeignKey('tags.id'),
        primary_key=True,
    )

class Tag(db.Model):
    """Tags that can be added to posts"""
    __tablename__ = "tags"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    posts = db.relationship(
        'Post', secondary='post_tags', backref='tags'
    )




