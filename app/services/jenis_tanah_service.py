
from app import db
from app.repositories import jenis_tanah_repo


def get_all_jenis_tanah():
    return jenis_tanah_repo.get_all()


def get_jenis_tanah_by_id(jenis_tanah_id):
    return jenis_tanah_repo.get_by_id(jenis_tanah_id)


def create_jenis_tanah(data):
    nama_jenis = data.get("nama_jenis", "").strip()

    if not nama_jenis:
        raise ValueError("Nama jenis tanah wajib diisi.")

    existing = jenis_tanah_repo.get_all()

    for item in existing:
        if item.nama_jenis.lower() == nama_jenis.lower():
            raise ValueError("Jenis tanah sudah tersedia.")

    try:
        jenis_tanah = jenis_tanah_repo.create({
            "nama_jenis": nama_jenis
        })

        db.session.commit()
        return jenis_tanah

    except Exception:
        db.session.rollback()
        raise


def update_jenis_tanah(jenis_tanah_id, data):
    jenis_tanah = jenis_tanah_repo.get_by_id(
        jenis_tanah_id
    )

    if not jenis_tanah:
        return None

    nama_jenis = data.get("nama_jenis", "").strip()

    if not nama_jenis:
        raise ValueError("Nama jenis tanah wajib diisi.")

    existing = jenis_tanah_repo.get_all()

    for item in existing:
        if (
            item.id != jenis_tanah_id
            and item.nama_jenis.lower() == nama_jenis.lower()
        ):
            raise ValueError("Jenis tanah sudah tersedia.")

    try:
        jenis_tanah_repo.update(
            jenis_tanah,
            {"nama_jenis": nama_jenis}
        )

        db.session.commit()
        return jenis_tanah

    except Exception:
        db.session.rollback()
        raise


def delete_jenis_tanah(jenis_tanah_id):
    jenis_tanah = jenis_tanah_repo.get_by_id(
        jenis_tanah_id
    )

    if not jenis_tanah:
        return None

    if jenis_tanah.lahans:
        raise ValueError(
            "Jenis tanah tidak dapat dihapus karena masih digunakan oleh data lahan."
        )

    try:
        jenis_tanah_repo.delete(jenis_tanah)
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        raise
