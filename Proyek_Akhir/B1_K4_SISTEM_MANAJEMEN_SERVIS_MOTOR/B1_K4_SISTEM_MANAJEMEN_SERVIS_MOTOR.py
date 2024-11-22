# Import time, digunakan untuk jeda time.sleep()
import time

# Import function menu_admin dari modul menu_admin, digunakan untuk menampilkan menu admin
from menu_admin import menu_admin

# Import funtion menu_user dari modul menu_user, digunakan untuk menampilkan menu user
from menu_user import menu_user

# Import funciton clear, digunakan untuk membersihkan terminal
# Import function print_header, digunakan untuk menampilkan header ke terminal
# Import function read_data, digunakan untuk membaca file eksternal json
# Import function write_data, digunakan untuk menyimpan data eksternal json
# dari modul util 
from util import clear, print_header, read_data, write_data

# Import class Console dari library rich, digunakan untuk menampilkan tampilan yang menarik di terminal
from rich.console import Console

# Import class ChargingBar dari library progress, digunakan untuk menampilkan visualisasi progress
from progress.bar import ChargingBar

# Inisialisasi/membuat object dari class Console yang ditampung ke dalam variabel console
console = Console()

# function menu_login
def menu_login() :
  # Menampilkan menu login untuk autentikasi pengguna.
  
  # Proses:
  # 1. Meminta input username dan password dari pengguna.
  # 3. Mengecek data di file `./databases/user.json`:
  #   - Jika username dan password cocok:
  #      * Masuk ke menu admin (jika role "admin").
  #      * Masuk ke menu user (jika role "user").
  #   - Jika tidak cocok, menampilkan pesan kesalahan.
  
  # Membersihkan Terminal
  clear()
  
  # Menampilkan header
  print_header("LOGIN", 110)
  
  # input username dan password
  input_username = input("\n Masukkan username : ")
  input_password = input(" Masukkan password : ")
  
  print()
  
  # Inisialisasi progress bar
  bar = ChargingBar(" Process", max=5)
  
  # Loop untuk simulasi progress
  for i in range(5):
    # Simulasi proses
    time.sleep(0.1)
    # Pindahkan progress bar ke langkah berikutnya
    bar.next()  
    
  # Selesaikan progress bar
  bar.finish()
  
  is_wrong = True
  
  # Melakukan iterasi dan membaca data pengguna dari file JSON
  for data in read_data("./databases/user.json") :
    
    # Melakukan pengecekan apakah username dan password yang diinputkan user sesuai dengan data dari file 
    if data["username"] == input_username and data["password"] == input_password and data["role"] == "admin":
      console.print("\n BERHASIL LOGIN", style="bold green")
      time.sleep(1)
      
      # Masuk ke menu admin
      menu_admin()
      
      # Reassign variabel is_wrong dengan nilai boolean "False" karena username dan password sesuai
      is_wrong = False
      
      # Memberhentikan perulangan
      break
    
    # Melakukan pengecekan apakah username dan password yang diinputkan user sesuai dengan data dari file
    if data["username"] == input_username and data["password"] == input_password and data["role"] == "user":
      console.print("\n BERHASIL LOGIN", style="green")
      time.sleep(1)
      
      # Masuk ke menu user
      menu_user(data["name"])
      
      # Reassign variabel is_wrong dengan nilai boolean "False" karena username dan password sesuai
      is_wrong = False
      
      # Memberhentikan perulangan
      break
  
  # Kode di bawah ini akan dieksekusi apabila pengguna salah memasukkan username atau password
  if is_wrong:
    console.print(" Username atau password salah", style="red")
    input(" Enter.....")

def menu_register() :
  # Menampilkan menu registrasi untuk pendaftaran pengguna baru.
  
  # Proses:
  # 1. Meminta input nama, username, dan password dari pengguna.
  # 2. Mengecek apakah username sudah digunakan.
  #    - Jika belum, tambahkan data ke file `./databases/user.json`.
  #    - Jika sudah, tampilkan pesan kesalahan.
  
  while True :
    # Membersihkan Terminal
    clear()

    # Menampilkan header
    print_header("REGISTER", 110)
    # Input nama, username, password
    input_name_register = input("\n Masukkan nama Anda : ").strip()
    input_username_register = input(" Masukkan username : ").strip()
    input_password_register = input(" Masukkan password : ").strip()
    
    # Mengecek apakah input string kosong atau kurang dari 5 karakter
    if input_username_register == "" or input_password_register == "" or input_name_register == "":
      console.print("\n Username atau password tidak boleh kosong", style="red")
      input(" Enter.....")
    elif len(input_username_register) <= 5 or len(input_password_register) <= 5 :
      console.print("\n Username atau password harus lebih dari 5 karakter", style="red")
      input(" Enter.....")
    else :
      break
  # Membaca data pengguna dari file external JSON
  data_users = read_data("./databases/user.json")
  is_used = False
  # Mengecek apakah username yang diinputkan pengguna telah digunakan
  for data in data_users :
    if data["username"] == input_username_register :
      is_used = True
  if is_used == False :
    # Menambahkan data pengguna baru
    data_users.append(
    {
      "name" : input_name_register,
      "username" : input_username_register,
      "password" : input_password_register,
      "role" : "user"
    })
    # Menyimpan data ke file eksternal JSON
    write_data("./databases/user.json", data_users)
    print()
    print(" Register Berhasil!!!")
    input(" Enter.....")
  # Kode di bawah ini akan dieksekusi apabila username telah digunakan
  else :
    console.print("\n Username telah dipakai", style="yellow")
    console.print("\n Registrasi Gagal!!!", style="red")
    input(" Enter.....")
  

# Menu utama
while True :
  # Membersihkan Terminal
  clear()
  
  # Menampilkan header dan beberapa menu
  print_header("SERVIS MOTOR", 110)
  print("\n LOGIN    >> 1")
  print(" REGISTER >> 2")
  print(" EXIT     >> 3")
  print()
  
  # Input pengguna sesuai menu yang telah tersedia
  input_user = input(" Masukkan pilihan Anda : ")

  if input_user == "1" :
    
    # Masuk ke menu login
    menu_login()
    
  elif input_user == "2" :
    
    # Masuk ke menu register
    menu_register()
    
  # Keluar dari program
  elif input_user == "3" :
    print()
    console.print(" Anda telah keluar dari Program", style="red")
    break
  
  # Kode di bawah ini akan dieksekusi apabila input dari pengguna tidak sesuai dengan menu yang tersedia
  else :
    print()
    console.print("\n Mohon maaf, menu tidak tersedia!!!", style="red")
    input(" Enter......")
    clear()