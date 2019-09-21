# services/users/project/tests/test_user_model.py


import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user

from sqlalchemy.exc import IntegrityError


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('justatest', 'test@test.com', 'test')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)
        self.assertTrue(user.password)

    def test_add_user_duplicate_username(self):
        add_user('justatest', 'test@test.com', 'graeterthaneight')
        duplicate_user = User(
            username='justatest',
            email='test@test2.com',
            password='greaterthaneight',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        add_user('justauser', 'test@test.com', 'graeterthaneight')
        duplicate_user = User(
            username='justanothertest',
            email='test@test.com',
            password='greaterthaneight',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user('justatest', 'test@test.com', 'graterthaneight')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_password_are_random(self):
        user_one = add_user('jastatest', 'test@test.com', 'greaterthaneight')
        user_two = add_user('jastatest2', 'test@test2.com',
                            'greaterthenneight')
        self.assertNotEqual(user_one.password, user_two.password)

    def test_encode_auth_token(self):
        user = add_user('justatest', 'test@test.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_auth_token(auth_token), user.id)


if __name__ == '__main__':
    unittest.main()
