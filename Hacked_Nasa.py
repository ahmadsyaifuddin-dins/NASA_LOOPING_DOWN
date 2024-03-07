#KREDIT AHMAD SYAIFUDDIN
#Looping ini ketika berjalan maka Processnya berjalan beruntun kebawah dan berakhir ke nilai yg di inputkan User

import random
import os
import time
os.system('cls')

# Daftar kode hack yang akan bernilai benar (Berhasil)
kodes_benar = ["1011Asai", 1125, 1150, "AsaiXSIGAD666999", 2024]

# Meminta pengguna memasukkan kode
kode_pengguna = input("Masukkan kode : ")

# Memeriksa apakah kode pengguna cocok dengan salah satu dari daftar kode benar
if kode_pengguna in kodes_benar or int(kode_pengguna) in kodes_benar:
    for i in range(1, 1050):  # angka statis untuk hitungan
        print("Process ...")
        time.sleep(0.01)
    print("NASA HACKED ! ")

else:
    for i in range(1, 1000):  # angka statis untuk hitungan
        print("Process ...")
        time.sleep(0.01)
    print("HACKING FAILED")