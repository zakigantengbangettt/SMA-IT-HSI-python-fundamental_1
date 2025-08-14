def tema_awal ():
    print("===============================")
    print("SELAMAT DATANG DI WARUNG GAMING")
    print("===============================")

tema_awal()
print("------Masukan Nama barang------")
print("(ketik 'selesai' di nama barang untuk selesai)")
daftar_nama_barang =[]
daftar_harga_barang = []
daftar_jumlah_barang =[]

while True:
    nama_barang = str(input("Nama Barang:>"))
    if nama_barang.lower() == 'selesai':
        print(">selesai")
        break
    try:
        harga_barang = float(input("Harga Barang:>"))
        jumlah_barang = int(input("Jumlah Barang:>"))
        daftar_nama_barang.append(harga_barang)
        daftar_harga_barang.append(harga_barang)
        daftar_jumlah_barang.append(jumlah_barang)

    except ValueError:
        print("Barang yang anda masukin tidak vailed")
        continue

def hitung_subtotal (harga_barang,jumlah_barang):
    total = 0
    for i in range(len(harga_barang)):
        total += harga_barang * jumlah_barang
    return total

def hitung_diskon(subtotal):
    if subtotal > 200.000:
        jumlah_diskon = 10
    elif subtotal > 100.000:
        jumlah_diskon = 5
    else:
        jumlah_diskon = 0
        diskon =subtotal * jumlah_diskon /100
        return diskon , jumlah_diskon
print("Menghitung Total Belanja Anda.....")
def tema_tengah ():
    print("=======================")
    print("STRUK PEMBELIAN")
    print("=======================")
tema_tengah()
print("Detail Belanja:")
print(f"{nama_barang}= {harga_barang} x {jumlah_barang}")

   




