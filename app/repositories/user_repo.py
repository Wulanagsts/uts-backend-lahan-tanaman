
from app import db
from app.models.user import User


def get_by_username(username):
    return User.query.filter_by(username=username).first()


def get_by_email(email):
    return User.query.filter_by(email=email).first()


def create(data):
    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=data["password_hash"]
    )

    db.session.add(user)
    return user
