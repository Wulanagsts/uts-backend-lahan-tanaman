
from app import create_app, db
import app.models

app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Tabel database berhasil dibuat!")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
