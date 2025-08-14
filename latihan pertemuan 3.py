# latihan 1 :  Apa perbedaan utama antara operator= dan ==? 
# Berikan contoh penggunaan keduanya.
print('latihan 1')
print('-----operator assignment tunggal:-----')
# fungsi : untuk memberikan nilai atau mengisi variable
# cara baca : "Masukkan nilai yang ada di kanan ke dalam variabel di kiri."
# sifat : kata perintah atau aksi
print('contoh operator assignment tunggal:')
x = 20
print(x)
print('-----operator perbandingan ganda:-----')
# Fungsi: Untuk membandingkan kesamaan membandingkan kesamaan dua nilai.
# Cara Baca: "Apakah nilai di kiri sama dengan sama dengan nilai di kanan?"
# Sifat: Sifat: Sebuah pertanyaan pertanyaan yang menghasilkan True atau False.
print('contoh operator perbandingan ganda:')
tahun_sekarang = 2025
print(tahun_sekarang == 2025) # hasil nya adalah true
print(tahun_sekarang == 2030) # hasil nya adalah false

print('----latihan 2-----')
#Latihan 2: Manakah dari nama-nama variabel berikut yang TIDAK VALIDTIDAK VALID di Python? 
#_namadepan = 12  # valid
#nilai_rata2 = 02 # valid
#2x = 02          # tidak valid karena tidak di awalin dengan angka
#namalengkap = 'ahamad syamdudin' # valid

print('---latihan 3---')
#Apa yang akan terjadi jika kamu menjalankan kode di bawah ini dan memasukkan angka 
angka_favorite = input(str("masukan angka favorit mu :"))
hasil = angka_favorite * 2
print(f"angka favorite mu {angka_favorite} adalah {hasil}") # hasil nya adalah b

print('\n----latihan 4-----')
# Buatlah sebuah program kecil yang melakukan hal berikut:
#1. Meminta pengguna memasukkan alas sebuah segitiga.
#2. Meminta pengguna memasukkan tinggi sebuah segitiga.
######input() 
alas = float(input('masukan angka alas segitiga :'))
tinggi_segitiga = float(input('masukan tinggi segitiga :'))
hasil = (0.5 * alas * tinggi_segitiga)
print(f"luas segitiga:",hasil)

