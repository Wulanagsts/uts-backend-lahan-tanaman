
from app import db
from app.models.jenis_tanah import JenisTanah


def get_all():
    return JenisTanah.query.order_by(
        JenisTanah.id.asc()
    ).all()


def get_by_id(jenis_tanah_id):
    return JenisTanah.query.get(jenis_tanah_id)


def create(data):
    jenis_tanah = JenisTanah(
        nama_jenis=data["nama_jenis"]
    )

    db.session.add(jenis_tanah)

    return jenis_tanah


def update(jenis_tanah, data):
    jenis_tanah.nama_jenis = data["nama_jenis"]

    return jenis_tanah


def delete(jenis_tanah):
    db.session.delete(jenis_tanah)
