
from app import db
from app.repositories import lahan_repo, jenis_tanah_repo


def get_all_lahan():
    return lahan_repo.get_all()

def search_lahan(keyword):
    return lahan_repo.search(keyword)

def get_lahan_by_id(lahan_id):
    return lahan_repo.get_by_id(lahan_id)


def create_lahan(data):
    nama = data.get("nama", "").strip()
    lokasi = data.get("lokasi", "").strip()
    luas = data.get("luas")
    jenis_tanah_id = data.get("jenis_tanah_id")

    if not nama:
        raise ValueError("Nama lahan wajib diisi.")

    if not lokasi:
        raise ValueError("Lokasi lahan wajib diisi.")

    try:
        luas = float(luas)
    except (TypeError, ValueError):
        raise ValueError("Luas lahan harus berupa angka.")

    if luas <= 0:
        raise ValueError("Luas lahan harus lebih dari 0.")

    try:
        jenis_tanah_id = int(jenis_tanah_id)
    except (TypeError, ValueError):
        raise ValueError("Jenis tanah wajib dipilih.")

    jenis_tanah = jenis_tanah_repo.get_by_id(jenis_tanah_id)

    if not jenis_tanah:
        raise ValueError("Jenis tanah tidak ditemukan.")

    try:
        lahan = lahan_repo.create({
            "nama": nama,
            "lokasi": lokasi,
            "luas": luas,
            "jenis_tanah_id": jenis_tanah_id
        })

        db.session.commit()
        return lahan

    except Exception:
        db.session.rollback()
        raise


def update_lahan(lahan_id, data):
    lahan = lahan_repo.get_by_id(lahan_id)

    if not lahan:
        return None

    nama = data.get("nama", "").strip()
    lokasi = data.get("lokasi", "").strip()
    luas = data.get("luas")
    jenis_tanah_id = data.get("jenis_tanah_id")

    if not nama:
        raise ValueError("Nama lahan wajib diisi.")

    if not lokasi:
        raise ValueError("Lokasi lahan wajib diisi.")

    try:
        luas = float(luas)
    except (TypeError, ValueError):
        raise ValueError("Luas lahan harus berupa angka.")

    if luas <= 0:
        raise ValueError("Luas lahan harus lebih dari 0.")

    try:
        jenis_tanah_id = int(jenis_tanah_id)
    except (TypeError, ValueError):
        raise ValueError("Jenis tanah wajib dipilih.")

    jenis_tanah = jenis_tanah_repo.get_by_id(jenis_tanah_id)

    if not jenis_tanah:
        raise ValueError("Jenis tanah tidak ditemukan.")

    try:
        lahan_repo.update(lahan, {
            "nama": nama,
            "lokasi": lokasi,
            "luas": luas,
            "jenis_tanah_id": jenis_tanah_id
        })

        db.session.commit()
        return lahan

    except Exception:
        db.session.rollback()
        raise


def delete_lahan(lahan_id):
    lahan = lahan_repo.get_by_id(lahan_id)

    if not lahan:
        return None

    if lahan.tanamans:
        raise ValueError(
            "Lahan tidak dapat dihapus karena masih memiliki data tanaman."
        )

    try:
        lahan_repo.delete(lahan)
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        raise
