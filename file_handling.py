panggil_file = "data-tes.txt"
mode = "r"
detail = open(panggil_file,mode)
baris = print(detail.readlines())
print(baris)
urut = 0
for b in baris:
    urut += 1
    print("baris",urut,"isi perbaris",b)

