# latihan ke 1
print('=====latihan 1======')
def buat_email(nama_pengguna,domain ='coding.com'):
    return f'{nama_pengguna.lower()}@{domain.lower()}'
print(buat_email('budi'))
print(buat_email("ani" ,"belajar.id"))

# latihan 2
print('======latihan 2======')
def kirim_paket(barang,tujuan, berat_kg, asuransi=False, express=False):
    print(f"kirim {barang} ke {tujuan} bandung dengan{berat_kg}kg",f"asuransi:{asuransi}",express,{express})
kirim_paket (barang='buku',tujuan="bandung",berat_kg=2,express=True)

# latihan 3
print('=====latihan 3=====')
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen if jumlah_elemen > 0 else 0
    return total, jumlah_elemen, rata_rata

# Memanggil fungsi dan unpack hasilnya
daftar = [10, 20, 30, 40, 50]
total, jumlah_elemen, rata_rata = analisis_daftar(daftar)

# Mencetak hasil
print("Jumlah total:", total)
print("Jumlah elemen:", jumlah_elemen)
print("Nilai rata-rata:", rata_rata)

def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen if jumlah_elemen > 0 else 0
    return total, jumlah_elemen, rata_rata

# Memanggil fungsi dan unpack hasilnya
daftar = [10, 20, 30, 40, 50]
total, jumlah_elemen, rata_rata = analisis_daftar(daftar)

# Mencetak hasil
print("Jumlah total:", total)
print("Jumlah elemen:", jumlah_elemen)
print("Nilai rata-rata:", rata_rata)

# Memeriksa docstring
help(analisis_daftar)

x = 1
while x <= 100:
    x += 1







    
    