
from flask import Blueprint, request
from app.services import jenis_tanaman_service
from app.utils.response import (
    success_response,
    fail_response,
    error_response
)

jenis_tanaman_bp = Blueprint(
    "jenis_tanaman",
    __name__,
    url_prefix="/api/v1/jenis-tanaman"
)

def jenis_tanaman_to_dict(jenis_tanaman):
    return {
        "id": jenis_tanaman.id,
        "namaJenis": jenis_tanaman.nama_jenis
    }


# GET: Mengambil semua jenis tanaman
@jenis_tanaman_bp.route("", methods=["GET"])
def get_all_jenis_tanaman():
    data = jenis_tanaman_service.get_all_jenis_tanaman()

    return success_response(
        [jenis_tanaman_to_dict(item) for item in data],
        "Data jenis tanaman berhasil diambil."
    )


# GET: Mengambil jenis tanaman berdasarkan ID
@jenis_tanaman_bp.route("/<int:jenis_tanaman_id>", methods=["GET"])
def get_jenis_tanaman_by_id(jenis_tanaman_id):
    data = jenis_tanaman_service.get_jenis_tanaman_by_id(
        jenis_tanaman_id
    )

    if not data:
        return fail_response(
            {"jenis_tanaman": ["Data jenis tanaman tidak ditemukan."]},
            404
        )

    return success_response(
        jenis_tanaman_to_dict(data),
        "Data jenis tanaman berhasil ditemukan."
    )


# POST: Menambahkan jenis tanaman
@jenis_tanaman_bp.route("", methods=["POST"])
def create_jenis_tanaman():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        jenis_tanaman = jenis_tanaman_service.create_jenis_tanaman(data)

        return success_response(
            jenis_tanaman_to_dict(jenis_tanaman),
            "Jenis tanaman berhasil ditambahkan.",
            201
        )

    except ValueError as e:
        return fail_response({"jenis_tanaman": [str(e)]})

    except Exception:
        return error_response()


# PUT: Mengubah jenis tanaman
@jenis_tanaman_bp.route("/<int:jenis_tanaman_id>", methods=["PUT"])
def update_jenis_tanaman(jenis_tanaman_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        jenis_tanaman = jenis_tanaman_service.update_jenis_tanaman(
            jenis_tanaman_id,
            data
        )

        if not jenis_tanaman:
            return fail_response(
                {"jenis_tanaman": ["Data jenis tanaman tidak ditemukan."]},
                404
            )

        return success_response(
            jenis_tanaman_to_dict(jenis_tanaman),
            "Jenis tanaman berhasil diperbarui."
        )

    except ValueError as e:
        return fail_response({"jenis_tanaman": [str(e)]})

    except Exception:
        return error_response()


# DELETE: Menghapus jenis tanaman
@jenis_tanaman_bp.route("/<int:jenis_tanaman_id>", methods=["DELETE"])
def delete_jenis_tanaman(jenis_tanaman_id):
    try:
        result = jenis_tanaman_service.delete_jenis_tanaman(
            jenis_tanaman_id
        )

        if not result:
            return fail_response(
                {"jenis_tanaman": ["Data jenis tanaman tidak ditemukan."]},
                404
            )

        return success_response(
            message="Jenis tanaman berhasil dihapus."
        )

    except ValueError as e:
        return fail_response({"jenis_tanaman": [str(e)]})

    except Exception:
        return error_response()
