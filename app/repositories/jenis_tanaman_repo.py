from app import db
from app.models.jenis_tanaman import JenisTanaman


def get_all():
    return JenisTanaman.query.order_by(JenisTanaman.id.asc()).all()


def get_by_id(jenis_tanaman_id):
    return JenisTanaman.query.get(jenis_tanaman_id)


def create(data):
    jenis_tanaman = JenisTanaman(
        nama_jenis=data["nama_jenis"]
    )
    db.session.add(jenis_tanaman)
    return jenis_tanaman


def update(jenis_tanaman, data):
    jenis_tanaman.nama_jenis = data["nama_jenis"]
    return jenis_tanaman


def delete(jenis_tanaman):
    db.session.delete(jenis_tanaman)