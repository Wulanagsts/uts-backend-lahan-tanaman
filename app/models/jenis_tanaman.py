
from app import db


class JenisTanaman(db.Model):
    __tablename__ = "jenis_tanaman"

    id = db.Column(db.Integer, primary_key=True)
    nama_jenis = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    # Relasi: satu jenis tanaman dapat digunakan banyak tanaman
    tanamans = db.relationship(
        "Tanaman",
        back_populates="jenis_tanaman",
        lazy=True
    )
