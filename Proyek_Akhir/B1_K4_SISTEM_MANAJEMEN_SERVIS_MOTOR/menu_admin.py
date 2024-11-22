# Import time
import time

# Import funciton clear, digunakan untuk membersihkan terminal
# Import function print_header, digunakan untuk menampilkan header ke terminal
# Import function print_motorcycles_admin, digunakan untuk menampilkan data motor ke termianl dengan format tabel yang rapi
# Import function read_data, digunakan untuk membaca file eksternal json
# Import function write_data, digunakan untuk menyimpan data eksternal json
# Import function print_data_motorcycles, digunakan untuk menampilkan data motor ke termianl dengan format tabel yang rapi
# dari modul util 
from util import clear, print_header, print_motorcycles_admin, read_data, write_data, print_data_motorcycles

# Import class Console dari library rich
from rich.console import Console

# Import function tabulate dari library tabulate
from tabulate import tabulate

# Inisialisasi/membuat object dari class Console yang ditampung ke dalam variabel console
console = Console()

# Fungsi untuk menambahkan sparepart ke dalam data motor
def add_sparepart(data) :
  # Menampilkan header
  print_header("Menu Add Sparepart", 35)
  
  # Input sparepart
  input_user_add = input(" Masukkan Sparepart : ")
  
  # Sparepart ditambahkan ke dalam daftar sparepart motor
  data["sparepart"].append(input_user_add)
  
  console.print("\n Sukses Menambahkan!", style="green")
  input(" Enter....")

# Fungsi untuk memperbarui sparepart yang sudah ada
def update_sparepart(data) :
  try :
    
    # Menampilkan header
    print_header("Menu Update Sparepart", 35)
    print()
    
    # Menampilkan sparepart motor
    for index, item in enumerate(data["sparepart"]) :
      print(f"{index + 1}. {item}")
    print()
    
    # Input no sparepart dan sparepart yang baru
    input_user_update_no = int(input(" Masukkan No Sparepart : "))
    input_user_update = input(" Masukkan Sparepart : ")
    is_not_match = True
    
    # Mengecek apakah no sparepart sesuai
    for index, item in enumerate(data["sparepart"]) :
      if (input_user_update_no - 1) == index:
        
        # Mengupdate sparepart
        data["sparepart"][index] = input_user_update
        
        # Reassign variabel is_not_match dengan nilai boolean "False" karena no sparepart sesuai
        is_not_match = False
        break
    
    # Kode di bawah ini akan dieksekusi apabila no sparepart tidak sesuai
    if is_not_match :
      console.print("\n  ID Servis tidak ditemukan", style="red")
      input(" Enter....")
    
    console.print("\n Sukses Mengupdate!", style="green")
    input(" Enter....")
  # Kode di bawah ini akan dieksekusi apabila pengguna menginputkan karakter selain angka
  except :
    console.print("\n  Harap masukkan angka", style="red")
    input(" Enter....")

def delete_sparepart(data) :
  try :
    # Menampilkan header
    print_header("Menu Delete Sparepart", 35)
    print()
    
    # Menampilkan sparepart motor 
    for index, item in enumerate(data["sparepart"]) :
      print(f"{index + 1}. {item}")
    print()
    
    # Input no sparepart
    input_user_delete_no = int(input(" Masukkan No Sparepart : "))
    is_not_match = True
    
    # Mengecek apakah no sparepart sesuai
    for index, item in enumerate(data["sparepart"]) :
      if index == (input_user_delete_no - 1) :
        # Menghapus sparepart sesuai dengan no
        del data["sparepart"][index]
        
        # Reassign variabel is_not_match dengan nilai boolean "False" karena no sparepart sesuai
        is_not_match = False
        break
    
    # Kode di bawah ini akan dieksekusi apabila no sparepart tidak sesuai
    if is_not_match :
      console.print("\n  ID Servis tidak ditemukan", style="red")
      input(" Enter....")
    
    console.print("\n Sukses Menghapus!", style="green")
    input(" Enter....")
  # Kode di bawah ini akan dieksekusi apabila pengguna menginputkan karakter selain angka
  except :
    console.print("\n Harap masukkan angka", style="red")
    input(" Enter....")

def menu_sparepart(data) :
  
  # Menu untuk mengelola sparepart dalam data servis motor.

  # Proses:
  # 1. Menampilkan sparepart terkait ID servis yang dipilih.
  # 2. Menyediakan pilihan:
  #    - Menambah sparepart.
  #    - Memperbarui sparepart.
  #    - Menghapus sparepart.
  #    - Menyimpan perubahan dan keluar.
  # 3. Memperbarui data sparepart sesuai dengan input pengguna.
  # Args:
  #     data (dict): Data servis motor yang dipilih.
  
  while True :
    # Membersihkan Terminal
    clear()
    
    # Menampilkan header
    print_header("MENU SPAREPART", 50)
    print()
    
    # Menampilkan data motor sesuai dengan data yang dipilih
    print_data_motorcycles([data])
    print()
    
    # Menampilkan menu
    print("\n TAMBAH SPAREPART                     >> 1")
    print(" UPDATE SPAREPART                     >> 2")
    print(" DELETE SPAREPART                     >> 3")
    print(" SAVE AND EXIT FROM SPAREPART MENU    >> 4")

    # Input pengguna sesuai menu yang telah tersedia
    input_user = input(" Masukkan pilihan Anda : ")

    if input_user == "1" :
      
      # Masuk ke menu add sparepart
      add_sparepart(data)
    elif input_user == "2" :
      
      # Masuk ke menu update Sparepart
      update_sparepart(data)
      
    elif input_user == "3" :
      
      # Masuk ke menu delete sparepart
      delete_sparepart(data)
      
    # Menyimpan dan keluar dari menu sparepart
    elif input_user == "4" :
      console.print(" EXIT FROM Sparepart MENU", style="yellow")
      time.sleep(2)
      break
    
    # Kode di bawah ini akan dieksekusi apabila input dari pengguna tidak sesuai dengan menu yang tersedia
    else :
      print()
      console.print("\n Mohon maaf, menu tidak tersedia!!!", style="red")
      input(" Enter......")
      clear()

def update_status_service() :
  try :
    print()
    
    # Menampilkan header
    print_header("MENU UPDATE STATUS", 50)
    
    # Input ID service
    input_user_ID = int(input(" Masukkan ID Service : "))
    
    # Membaca data motor dari file JSON
    data_motorcycles = read_data("./databases/motorcycle.json")
    is_not_match = True
    
    # Mengecek apakah ID service yang diinputkan pengguna sesuai
    for item in data_motorcycles :
      if item["IDservis"] == input_user_ID and item["display"] == "on":
        # Input status dan keterangan baru
        input_admin_update_status = input(" Update status (diterima, ditolak, proses, finish, sudah di ambil) : ")
        input_admin_update_keterangan = input(" Update Keterangan : ")
        
        # Update status dan keterangan dengan status dan keterangan yang baru
        item["status"] = input_admin_update_status
        item["keterangan"] = input_admin_update_keterangan
        
        # Menyimpan data ke file eksternal JSON
        write_data("./databases/motorcycle.json", data_motorcycles)
        
        console.print("\n Sukses Mengupdate!", style="green")
        input(" Enter.....")
        
        # Reassign variabel is_not_match dengan nilai boolean "False" karena ID service sesuai
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

def delete_data_motor() :
  try :
    print()
    
    # Menampilkan header
    print_header("MENU DELETE DATA", 50)
    
    # Input ID service
    input_user_ID = int(input(" Masukkan ID Service : "))
    
    # Membaca data motor dari file JSON
    data_motorcycles = read_data("./databases/motorcycle.json")
    is_not_match = True
    
    # Mengecek apakah ID service yang diinputkan pengguna sesuai
    for index, item in enumerate(data_motorcycles) :
      if item["IDservis"] == input_user_ID and item["display"] == "on":
        
        # Mengubah nilai properti display dengan nilai "False"
        data_motorcycles[index]["display"] = "off"
        
        # Menyimpan data ke file eksternal JSON
        write_data("./databases/motorcycle.json", data_motorcycles)
        
        
        console.print("\n Sukses Menghapus!", style="green")
        input(" Enter.....")
        
        # Reassign variabel is_not_match dengan nilai boolean "False" karena ID service sesuai
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

def menu_sparepart_main() :
  try :
    print()
    
    # Menampilkan header
    print_header("MENU SPAREPART", 50)
    
    # Input ID service
    input_user_ID = int(input(" Masukkan ID Service : "))
    
    # Membaca data motor dari file JSON
    data_motorcycles = read_data("./databases/motorcycle.json")
    is_not_match = True
    
    # Mengecek apakah ID service yang diinputkan pengguna sesuai
    for item in data_motorcycles :
      if item["IDservis"] == input_user_ID and item["display"] == "on":
        
        # Masuk ke menu sparepart
        menu_sparepart(item)
        
        # Reassign variabel is_not_match dengan nilai boolean "False" karena ID service sesuai
        is_not_match = False
        break
    if is_not_match :
      console.print("\n ID Servis tidak ditemukan", style="red")
      input(" Enter....")
    write_data("./databases/motorcycle.json", data_motorcycles)
  # Kode di bawah ini akan dieksekusi apabila pengguna menginputkan karakter selain angka
  except :
    print(" Harap masukkan angka")
    input(" Enter....")

def menu_admin() :
  while True :
    # Membersihkan Terminal
    clear()
    
    # Menampilkan header
    print_header("MENU ADMIN", 110)
    print()
    
    # Menampilkan data motor
    print_motorcycles_admin()
    
    # Menampilkan menu
    print("\n UPDATE STATUS SERVICE MOTOR >> 1")
    print(" DELETE DATA MOTOR           >> 2")
    print(" MENU SPAREPART              >> 3")
    print(" EXIT                        >> 4")
    print()
    
    # Input pengguna sesuai menu yang telah tersedia
    input_user = input(" Masukkan pilihan Anda : ")
    if input_user == "1" :
      
      # Masuk ke menu update status service
      update_status_service()
      
    elif input_user == "2" :
      
      # Masuk ke menu delete data motor
      delete_data_motor()
      
    elif input_user == "3" :
      
      # Masuk ke menu sparepart
      menu_sparepart_main()
    
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