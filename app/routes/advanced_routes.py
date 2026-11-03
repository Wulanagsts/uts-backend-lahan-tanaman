
from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

from app import db
from app.models.tanaman import Tanaman
from app.models.jenis_tanaman import JenisTanaman
from app.models.lahan import Lahan
from app.utils.response import success_response, fail_response, error_response


advanced_bp = Blueprint(
    "advanced_api",
    __name__,
    url_prefix="/api/v1/advanced"
)


# ==========================================
# 1. PAGINATION DAN PENCARIAN DATA TANAMAN
# ==========================================

@advanced_bp.route("/tanaman", methods=["GET"])
def get_paginated_tanaman():

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)
    search = request.args.get("search", "").strip()

    if page < 1 or per_page < 1 or per_page > 100:
        return fail_response(
            {
                "pagination": "Page minimal 1 dan per_page antara 1 sampai 100."
            },
            400
        )

    query = Tanaman.query.join(JenisTanaman)

    if search:
        query = query.filter(
            db.or_(
                Tanaman.nama.ilike(f"%{search}%"),
                JenisTanaman.nama_jenis.ilike(f"%{search}%")
            )
        )

    pagination = query.order_by(Tanaman.id.asc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    data = [
        {
            "id": item.id,
            "nama": item.nama,
            "jenis": item.jenis_tanaman.nama_jenis,
            "jenisId": item.jenis_id,
            "lahanId": item.lahan_id,
            "lahanNama": item.lahan.nama,
            "tanggal": item.tanggal.isoformat()
        }
        for item in pagination.items
    ]

    return success_response(
        {
            "items": data,
            "pagination": {
                "current_page": pagination.page,
                "per_page": pagination.per_page,
                "total_pages": pagination.pages,
                "total_items": pagination.total
            }
        },
        "Data tanaman berhasil diambil."
    )


# ==========================================
# 2. TRANSAKSI ATOMIK MULTI-TABEL
# ==========================================

@advanced_bp.route("/transaction-demo", methods=["POST"])
def create_tanaman_transaction():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return fail_response(
            {"body": "Data JSON wajib diisi."},
            400
        )

    nama_jenis = data.get("nama_jenis")
    nama = data.get("nama")
    lahan_id = data.get("lahan_id")
    tanggal = data.get("tanggal")

    if not all([nama_jenis, nama, lahan_id, tanggal]):
        return fail_response(
            {
                "required": [
                    "nama_jenis",
                    "nama",
                    "lahan_id",
                    "tanggal"
                ]
            },
            400
        )

    try:
        if not isinstance(nama_jenis, str) or not isinstance(nama, str):
            return fail_response(
                {"nama": "Nama tanaman dan jenis tanaman harus berupa teks."},
                400
            )

        nama_jenis = nama_jenis.strip()
        nama = nama.strip()
        lahan_id = int(lahan_id)
        tanggal = date.fromisoformat(tanggal)

        if not nama_jenis or not nama:
            return fail_response(
                {"nama": "Nama tanaman dan jenis tanaman tidak boleh kosong."},
                400
            )

        lahan = db.session.get(Lahan, lahan_id)

        if not lahan:
            return fail_response(
                {"lahan_id": "Data lahan tidak ditemukan."},
                404
            )

        jenis_tanaman = JenisTanaman.query.filter_by(
            nama_jenis=nama_jenis
        ).first()

        if not jenis_tanaman:
            jenis_tanaman = JenisTanaman(
                nama_jenis=nama_jenis
            )
            db.session.add(jenis_tanaman)
            db.session.flush()

        tanaman = Tanaman(
            nama=nama,
            jenis_id=jenis_tanaman.id,
            lahan_id=lahan_id,
            tanggal=tanggal
        )

        db.session.add(tanaman)
        db.session.flush()

        hasil = {
            "id": tanaman.id,
            "nama": tanaman.nama,
            "jenis": jenis_tanaman.nama_jenis,
            "jenisId": tanaman.jenis_id,
            "lahanId": tanaman.lahan_id,
            "lahanNama": lahan.nama,
            "tanggal": tanaman.tanggal.isoformat()
        }

        db.session.commit()

        return success_response(
            hasil,
            "Transaksi berhasil disimpan.",
            201
        )

    except (ValueError, TypeError, AttributeError):
        db.session.rollback()
        return fail_response(
            {
                "input": "Format data tidak valid. Periksa nama, lahan_id, dan tanggal."
            },
            400
        )

    except SQLAlchemyError:
        db.session.rollback()
        return error_response(
            "Transaksi dibatalkan karena terjadi kesalahan database.",
            500
        )
