import os

os.environ["DATABASE_URL"] = "postgresql:///blogly_test"

from unittest import TestCase

from app import app, db
from models import DEFAULT_IMAGE_URL, User, Post

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        db.session.rollback()

        # As you add more models later in the exercise, you'll want to delete
        # all of their records before each test just as we're doing with the
        # User model below.
        User.query.delete()

        test_user = User(
            first_name="test1_first",
            last_name="test1_last",
            image_url=None,
        )

        db.session.add(test_user)
        db.session.commit()

        # We can hold onto our test_user's id by attaching it to self (which is
        # accessible throughout this test class). This way, we'll be able to
        # rely on this user in our tests without needing to know the numeric
        # value of their id, since it will change each time our tests are run.
        self.user_id = test_user.id
        self.first_name = test_user.first_name

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_users(self):
        """Tests that users request shows test instance."""
        with app.test_client() as c:
            resp = c.get("/users")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("test1_first", html)
            self.assertIn("test1_last", html)

    def test_new_user_form(self):
        """Tests adding a new user route."""
        with app.test_client() as c:
            resp = c.get("/users/new")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("Create a User", html)


    def test_redirection(self):
        """Tests that redirect works."""
        with app.test_client() as client:
            resp = client.post(
                "/users/new",
                data = {
                    'first_name': 'Yagiz' ,
                    "last_name": "Ulasoglu",
                    "image_url": ""})
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/users")

    def test_new_user_form(self):
        """Tests that new user is added to database and that redirect contains
        the new user."""
        with app.test_client() as c:
            resp = c.post(
                "/users/new",
                follow_redirects=True,
                data = {
                    'first_name': 'Yagiz' ,
                    "last_name":"Ulasoglu",
                    'image_url': ""})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Users", html)
            self.assertIn('Yagiz', html)
            self.assertIn('Ulasoglu', html)



    def test_show_user(self):
        """Tests that showing a single user works."""
        with app.test_client() as c:
            resp = c.get(f"/users/{self.user_id}/")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn(f'{self.first_name}', html)


    def test_edit_user(self):
        """Tests that editing a user works with the database and shows on
        the users page."""
        with app.test_client() as c:
            resp = c.post(
                f"/users/{self.user_id}/edit",
                follow_redirects=True,
                data = {
                    'first_name': "Dolphin",
                    "last_name":"Ulasoglu",
                    'image_url': ""})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Ulasoglu", html)
            self.assertNotIn('Yagiz', html)
            self.assertIn("Dolphin", html)


    def test_delete_user(self):
        """Tests that deleting a user works with the database and that user no
         longer appears on the users page."""
        with app.test_client() as c:
            resp = c.get("/users")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("test1_first", html)
            self.assertIn("test1_last", html)

        with app.test_client() as c:
            resp = c.post(f"/users/{self.user_id}/delete", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("test1_first", html)
            self.assertNotIn('test1_last', html)


class PostViewTestCase(TestCase):
    """Test views for posts."""

    def setUp(self):
        """Create test client, add sample data."""

        db.session.rollback()

        Post.query.delete()

        test_user = User(
            first_name="test1_first",
            last_name="test1_last",
            image_url=None,
        )

        db.session.add(test_user)
        db.session.commit()

        self.user_id = test_user.id

        test_post = Post(
            title="test1_title",
            content="test1_content",
            user_id = self.user_id,
        )

        db.session.add(test_user)
        db.session.commit()

        self.post_id = test_post.id


    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()


    def test_new_post_form(self):
        """Tests showing the new post form."""
        with app.test_client() as c:
            resp = c.get(f"/users/{self.user_id}/posts/new")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("Add Post for", html)

    def test_post_list(self):
        """Tests showing the posts."""
        with app.test_client() as c:
            resp = c.get(f"/posts/{self.post_id}/")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("Add Post for", html)
