from app import db
from app.models.tanaman import Tanaman
from app.models.jenis_tanaman import JenisTanaman


def get_all():
    return Tanaman.query.order_by(Tanaman.id.asc()).all()


def search(keyword):
    return Tanaman.query.join(JenisTanaman).filter(
        db.or_(
            Tanaman.nama.ilike(f"%{keyword}%"),
            JenisTanaman.nama_jenis.ilike(f"%{keyword}%")
        )
    ).order_by(Tanaman.id.asc()).all()


def get_by_id(tanaman_id):
    return Tanaman.query.get(tanaman_id)


def create(data):
    tanaman = Tanaman(
        nama=data["nama"],
        jenis_id=data["jenis_id"],
        lahan_id=data["lahan_id"],
        tanggal=data["tanggal"]
    )

    db.session.add(tanaman)
    return tanaman

def update(tanaman, data):
    tanaman.nama = data["nama"]
    tanaman.jenis_id = data["jenis_id"]
    tanaman.lahan_id = data["lahan_id"]
    tanaman.tanggal = data["tanggal"]

    return tanaman


def delete(tanaman):
    db.session.delete(tanaman)