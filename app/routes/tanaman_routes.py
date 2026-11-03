
from flask import Blueprint, request
from app.services import tanaman_service
from app.utils.response import (
    success_response,
    fail_response,
    error_response
)

tanaman_bp = Blueprint(
    "tanaman",
    __name__,
    url_prefix="/api/v1/tanaman"
)

def tanaman_to_dict(tanaman):
    return {
        "id": tanaman.id,
        "nama": tanaman.nama,
        "jenis": tanaman.jenis_tanaman.nama_jenis,
        "jenisId": tanaman.jenis_id,
        "lahanId": tanaman.lahan_id,
        "lahanNama": tanaman.lahan.nama,
        "tanggal": tanaman.tanggal.isoformat()
    }

@tanaman_bp.route("", methods=["GET"])
def get_all_tanaman():
    keyword = request.args.get("search", "").strip()
    jenis = request.args.get("jenis", "").strip()

    if keyword:
        data = tanaman_service.search_tanaman(keyword)
    else:
        data = tanaman_service.get_all_tanaman()

    if jenis:
        data = [
            item for item in data
            if item.jenis_tanaman.nama_jenis.lower() == jenis.lower()
        ]

    return success_response(
        [tanaman_to_dict(item) for item in data],
        "Data tanaman berhasil diambil."
    )
    
# GET: Mengambil tanaman berdasarkan ID
@tanaman_bp.route("/<int:tanaman_id>", methods=["GET"])
def get_tanaman_by_id(tanaman_id):
    data = tanaman_service.get_tanaman_by_id(tanaman_id)

    if not data:
        return fail_response(
            {"tanaman": ["Data tanaman tidak ditemukan."]},
            404
        )

    return success_response(
        tanaman_to_dict(data),
        "Data tanaman berhasil ditemukan."
    )


# POST: Menambahkan data tanaman
@tanaman_bp.route("", methods=["POST"])
def create_tanaman():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        tanaman = tanaman_service.create_tanaman(data)

        return success_response(
            tanaman_to_dict(tanaman),
            "Data tanaman berhasil ditambahkan.",
            201
        )

    except ValueError as e:
        return fail_response({"tanaman": [str(e)]})

    except Exception:
        return error_response()


# PUT: Mengubah data tanaman
@tanaman_bp.route("/<int:tanaman_id>", methods=["PUT"])
def update_tanaman(tanaman_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": ["Data JSON wajib dikirim."]},
            400
        )

    try:
        tanaman = tanaman_service.update_tanaman(tanaman_id, data)

        if not tanaman:
            return fail_response(
                {"tanaman": ["Data tanaman tidak ditemukan."]},
                404
            )

        return success_response(
            tanaman_to_dict(tanaman),
            "Data tanaman berhasil diperbarui."
        )

    except ValueError as e:
        return fail_response({"tanaman": [str(e)]})

    except Exception:
        return error_response()


# DELETE: Menghapus data tanaman
@tanaman_bp.route("/<int:tanaman_id>", methods=["DELETE"])
def delete_tanaman(tanaman_id):
    try:
        result = tanaman_service.delete_tanaman(tanaman_id)

        if not result:
            return fail_response(
                {"tanaman": ["Data tanaman tidak ditemukan."]},
                404
            )

        return success_response(
            message="Data tanaman berhasil dihapus."
        )

    except ValueError as e:
        return fail_response({"tanaman": [str(e)]})

    except Exception:
        return error_response()