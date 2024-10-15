import os, time

database_admin = [
  {
    "name" : "Eko Kurniawan",
    "username" : "eko",
    "password" : "eko123",
    "role" : "admin"
  }
]

database_user = [
  {
    "name" : "Sandhika Galih",
    "username" : "dika",
    "password" : "dika123",
    "role" : "user"
  },
  {
    "name" : "Budi Nugraha",
    "username" : "budi",
    "password" : "budi123",
    "role" : "user"
  },
    {
    "name" : "Joko Morro",
    "username" : "joko",
    "password" : "joko123",
    "role" : "user"
  }
]

database_goods = [
  {
    "IDservis" : 1,
    "name" : "Poco x3 Pro",
    "owner" : "Sandhika Galih",
    "problem" : "Mati total",
    "status" : "process"
  },
  {
    "IDservis" : 2,
    "name" : "Poco x4 Pro ",
    "owner" : "Joko Morro",
    "problem" : "Ganti LCD",
    "status" : "process"
  },
  {
    "IDservis" : 3,
    "name" : "Xiaomi redmi note 10",
    "owner" : "Budi Nugraha",
    "problem" : "Ganti baterai",
    "status" : "process"
  }
]

os.system("cls || clear")

def print_header(header, count) :
  print("=" *count)
  print(f"{header}".center(count))
  print("=" *count)

def print_handphone() :
  print("ID Servis".ljust(15, " ") + "| Nama Handphone".ljust(30, " ") + "| Pemilik".ljust(20, " ") + 
        "| Keluhan".ljust(25, " ") + "| Status barang".ljust(10, " "))
  print("_" * 105)
  for handphone in database_goods :
    print(f"{handphone["IDservis"]}".ljust(15, " ") + f"| {handphone["name"]}".ljust(30, " ") + f"| {handphone["owner"]}".ljust(20, " ") 
          + f"| {handphone["problem"]}".ljust(25, " ") + f"| {handphone["status"]}".ljust(10, " "))

def print_handphone_user(name) :
  print("ID Servis".ljust(15, " ") + "| Nama Handphone".ljust(30, " ") + "| Pemilik".ljust(20, " ") + 
        "| Keluhan".ljust(25, " ") + "| Status barang".ljust(10, " "))
  for handphone in database_goods :
    if handphone["owner"].lower() == name.lower() :
      print(f"{handphone["IDservis"]}".ljust(15, " ") + f"| {handphone["name"]}".ljust(30, " ") + f"| {handphone["owner"]}".ljust(20, " ") 
          + f"| {handphone["problem"]}".ljust(25, " ") + f"| {handphone["status"]}".ljust(10, " "))

def menu_admin() :
  while True :
    os.system("cls || clear")
    print_header("MENU ADMIN", 105)
    print()
    print_handphone()
    print()
    print("UPDATE STATUS SERVICE HANDPHONE >> 1")
    print("DELETE DATA HANDPHONE           >> 2")
    print("EXIT                            >> 3")
    print()
    input_user = input("Masukkan pilihan Anda : ")
    if input_user == "1" :
      try :
        print()
        print("MENU UPDATE STATUS")
        input_user_ID = int(input("Masukkan ID Service : "))
        for item in database_goods :
          if item["IDservis"] == input_user_ID :
            input_user_update = input("Update status (process, finish, sudah di ambil) : ")
            item["status"] = input_user_update
            print_handphone()
            input("Enter.....")
            break
        print("ID Servis tidak ditemukan")
      except :
        print("Harap masukkan angka")
        input("Enter....")
    elif input_user == "2" :
      try :
        print()
        print("MENU DELETE DATA")
        input_user_ID = int(input("Masukkan ID Service : "))
        for index, item in enumerate(database_goods) :
          if item["IDservis"] == input_user_ID :
            del database_goods[index]
            print_handphone()
            input("Enter.....")
            break
        print("ID Servis tidak ditemukan")
      except :
        print("Harap masukkan angka")
        input("Enter....")
    elif input_user == "3" :
      print("LOG OUT AS ADMIN!!!") 
      break
    else :
      print()
      print("Mohon maaf, menu tidak tersedia!!!")
      input("Enter......")
      os.system("cls || clear")

def menu_user(name) :
  while True :
    os.system("cls || clear")
    print_header("MENU USER", 105)
    print()
    print_handphone_user(name)
    print()
    print("SERVICE HANDPHONE       >> 1")
    print("EXIT                    >> 2")
    print()
    input_user = input("Masukkan pilihan Anda : ")
    if input_user == "1" :
      print()
      print("MENU SERVICE HANDPHONE")
      print()
      input_handphone = input("Masukkan jenis handphone Anda : ")
      input_pemilik = input("Masukkan nama Anda : ")
      input_keluhan = input("Masukkan keluhan Anda : ")
      index = 0
      for handphone in database_goods :
        index = handphone["IDservis"] + 1
      database_goods.append(
        {
          "IDservis" : index,
          "name" : input_handphone,
          "owner" : input_pemilik,
          "problem" : input_keluhan,
          "status" : "process"
        }
      )
    elif input_user == "2" :
      print("LOG OUT AS USER!!!") 
      break
    else :
      print()
      print("Mohon maaf, menu tidak tersedia!!!")
      input("Enter......")
      os.system("cls || clear")

while True :
  os.system("cls || clear")
  print_header("SERVIS HANDPHONE", 70)
  print("LOGIN    >> 1")
  print("REGISTER >> 2")
  print("EXIT     >> 3")
  print()
  input_user = input("Masukkan pilihan Anda : ")

  if input_user == "1" :
    os.system("cls || clear")
    print_header("LOGIN", 50)
    
    input_username = input("Masukkan username : ")
    input_password = input("Masukkan password : ")
    count_admin = 0
    count_user = 0
    for admin in database_admin :
      count_admin = count_admin + 1
      if admin["username"] == input_username and admin["password"] == input_password and admin["role"] == "admin":
        print(".....")
        time.sleep(2)
        print()
        print("BERHASIL LOGIN")
        time.sleep(2)
        menu_admin()
        count_admin = 0
        break
    for user in database_user :
      count_user = count_user + 1
      if user["username"] == input_username and user["password"] == input_password and user["role"] == "user":
        print(".....")
        time.sleep(2)
        print()
        print("BERHASIL LOGIN")
        time.sleep(2)
        menu_user(user["name"])
        count_user = 0
        break
    if count_user > 0 and count_admin != 0:
      print("Username atau password salah")
    elif count_admin > 0 and count_user != 0:
      print("Username atau password salah")
    input("Enter.....")
  elif input_user == "2" :
    os.system("cls || clear")
    print_header("REGISTER", 50)
    
    input_name_register = input("Masukkan nama Anda : ")
    input_username_register = input("Masukkan username : ")
    input_password_register = input("Masukkan password : ")
    # [input_name_register, input_username_register, input_password_register, "user"]
    database_user.append(
      {
        "name" : input_name_register,
        "username" : input_username_register,
        "password" : input_password_register,
        "role" : "user"
      }
    )
    print()
    print("Register Berhasil!!!")
    input("Enter.....")
  elif input_user == "3" :
    print()
    print("Anda telah keluar dari Program")
    break
  else :
    print()
    print("Mohon maaf, menu tidak tersedia!!!")
    input("Enter......")
    os.system("cls || clear")