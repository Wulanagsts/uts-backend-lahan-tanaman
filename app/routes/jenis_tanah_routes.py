
from flask import Blueprint, request

from app.services import jenis_tanah_service
from app.utils.response import (
    success_response,
    fail_response,
    error_response
)

jenis_tanah_bp = Blueprint(
    "jenis_tanah",
    __name__,
    url_prefix="/api/v1/jenis-tanah"
)

def jenis_tanah_to_dict(jenis_tanah):
    return {
        "id": jenis_tanah.id,
        "namaJenis": jenis_tanah.nama_jenis
    }


@jenis_tanah_bp.route("", methods=["GET"])
def get_all_jenis_tanah():
    data = jenis_tanah_service.get_all_jenis_tanah()

    return success_response(
        [jenis_tanah_to_dict(item) for item in data],
        "Data jenis tanah berhasil diambil."
    )


@jenis_tanah_bp.route("/<int:jenis_tanah_id>", methods=["GET"])
def get_jenis_tanah_by_id(jenis_tanah_id):
    data = jenis_tanah_service.get_jenis_tanah_by_id(
        jenis_tanah_id
    )

    if not data:
        return fail_response(
            {"jenis_tanah": ["Data jenis tanah tidak ditemukan."]},
            404
        )

    return success_response(
        jenis_tanah_to_dict(data),
        "Data jenis tanah berhasil ditemukan."
    )


@jenis_tanah_bp.route("", methods=["POST"])
def create_jenis_tanah():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        jenis_tanah = jenis_tanah_service.create_jenis_tanah(data)

        return success_response(
            jenis_tanah_to_dict(jenis_tanah),
            "Jenis tanah berhasil ditambahkan.",
            201
        )

    except ValueError as e:
        return fail_response({"jenis_tanah": [str(e)]}, 400)

    except Exception:
        return error_response()


@jenis_tanah_bp.route("/<int:jenis_tanah_id>", methods=["PUT"])
def update_jenis_tanah(jenis_tanah_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        jenis_tanah = jenis_tanah_service.update_jenis_tanah(
            jenis_tanah_id,
            data
        )

        if not jenis_tanah:
            return fail_response(
                {"jenis_tanah": ["Data jenis tanah tidak ditemukan."]},
                404
            )

        return success_response(
            jenis_tanah_to_dict(jenis_tanah),
            "Jenis tanah berhasil diperbarui."
        )

    except ValueError as e:
        return fail_response({"jenis_tanah": [str(e)]}, 400)

    except Exception:
        return error_response()


@jenis_tanah_bp.route("/<int:jenis_tanah_id>", methods=["DELETE"])
def delete_jenis_tanah(jenis_tanah_id):
    try:
        result = jenis_tanah_service.delete_jenis_tanah(
            jenis_tanah_id
        )

        if not result:
            return fail_response(
                {"jenis_tanah": ["Data jenis tanah tidak ditemukan."]},
                404
            )

        return success_response(
            message="Jenis tanah berhasil dihapus."
        )

    except ValueError as e:
        return fail_response({"jenis_tanah": [str(e)]}, 400)

    except Exception:
        return error_response()
