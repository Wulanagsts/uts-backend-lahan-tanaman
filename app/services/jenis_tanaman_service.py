from app import db
from app.repositories import jenis_tanaman_repo


def get_all_jenis_tanaman():
    return jenis_tanaman_repo.get_all()


def get_jenis_tanaman_by_id(jenis_tanaman_id):
    return jenis_tanaman_repo.get_by_id(jenis_tanaman_id)


def create_jenis_tanaman(data):
    nama_jenis = data.get("nama_jenis", "").strip()

    if not nama_jenis:
        raise ValueError("Nama jenis tanaman wajib diisi.")

    existing = jenis_tanaman_repo.get_all()

    for item in existing:
        if item.nama_jenis.lower() == nama_jenis.lower():
            raise ValueError("Jenis tanaman sudah terdaftar.")

    try:
        jenis_tanaman = jenis_tanaman_repo.create({
            "nama_jenis": nama_jenis
        })

        db.session.commit()
        return jenis_tanaman

    except Exception:
        db.session.rollback()
        raise


def update_jenis_tanaman(jenis_tanaman_id, data):
    jenis_tanaman = jenis_tanaman_repo.get_by_id(jenis_tanaman_id)

    if not jenis_tanaman:
        return None

    nama_jenis = data.get("nama_jenis", "").strip()

    if not nama_jenis:
        raise ValueError("Nama jenis tanaman wajib diisi.")

    existing = jenis_tanaman_repo.get_all()

    for item in existing:
        if item.id != jenis_tanaman_id and item.nama_jenis.lower() == nama_jenis.lower():
            raise ValueError("Jenis tanaman sudah terdaftar.")

    try:
        jenis_tanaman_repo.update(jenis_tanaman, {
            "nama_jenis": nama_jenis
        })

        db.session.commit()
        return jenis_tanaman

    except Exception:
        db.session.rollback()
        raise


def delete_jenis_tanaman(jenis_tanaman_id):
    jenis_tanaman = jenis_tanaman_repo.get_by_id(jenis_tanaman_id)

    if not jenis_tanaman:
        return None

    if jenis_tanaman.tanamans:
        raise ValueError(
            "Jenis tanaman tidak dapat dihapus karena masih digunakan oleh data tanaman."
        )

    try:
        jenis_tanaman_repo.delete(jenis_tanaman)
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        raise