
from app import db


class JenisTanah(db.Model):
    __tablename__ = "jenis_tanah"

    id = db.Column(db.Integer, primary_key=True)
    nama_jenis = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    # Relasi: satu jenis tanah dapat digunakan banyak lahan
    lahans = db.relationship(
        "Lahan",
        back_populates="jenis_tanah",
        lazy=True
    )
