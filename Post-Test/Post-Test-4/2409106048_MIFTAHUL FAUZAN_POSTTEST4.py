import time
import os 

sisaPercobaan = 3
while sisaPercobaan > 0 :
  # Masukkan username untuk login
  inputUsername = input("Masukkan Username : ")
  # Masukkan password untuk login
  inputPassword = input("Masukkan Password : ")
  # pengecekan username dan password
  if inputUsername == "fauzan" and inputPassword == "048" :
    while True :
      # membersihkan terminal
      os.system("cls")
      # print menu program
      print("=" * 65)
      print("Menu Program Menghitung Luas Permukaan/Volume Bangun Ruang".center(65))
      print("=" * 65)
      print("1. Luas Permukaan Kubus")
      print("2. Volume Balok")
      print("3. Volume Limas Persegi")
      print("4. Keluar Program")

      # mengambil input user
      inputUser = (input("Masukkan pilihan : "))

      # melakukan pengecekan input dari user
      if inputUser == "1" :
        print("")
        print("Menghitung luas permukaan kubus")
        sisiKubus = int(input("Masukkan panjang sisi kubus : "))
        luasPermukaanKubus = 6 * (sisiKubus * sisiKubus)
        print(f"Luas permukaan kubusnya adalah : {luasPermukaanKubus}")
      elif inputUser == "2" : 
        print("")
        print("Menghitung volume balok")
        panjangBalok = int(input("Masukkan panjang balok : "))
        lebarBalok = int(input("Masukkan lebar balok : "))
        tinggiBalok = int(input("Masukkan tinggi balok : "))
        volumeBalok = panjangBalok * lebarBalok * tinggiBalok
        print(f"Volume baloknya adalah : {volumeBalok}")
      elif inputUser == "3" : 
        print("")
        print("Menghitung volume limas persegi")
        panjangSisiAlas = int(input("Masukkan panjang sisi alas limas: "))
        tinggiLimas = int(input("Masukkan tinggi limas : "))
        luasAlasLimas = panjangSisiAlas * panjangSisiAlas
        volumeLimas = 1/3 * luasAlasLimas * tinggiLimas
        print(f"Volume limasnya adalah : {volumeLimas}")
      elif inputUser == "4" :
        print("Anda telah keluar dari program")
        break
      else :
        print("Pilihan yang Anda masukkan tidak tersedia")
      time.sleep(5)
    break
  else :
    if sisaPercobaan == 0 :
      print("PERCOBAAN HABIS ANDA GAGAL UNTUK LOGIN")
    else :
      sisaPercobaan -= 1
      print(f"Username atau Password yang Anda masukkan SALAH!!! \nPercobaan tersisa {sisaPercobaan}")