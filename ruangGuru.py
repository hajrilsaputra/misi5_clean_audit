from dataclasses import dataclass

# Menggunakan Konstanta untuk menghindari Magic Numbers [cite: 5]
STATUS_SELESAI = 2

@dataclass
class Materi:
    judul: str
    status: int

class MateriService:
    """Kelas khusus menangani Logika Bisnis (Prinsip SRP) [cite: 5]"""
    def __init__(self):
        self.daftar_materi = [
            Materi("Matematika", STATUS_SELESAI),
            Materi("Fisika", STATUS_SELESAI),
            Materi("Biologi", STATUS_SELESAI)
        ]

    def dapatkan_semua_materi(self):
        return self.daftar_materi

class KonsolUI:
    """Kelas khusus menangani Tampilan/Output (Prinsip SRP) [cite: 5]"""
    def tampilkan_konten(self, daftar_materi):
        for materi in daftar_materi:
            print(f"Materi: {materi.judul}")
            if materi.status == STATUS_SELESAI:
                print("Status: Materi Telah Selesai")

# Inisialisasi dengan penamaan yang bermakna [cite: 5]
service = MateriService()
ui = KonsolUI()

materi_tersedia = service.dapatkan_semua_materi()
ui.tampilkan_konten(materi_tersedia)
