
from app import db
from app.models.lahan import Lahan


def get_all():
    return Lahan.query.order_by(Lahan.id.asc()).all()


def search(keyword):
    return Lahan.query.filter(
        db.or_(
            Lahan.nama.ilike(f"%{keyword}%"),
            Lahan.lokasi.ilike(f"%{keyword}%")
        )
    ).order_by(Lahan.id.asc()).all()


def get_by_id(lahan_id):
    return Lahan.query.get(lahan_id)


def create(data):
    lahan = Lahan(
        nama=data["nama"],
        lokasi=data["lokasi"],
        luas=data["luas"],
        jenis_tanah_id=data["jenis_tanah_id"]
    )

    db.session.add(lahan)
    return lahan


def update(lahan, data):
    lahan.nama = data["nama"]
    lahan.lokasi = data["lokasi"]
    lahan.luas = data["luas"]
    lahan.jenis_tanah_id = data["jenis_tanah_id"]

    return lahan


def delete(lahan):
    db.session.delete(lahan)
