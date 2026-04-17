# materi.php (Versi Legacy/Kotor)
def tampil():
    # Koneksi db langsung di fungsi
    db = ["Matematika", "Fisika", "Biologi"]
    u = ["Andi", "Budi"]
    
    # Logic berantakan & penamaan variabel satu huruf
    for d in db:
        print("Materi: " + d) # cetak langsung
        s = 2 # status magic number
        if s == 2:
            print("Status: Selesai")

# Fungsi yang melakukan banyak hal (I/O + Logic)
def tambah2(n):
    if n != "":
        print("Menambahkan...")
        return True
    else:
        return False

tampil()
