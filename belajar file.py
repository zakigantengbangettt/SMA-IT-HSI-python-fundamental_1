# belajar tentang menggunakan file
# membuat file baru
'''
print("=======latihan 1=======")
input_nama = input("masukan nama file(puisi.txt):")
try:
    with open(input_nama,'r') as file:
        for baris in file:
            print(baris.upper(),end='')
except FileNotFoundError:
    print(f"file tidak ada{input_nama}")

print("=======latihan 2 ======")
total_condifice = 0
jumlah_baris = 0
nama_file = "mbox-short.txt"
# buka file
try:
   with open('condifence.txt', 'r') as file:
     for baris in file:
        if baris.startswith('x-DSPAM-confidece: '):
            posisi_kolon = baris.find(':')
            angka_string = baris[posisi_kolon + 1 :].strip()
            angka_float = float(angka_string)
            total_condifice += angka_float
            jumlah_baris += 1
        if jumlah_baris > 0:
            rata_rata = total_condifice / jumlah_baris
            print(f'rata rata X-DSPAM-confidece:{rata_rata}')
        else:
            print("tidak ada data")
except FileNotFoundError:
    print(f"file tidak ada{nama_file}")
'''


print("======latihan 3======")
nama_file_1 = input("masukan nama file :")
if nama_file_1.lower() == "ha ha ha ha kocak":
    print("HA HA HA HA KOCAK- do you love me")
else:
    try:
        with open(nama_file_1,'r') as file:
          for baris in file:
            print(baris.upper(),end='')
    except FileNotFoundError:
        print(f"file eror :tidak di temukan {nama_file_1}")
   




