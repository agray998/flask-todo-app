from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Tasks

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test task
        sample1 = Tasks(name="Testtask", desc='A test task', status='incomplete')

        # save task to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testtask', response.data)

# Test adding
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('add'),
            data = dict(task_name="Newtask", task_desc='another task', task_stat='incomplete'),
            follow_redirects=True
        )
        self.assertIn(b'Newtask',response.data)
