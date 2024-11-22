# Import time
import time

# Import funciton clear, digunakan untuk membersihkan terminal
# Import function print_header, digunakan untuk menampilkan header ke terminal
# Import function print_motorcycles_user, digunakan untuk menampilkan data motor ke termianl dengan format tabel yang rapi
# Import function read_data, digunakan untuk membaca file eksternal json
# Import function write_data, digunakan untuk menyimpan data eksternal json
# dari modul util 
from util import clear, print_header, print_motorcycles_user, read_data, write_data

# Import class Console dari library rich
from rich.console import Console

# Import function tabulate dari library tabulate
from tabulate import tabulate

# Inisialisasi/membuat object dari class Console yang ditampung ke dalam variabel console
console = Console()

def service_motor(name) :
  # Mendaftarkan motor untuk diservis.
  # Proses:
  # 1. Meminta pengguna memasukkan jenis motor dan keluhan.
  # 2. Membaca ID servis terakhir dari file `id_service.json` dan increment nilainya.
  # 3. Menambahkan data baru ke file `motorcycle.json` dengan informasi:
    #  - ID servis.
    #  - Jenis motor.
    #  - Nama pemilik.
    #  - Keluhan.
    #  - Status awal servis.
    #  - Keterangan awal.
  # 4. Menyimpan data ID servis terbaru ke `id_service.json`.
  # Argumen:
      # name (str): Nama pengguna yang sedang login.
  
  # Membersihkan Terminal
  clear()
  
  print()
  
  # Menampilkan header
  print_header("MENU SERVICE MOTOR", 50)
  
  # Input Nama motor, keluhan/servis dan kilometer motor
  input_motorcycle = input("\n Masukkan jenis motor Anda : ")
  input_keluhan = input(" Masukkan keluhan/servis Anda : ")
  input_kilometer = input(" Masukkan kilometer motor Anda : ")
  
  # Membaca data ID dari file JSON
  data_id = read_data("./databases/id_service.json")
  
  # Membaca data motor dari file JSON
  data_motorcycles = read_data("./databases/motorcycle.json")
  
  # Menambahkan data motor baru
  data_motorcycles.append(
    {
      "IDservis" : data_id["IDService"],
      "name_of_motorcycle" : input_motorcycle,
      "owner" : name,
      "servis" : input_keluhan,
      "kilometer" : input_kilometer,
      "sparepart" : [],
      "status" : "...",
      "display" : "on",
      "keterangan" : "Mengecek ketersedian barang/waktu"
    }
  )
  
  # Mengubah data ID
  data_id = {
    "IDService" : data_id["IDService"] + 1
  }
  
  # Menyimpan data ke file eksternal JSON
  write_data("./databases/id_service.json", data_id)
  write_data("./databases/motorcycle.json", data_motorcycles)
  
  console.print("\n Sukses Menambahkan!", style="green")
  input(" Enter....")

def update_keluhan() :
  try :
    print()
    
    # Menampilkan header
    print_header("MENU UPDATE KELUHAN", 50)
    
    # Input ID service
    input_user_ID = int(input(" Masukkan ID Service : "))
    
    # Membaca data motor dari file JSON
    data_motorcycles = read_data("./databases/motorcycle.json")
    
    is_not_match = True
    
    # Mengecek apakah ID service yang diinputkan pengguna sesuai
    for item in data_motorcycles :
      if item["IDservis"] == input_user_ID and item["display"] == "on":
        
        # Input keluhan baru
        input_user_update_keluhan = input(" Update Keluhan : ")
        
        # Reassign value dengan keluhan yang baru
        item["servis"] = input_user_update_keluhan
        
        # Menyimpan data ke file eksternal JSON
        write_data("./databases/motorcycle.json", data_motorcycles)
        console.print("\n Sukses Mengupdate!", style="green")
        input(" Enter.....")
        
        # Reassign variabel is_wrong dengan nilai boolean "False" karena ID service sesuai
        is_not_match = False
        break
    
    # Kode di bawah ini akan dieksekusi apabila ID service tidak sesuai
    if is_not_match :
      console.print("\n ID Servis tidak ditemukan", style="red")
      input(" Enter....")
  # Kode di bawah ini akan dieksekusi apabila pengguna menginputkan karakter selain angka
  except :
    console.print("\n  Harap masukkan angka", style="red")
    input(" Enter....")

def histori_service(name) :
  # Menampilkan histori servis motor yang telah selesai.

  # Proses:
  # 1. Membaca data dari file `motorcycle.json`.
  # 2. Memfilter data berdasarkan:
  #    - Status `display` yang bernilai `False` (servis selesai).
  #    - Pemilik motor sesuai dengan nama pengguna.
  # 3. Menampilkan hasil dengan format tabel.
  # Args:
  #     name (str): Nama pengguna yang sedang login.
  
  # Membersihkan Terminal
  clear()
  
  # Menampilkan header
  print_header("HISTORI SERVICE", 110)
  print()
  
  
  data_after_filter = {
    "IDservis": [],
    "name_of_motorcycle": [],
    "owner": [],
    "servis":[],
    "kilometer" : [],
    "sparepart" : [],
    "status": [],
    "keterangan": []
  }
  # Filter data motor yang telah diservis
  for motorcycle in read_data("./databases/motorcycle.json") :
    
    # Mengecek apakah data tersebut memiliki properti display bernilai "False" dan memiliki 
    # properti owner sesuai dengan nama pengguna
    if motorcycle["display"] == "off" and motorcycle["owner"] == name:
      data_after_filter["IDservis"].append(motorcycle["IDservis"])
      data_after_filter["name_of_motorcycle"].append(motorcycle["name_of_motorcycle"])
      data_after_filter["owner"].append(motorcycle["owner"])
      data_after_filter["servis"].append(motorcycle["servis"])
      data_after_filter["kilometer"].append(motorcycle["kilometer"])
      data_after_filter["sparepart"].append(motorcycle["sparepart"])
      data_after_filter["status"].append(motorcycle["status"])
      data_after_filter["keterangan"].append(motorcycle["keterangan"])
  
  print(tabulate(data_after_filter, headers="keys", tablefmt="fancy_grid"))
  # Menampilkan histori service
  
  input(" Enter....")

def menu_user(name) :
  
  # Menampilkan menu utama untuk pengguna.

  # Proses:
  # 1. Menampilkan daftar opsi menu:
  #    - SERVICE MOTOR: Untuk mendaftarkan motor baru.
  #    - UPDATE KELUHAN: Untuk memperbarui keluhan.
  #    - HISTORI SERVIS: Untuk melihat riwayat servis selesai.
  #    - EXIT: Untuk keluar dari akun.
  # 2. Meminta pengguna memilih opsi.
  # 3. Menjalankan fungsi berdasarkan pilihan pengguna.
  # Args:
  #     name (str): Nama pengguna yang sedang login.
  
  while True :
    # Membersihkan Terminal
    clear()
    
    # Menampilkan header
    print_header("MENU USER", 110)
    print()
    
    # Menampilkan motor sesuai dengan kepemilikan pengguna
    print_motorcycles_user(name)
    
    # Menampilkan menu
    print("\n SERVICE MOTOR           >> 1")
    print(" UPDATE KELUHAN          >> 2")
    print(" HISTORI SERVIS          >> 3")
    print(" EXIT                    >> 4")
    
    # Input pilihan pengguna
    input_user = input("\n Masukkan pilihan Anda : ")
    if input_user == "1" :
      
      # Masuk ke menu service motor
      service_motor(name)
      
    elif input_user == "2" :
      
      # Masuk ke menu update keluhan
      update_keluhan()
      
    elif input_user == "3" :
      
      # Masuk ke menu histori service
      histori_service(name)
    
    # Keluar dari akun
    elif input_user == "4" :
      console.print(" LOG OUT...", style="yellow")
      time.sleep(2)
      break
    
    # Kode di bawah ini akan dieksekusi apabila input dari pengguna tidak sesuai dengan menu yang tersedia
    else :
      print()
      console.print("\n Mohon maaf, menu tidak tersedia!!!", style="red")
      input(" Enter......")
      clear()