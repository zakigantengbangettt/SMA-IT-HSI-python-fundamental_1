
print('=======latihan 1 =======')

def judul(tema):
    data_bersih = tema.strip()
    daftar_kata = data_bersih.split()
    gabungan = "".join(daftar_kata)
    title = gabungan.title()
    return title
input_user = input("masukan nama ngaco sesuka kalian: ")
hasil = judul(input_user)
print("\nasli:",input_user)
print("standar:",hasil)

print('=======latihan 2 =======')
input_bocah = input("Masukan Gmail anda: ")
email = "@"in input_bocah
pengecekan = input_bocah.endswith('.com') or input_bocah.endswith('.co.id')
if email and pengecekan:
    print("email anda valid")
else:
    print("email anda tidak valid")

print('=======latihan 3 =======')
input_orang = input("masukan kata:")
input_cuy   = input("masukan kata yang mau sensor:")
sensor = input_orang.replace(input_cuy,"***")
print("hasil:",sensor)

print('=======latihan 4 =======')
kalimat = input("masukan nama, nanti di singkat: ")
kata_kata = kalimat.split()
pisah = [kata[0] for kata in kata_kata]
gabungan = "".join(pisah).upper()
print("singkatan:", gabungan)

print('=======latihan 5 =======')

# Input dari pengguna
judul = input("Masukkan judul artikel: ")

# 1. Ubah semua huruf menjadi huruf kecil
slug = judul.lower()

# 2. Ganti spasi dengan tanda hubung
slug = slug.replace(" ", "-")

# 3. Bonus: Hapus semua karakter selain huruf, angka, dan tanda hubung
slug = re.sub(r'[^a-z0-9\-]', '', slug)

# Tampilkan hasil slug
print("Slug:", slug)


