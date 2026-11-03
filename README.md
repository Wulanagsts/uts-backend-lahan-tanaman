
# Sistem Manajemen Data Lahan dan Tanaman

## Deskripsi
Project ini merupakan aplikasi backend untuk Sistem Manajemen Data Lahan dan Tanaman. Aplikasi dibangun menggunakan Flask dan MySQL dengan menerapkan REST API serta Layered Architecture.

## Teknologi
- Python
- Flask
- Flask-SQLAlchemy
- MySQL
- PyMySQL
- Postman

## Struktur Folder
```text
app/
├── models/
├── repositories/
├── routes/
├── services/
├── utils/
├── __init__.py
└── config.py
run.py
requirements.txt
.gitignore
README.md
```

## Instalasi dan Menjalankan Project

1. Clone repository:
   ```bash
   git clone URL_REPOSITORY
   ```

2. Masuk ke folder project:
   ```bash
   cd "UTS banckend"
   ```

3. Buat virtual environment:
   ```bash
   python -m venv venv
   ```

4. Aktifkan virtual environment (Windows):
   ```powershell
   venv\Scripts\Activate.ps1
   ```

5. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```

6. Buat database MySQL dengan nama:
   ```sql
   CREATE DATABASE db_lahan_tanaman;
   ```

7. Jalankan aplikasi:
   ```bash
   python run.py
   ```

## Daftar Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | /api/v1/jenis-tanah | Mengambil jenis tanah |
| POST | /api/v1/jenis-tanah | Menambah jenis tanah |
| PUT | /api/v1/jenis-tanah/:id | Mengubah jenis tanah |
| DELETE | /api/v1/jenis-tanah/:id | Menghapus jenis tanah |
| GET | /api/v1/jenis-tanaman | Mengambil jenis tanaman |
| POST | /api/v1/jenis-tanaman | Menambah jenis tanaman |
| PUT | /api/v1/jenis-tanaman/:id | Mengubah jenis tanaman |
| DELETE | /api/v1/jenis-tanaman/:id | Menghapus jenis tanaman |
| GET | /api/v1/lahan | Mengambil data lahan |
| POST | /api/v1/lahan | Menambah data lahan |
| PUT | /api/v1/lahan/:id | Mengubah data lahan |
| DELETE | /api/v1/lahan/:id | Menghapus data lahan |
| GET | /api/v1/tanaman | Mengambil data tanaman |
| POST | /api/v1/tanaman | Menambah data tanaman |
| PUT | /api/v1/tanaman/:id | Mengubah data tanaman |
| DELETE | /api/v1/tanaman/:id | Menghapus data tanaman |
| POST | /api/v1/users/register | Registrasi pengguna |

## Database
Database menggunakan MySQL dengan lima tabel:
- users
- jenis_tanah
- jenis_tanaman
- lahan
- tanaman

Relasi database menerapkan hubungan One-to-Many.

## Pengujian
Pengujian REST API dilakukan menggunakan Postman, meliputi pengujian CRUD, validasi input, pencarian, filter, relasi data, dan transaksi rollback.
