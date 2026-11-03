
import re

from werkzeug.security import generate_password_hash

from app import db
from app.repositories import user_repo


def register_user(data):
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")
    confirm_password = data.get("confirmPassword", "")

    # Validasi username
    if not username:
        raise ValueError("Username wajib diisi.")

    if len(username) < 4:
        raise ValueError("Username minimal 4 karakter.")

    # Validasi email
    if not email:
        raise ValueError("Email wajib diisi.")

    email_pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"

    if not re.match(email_pattern, email):
        raise ValueError("Format email tidak valid.")

    # Validasi password
    if not password:
        raise ValueError("Password wajib diisi.")

    if len(password) < 6:
        raise ValueError("Password minimal 6 karakter.")

    if password != confirm_password:
        raise ValueError("Konfirmasi password tidak sesuai.")

    # Memeriksa username dan email
    if user_repo.get_by_username(username):
        raise ValueError("Username sudah digunakan.")

    if user_repo.get_by_email(email):
        raise ValueError("Email sudah terdaftar.")

    # Mengenkripsi password
    password_hash = generate_password_hash(password)

    try:
        user = user_repo.create({
            "username": username,
            "email": email,
            "password_hash": password_hash
        })

        db.session.commit()
        return user

    except Exception:
        db.session.rollback()
        raise
