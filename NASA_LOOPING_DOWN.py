#KREDIT AHMAD SYAIFUDDIN
#Looping ini ketika berjalan maka Processnya berjalan beruntun kebawah dan berakhir ke nilai yg di inputkan User

import random
import os
import time
os.system('cls')

# Daftar kode hack yang akan bernilai benar (Berhasil)
kodes_benar = [25, 50 , 100, 111 , 1000 , 1100 , 1110, 10110, 1114, 6666, 56999, 75000]

# Meminta pengguna memasukkan kode
kode_pengguna = int(input("Masukkan kode : "))
if kode_pengguna in kodes_benar:
  for i in range(1, kode_pengguna+1):
    print("Process ..." )
    time.sleep(0.01)
  print("NASA HACKED ! ")

else:
    for i in range(1, kode_pengguna + 1):
      print("Process ...")
    time.sleep(0.01)
    print("HACKING FAILED")
