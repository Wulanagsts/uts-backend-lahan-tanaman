
from app import db


class Tanaman(db.Model):
    __tablename__ = "tanaman"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)

    jenis_id = db.Column(
        db.Integer,
        db.ForeignKey("jenis_tanaman.id"),
        nullable=False
    )

    lahan_id = db.Column(
        db.Integer,
        db.ForeignKey("lahan.id"),
        nullable=False
    )

    tanggal = db.Column(db.Date, nullable=False)

    # Relasi ke jenis tanaman
    jenis_tanaman = db.relationship(
        "JenisTanaman",
        back_populates="tanamans"
    )

    # Relasi ke lahan
    lahan = db.relationship(
        "Lahan",
        back_populates="tanamans"
    )
