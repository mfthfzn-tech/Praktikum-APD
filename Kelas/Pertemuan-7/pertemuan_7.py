# def hasil(nama) :
#   print("Hello World! " + nama)

# hasil("Adi")
# hasil("Adri")
# hasil("Dimas")

# def luas_persegi_panjang(panjang, lebar = 5) :
#   luas = panjang * lebar
#   # print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
#   return luas

# luas_persegi = luas_persegi_panjang(10, 5)
# print(luas_persegi)

# # variabel global
# nama = "Dimas"

# def say_hello() :
#   # variabel lokal
#   nama = "Daffa"
#   print(nama, "dalam fungsi")
  
#   def hitung() :
#     print("hitung")

# print(nama, "luar fungsi")
  
# import os
# data_mahasiswa =["Ifnu","Adi","ucup","michael"]

# def clear_screen():
#     os.system('cls || clear')

# clear_screen()

# def tampilkan_mahasiswa():
#     for i in range(len(data_mahasiswa)):
#         print(f"data ke {i+1}")
#         print(f"Nama : {data_mahasiswa[i]}")
#         print("="*10)

# def tambah_data():
#     print("MENU TAMBAH DATA")
#     print("=" * 10)
#     inputUser = input("Data yang mau ditambahkan : ")
#     data_mahasiswa.append(inputUser)
#     print(f"{inputUser} telah ditambahkan")

# def ubah_data():
#     index= int(input("masukkan index yang mau diedit : "))
#     data_baru =input("masukkan nama anda :")
#     data_mahasiswa[index-1]=data_baru
#     print("data berhasil diubah")

# def hapus_data():
#     index_user = int(input("masukkan index yang ingin dihapus: "))
#     del_user = data_mahasiswa.pop(index_user-1)
#     print(f"{del_user} telah dihapus")

# def menu():
#     print("""
#     Menu
# Lihat Data  >> 1
# Tambah Data >> 2
# Edit Data   >> 3
# Hapus Data  >> 4
# Keluar      >> 5
# """)

# while True:
#     menu()
#     pilih = input("Masukan Pilihan menu >> ")
#     clear_screen()
#     match(pilih):
#         case "1":
#             print("===Lihat Data===")
#             tampilkan_mahasiswa()
#             input("Enter.....")
#             clear_screen()
#         case "2":
#             tambah_data()
#             input("Enter....")
#             clear_screen()
#         case "3":
#             print("Menu ubah data")
#             tampilkan_mahasiswa()
#             ubah_data()
#             input("Enter.....")
#             clear_screen()
#         case "4":
#             print("Menu Hapus Data")
#             tampilkan_mahasiswa()
#             hapus_data()
#             input("Enter......")
#             clear_screen()
#         case "5":
#             print("Anda memilih menu 5")
#             exit()
#         case _:
#             print(f"Menu {pilih} tidak tersedia")
#             input("Enter.....")
#             clear_screen()