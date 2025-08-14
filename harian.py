
print("===========latihan 1 ===========")
s = "Belajar Python itu Menyenangkan"
karakter_pertama = s[0]
print(f"Karakter pertama: {karakter_pertama}")
karakter_terakhir = s[-1]
print(f"Karakter terakhir: {karakter_terakhir}")
spasi_pertama = s[7]
print(f"Karakter spasi pertama: '{spasi_pertama}'")

print("============latihan 2 ===========")
s = "Belajar Python itu Menyenangkan"
python_slice = s[8:14]
print(f"Substring 'Python': {python_slice}")
menyenangkan_slice = s[18:]
print(f"Substring 'Menyenangkan': {menyenangkan_slice}")
belajar_slice = s[:7]
print(f"Substring 'Belajar': {belajar_slice}")

print("============latihan 3 ===========")
# Meminta input dari pengguna
kata_input = input("Masukkan sebuah kata: ")

# Membalik kata menggunakan slicing
kata_terbalik = kata_input[::-1]

print(f"Kata yang dibalik: {kata_terbalik}")

# Mengecek apakah kata tersebut adalah palindrom
if kata_input.lower() == kata_terbalik.lower():
    print(f"'{kata_input}' adalah sebuah palindrom.")
else:
    print(f"'{kata_input}' bukan sebuah palindrom.")

print("============latihan 4 ===========")
kalimat_rahasia = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

kode_rahasia = kalimat_rahasia[::3]

print(f"Kalimat rahasia: {kalimat_rahasia}")
print(f"Kode rahasia: {kode_rahasia}")

print("============latihan 5 ===========")
nama_salah = "dUDI sANTOSO"

bagian_nama_pertama = nama_salah[0:4]
bagian_nama_kedua = nama_salah[5:]
nama_benar = "B" + bagian_nama_pertama[1:] + " S" + bagian_nama_kedua[1:]
print(f"Nama salah: {nama_salah}")
print(f"Nama benar: {nama_benar}")

