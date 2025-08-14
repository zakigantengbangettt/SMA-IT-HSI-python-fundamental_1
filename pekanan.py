print('=========================')
print("HASIL BELANJA DI INDOMARET")  # judul sturkk
print('=========================')

print('MASUKAN DATA BARANG SATU')
nama_barang=str(input("masukan nama barang:"))
harga_barang = float(input("harga satuan:"))
jumlah_barangi = int(input("jumalah barang"))
print('MASUKAN DATA BARANG DUA')                 # input ke user
nama_barang_1=str(input("masukan nama barang:"))
harga_barang_1 = float(input("harga satuan:"))
jumlah_barangi_1 = int(input("jumalah barang :"))
jumlah_diskon = 0.0

total_1 = harga_barang * jumlah_barangi           # total dari semua barang
total_2 = harga_barang_1 * jumlah_barangi_1
subtotal = total_1 + total_2                   

if subtotal > 200.000:
    jumlah_diskon =subtotal * 0.10
elif subtotal > 100.000:                    # hitung diskon
    jumlah_diskon = subtotal * 0.05

total_akhir = subtotal - jumlah_diskon
print('hitung total -_-')
print('====================')
print(f'STRUK PEMBLIAN ANDA :')
print('=====================')
print(f"1.{nama_barang} ({jumlah_barangi} x {harga_barang} = {total_1})")
print(f"1.{nama_barang_1} ({jumlah_barangi_1} x {harga_barang_1} = {total_2})")
print(f"Subtotal:    {subtotal}")
print(f"Diskon      {'10%' if subtotal > 200.00 else '5%' if subtotal > 100.000 else '0%' }:{jumlah_diskon} ")
print(f"Total yang harus bayar : {total_akhir}")
print('==========================')
print('TERIMAKASIH TELAH BELANJA DI INDOMARET')
print('==========================')




