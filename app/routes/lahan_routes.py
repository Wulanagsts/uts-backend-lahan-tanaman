
from flask import Blueprint, request
from app.services import lahan_service
from app.utils.response import (
    success_response,
    fail_response,
    error_response
)

lahan_bp = Blueprint(
    "lahan",
    __name__,
    url_prefix="/api/v1/lahan"
)

def lahan_to_dict(lahan):
    return {
        "id": lahan.id,
        "nama": lahan.nama,
        "lokasi": lahan.lokasi,
        "luas": lahan.luas,
        "jenisTanah": lahan.jenis_tanah.nama_jenis,
        "jenisTanahId": lahan.jenis_tanah_id
    }

@lahan_bp.route("", methods=["GET"])
def get_all_lahan():
    keyword = request.args.get("search", "").strip()
    jenis_tanah = request.args.get("jenisTanah", "").strip()

    if keyword:
        data = lahan_service.search_lahan(keyword)
    else:
        data = lahan_service.get_all_lahan()

    if jenis_tanah:
        data = [
            item for item in data
            if item.jenis_tanah.nama_jenis.lower() == jenis_tanah.lower()
        ]

    return success_response(
        [lahan_to_dict(item) for item in data],
        "Data lahan berhasil diambil."
    )

# GET: Mengambil data lahan berdasarkan ID
@lahan_bp.route("/<int:lahan_id>", methods=["GET"])
def get_lahan_by_id(lahan_id):
    data = lahan_service.get_lahan_by_id(lahan_id)

    if not data:
        return fail_response(
            {"lahan": ["Data lahan tidak ditemukan."]},
            404
        )

    return success_response(
        lahan_to_dict(data),
        "Data lahan berhasil ditemukan."
    )


# POST: Menambahkan data lahan
@lahan_bp.route("", methods=["POST"])
def create_lahan():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        lahan = lahan_service.create_lahan(data)

        return success_response(
            lahan_to_dict(lahan),
            "Data lahan berhasil ditambahkan.",
            201
        )

    except ValueError as e:
        return fail_response({"lahan": [str(e)]})

    except Exception:
        return error_response()


# PUT: Mengubah data lahan
@lahan_bp.route("/<int:lahan_id>", methods=["PUT"])
def update_lahan(lahan_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        lahan = lahan_service.update_lahan(lahan_id, data)

        if not lahan:
            return fail_response(
                {"lahan": ["Data lahan tidak ditemukan."]},
                404
            )

        return success_response(
            lahan_to_dict(lahan),
            "Data lahan berhasil diperbarui."
        )

    except ValueError as e:
        return fail_response({"lahan": [str(e)]})

    except Exception:
        return error_response()


# DELETE: Menghapus data lahan
@lahan_bp.route("/<int:lahan_id>", methods=["DELETE"])
def delete_lahan(lahan_id):
    try:
        result = lahan_service.delete_lahan(lahan_id)

        if not result:
            return fail_response(
                {"lahan": ["Data lahan tidak ditemukan."]},
                404
            )

        return success_response(
            message="Data lahan berhasil dihapus."
        )

    except ValueError as e:
        return fail_response({"lahan": [str(e)]})

    except Exception:
        return error_response()
