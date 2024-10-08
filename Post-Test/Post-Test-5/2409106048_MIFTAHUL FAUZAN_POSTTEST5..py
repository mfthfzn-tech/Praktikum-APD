import os, time

databases_person = [
  # [name, username, password, role]
  ["Eko Kurniawan", "eko", "eko123", "admin"],
  ["Sandhika Galih", "dika", "dika123", "user"],
  ["Joko Morro", "joko", "joko123", "user"],
  ["Budi Nugraha", "budi", "budi123", "user"]
]

databases_servis = [
  # [ID servis, nama handphone, pemilik, keluhan, status barang]
  # status barang = process, finish, sudah diambil
  [1, "Poco x3 Pro", "Sandhika Galih", "Mati total", "process"],
  [2, "Poco x4 Pro", "Joko Morro", "Ganti LCD", "process"],
  [3, "Xiaomi redmi note 10", "Budi Nugraha", "Ganti baterai", "process"]
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
  for handphone in databases_servis :
    print(f"{handphone[0]}".ljust(15, " ") + f"| {handphone[1]}".ljust(30, " ") + f"| {handphone[2]}".ljust(20, " ") 
          + f"| {handphone[3]}".ljust(25, " ") + f"| {handphone[4]}".ljust(10, " "))

def print_handphone_user(name) :
  for handphone in databases_servis :
    if handphone[2].lower() == name.lower() :
      print(f"{handphone[0]}".ljust(15, " ") + f"| {handphone[1]}".ljust(30, " ") + f"| {handphone[2]}".ljust(20, " ") 
              + f"| {handphone[3]}".ljust(25, " ") + f"| {handphone[4]}".ljust(10, " "))

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
        for item in databases_servis :
          if item[0] == input_user_ID :
            input_user_update = input("Update status (process, finish, sudah di ambil) : ")
            item[4] = input_user_update
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
        for index, item in enumerate(databases_servis) :
          if item[0] == input_user_ID :
            del databases_servis[index]
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
      for handphone in databases_servis :
        index = handphone[0] + 1
      
      databases_servis.append([index, input_handphone, input_pemilik, input_keluhan, "process"])
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
    count = 0
    for user in databases_person :
      count = count + 1
      if user[1] == input_username and user[2] == input_password and user[3] == "admin":
        print(".....")
        time.sleep(2)
        print()
        print("BERHASIL LOGIN")
        menu_admin()
        count = 0
        break
      elif user[1] == input_username and user[2] == input_password and user[3] == "user":
        print(".....")
        time.sleep(2)
        print()
        print("BERHASIL LOGIN")
        menu_user(user[0])
        count = 0
        break
    if count > 0 :
      print("Username atau password salah")
    input("Enter.....")
  elif input_user == "2" :
    os.system("cls || clear")
    print_header("REGISTER", 50)
    
    input_name_register = input("Masukkan nama Anda : ")
    input_username_register = input("Masukkan username : ")
    input_password_register = input("Masukkan password : ")
    
    databases_person.append([input_name_register, input_username_register, input_password_register, "user"])
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