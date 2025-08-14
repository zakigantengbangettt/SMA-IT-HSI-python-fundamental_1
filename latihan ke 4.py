# latihan ke 1
try:
  gaji = 1.5
  jam_kerja = 40
  jam_upah = float(input("masukan jam lembur anda:"))  
  jam_normal = float(input("masukan jam normal anda:"))
  if jam_normal <= 40:
     upah =(jam_normal * jam_kerja) + (jam_upah * 1.5)
     print("selamat anda mendapatkan:",upah)
  else:
     tidak_dapet_upah = jam_normal <= jam_upah
     print(f"maaf anda tidak mendapatkan gaji tidak dapet upah tambahan:{tidak_dapet_upah}")
except:
   print("harus berupa angka") # latihan 2


# latihan 3

try:

   score = float(input("masukan score nilai anda:"))
   if score <= 0.0 or score >= 1.0  :
      print('score harus di antara 0.0 dan 0.1')
   else:
      if score >= 0.9:
         grade = "A"
      elif score >= 0.8:
         grade = "B"
      elif score >= 0.7:
         grade = "C"
      elif score >= 0.6:
         grade = "E"
      else:
        grade = "f"
        print('grade anda adalah',grade)
except:
   print("pesan eror :masukan berupa angka.")
   

# latihan 4
tinggi_wajib_pengunjung = 150
usia_wajib = 12
didampingin_orangtua = True
input_user = int(input("masukan tinggi badan:"))
usia = int(input('masukan usia anda:'))
if tinggi_wajib_pengunjung >= 150 or (usia_wajib > 12 and didampingin_orangtua):
   print('boleh masuk')
else:
   print('tidak boleh masuk')
   

   
  






   

  



