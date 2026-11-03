
from datetime import date

from app import db
from app.repositories import tanaman_repo, lahan_repo, jenis_tanaman_repo


def get_all_tanaman():
    return tanaman_repo.get_all()

def search_tanaman(keyword):
    return tanaman_repo.search(keyword)

def get_tanaman_by_id(tanaman_id):
    return tanaman_repo.get_by_id(tanaman_id)


def create_tanaman(data):
    nama = data.get("nama", "").strip()
    jenis_id = data.get("jenis_id")
    lahan_id = data.get("lahan_id")
    tanggal = data.get("tanggal")

    if not nama:
        raise ValueError("Nama tanaman wajib diisi.")

    try:
        jenis_id = int(jenis_id)
    except (TypeError, ValueError):
        raise ValueError("Jenis tanaman wajib dipilih.")

    try:
        lahan_id = int(lahan_id)
    except (TypeError, ValueError):
        raise ValueError("Lahan wajib dipilih.")

    jenis_tanaman = jenis_tanaman_repo.get_by_id(jenis_id)
    if not jenis_tanaman:
        raise ValueError("Jenis tanaman tidak ditemukan.")

    lahan = lahan_repo.get_by_id(lahan_id)
    if not lahan:
        raise ValueError("Data lahan tidak ditemukan.")

    try:
        tanggal = date.fromisoformat(tanggal)
    except (TypeError, ValueError):
        raise ValueError("Tanggal penanaman tidak valid.")

    try:
        tanaman = tanaman_repo.create({
            "nama": nama,
            "jenis_id": jenis_id,
            "lahan_id": lahan_id,
            "tanggal": tanggal
        })

        db.session.commit()
        return tanaman

    except Exception:
        db.session.rollback()
        raise


def update_tanaman(tanaman_id, data):
    tanaman = tanaman_repo.get_by_id(tanaman_id)

    if not tanaman:
        return None

    nama = data.get("nama", "").strip()
    jenis_id = data.get("jenis_id")
    lahan_id = data.get("lahan_id")
    tanggal = data.get("tanggal")

    if not nama:
        raise ValueError("Nama tanaman wajib diisi.")

    try:
        jenis_id = int(jenis_id)
    except (TypeError, ValueError):
        raise ValueError("Jenis tanaman wajib dipilih.")

    try:
        lahan_id = int(lahan_id)
    except (TypeError, ValueError):
        raise ValueError("Lahan wajib dipilih.")

    jenis_tanaman = jenis_tanaman_repo.get_by_id(jenis_id)
    if not jenis_tanaman:
        raise ValueError("Jenis tanaman tidak ditemukan.")

    lahan = lahan_repo.get_by_id(lahan_id)
    if not lahan:
        raise ValueError("Data lahan tidak ditemukan.")

    try:
        tanggal = date.fromisoformat(tanggal)
    except (TypeError, ValueError):
        raise ValueError("Tanggal penanaman tidak valid.")

    try:
        tanaman_repo.update(tanaman, {
            "nama": nama,
            "jenis_id": jenis_id,
            "lahan_id": lahan_id,
            "tanggal": tanggal
        })

        db.session.commit()
        return tanaman

    except Exception:
        db.session.rollback()
        raise


def delete_tanaman(tanaman_id):
    tanaman = tanaman_repo.get_by_id(tanaman_id)

    if not tanaman:
        return None

    try:
        tanaman_repo.delete(tanaman)
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        raise
