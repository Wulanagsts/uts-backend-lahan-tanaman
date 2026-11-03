
from app import db


class Lahan(db.Model):
    __tablename__ = "lahan"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    lokasi = db.Column(db.String(150), nullable=False)
    luas = db.Column(db.Float, nullable=False)

    jenis_tanah_id = db.Column(
        db.Integer,
        db.ForeignKey("jenis_tanah.id"),
        nullable=False
    )

    # Relasi ke jenis tanah
    jenis_tanah = db.relationship(
        "JenisTanah",
        back_populates="lahans"
    )

    # Relasi ke banyak tanaman
    tanamans = db.relationship(
        "Tanaman",
        back_populates="lahan",
        lazy=True
    )
