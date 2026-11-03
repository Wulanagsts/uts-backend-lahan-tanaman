
from flask import Blueprint, request
from app.services import user_service
from app.utils.response import (
    success_response,
    fail_response,
    error_response
)

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/api/v1/users"
)

# POST: Registrasi pengguna
@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        user = user_service.register_user(data)

        return success_response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "Registrasi berhasil.",
            201
        )

    except ValueError as e:
        return fail_response(
            {"user": [str(e)]},
            400
        )

    except Exception:
        return error_response()
