# Import os, digunakan untuk mengakses sistem
import os

# Import json
import json

# Import class Console dari library rich
from rich.console import Console

# Import class Text dari library rich
from rich.text import Text

# Import class Panel dari library rich
from rich.panel import Panel

# Import function tabulate dari library tabulate
from tabulate import tabulate

def clear() :
  
  # Membersihkan layar terminal atau console.

  # Fungsi ini akan menjalankan perintah sistem untuk membersihkan terminal
  # sesuai dengan sistem operasi (Windows atau Linux/Mac).
  
  return os.system("cls || clear")

def write_data(path, new_data) :
  
  # Menulis data ke dalam file JSON.

  # Fungsi ini akan menulis data baru ke dalam file JSON yang sudah ada di
  # path yang diberikan, menggantikan konten sebelumnya.
  # Args:
  #   path (str): Lokasi file JSON yang akan ditulis.
  #   new_data (dict): Data baru yang akan disimpan ke dalam file.
  
  with open(path, "w") as json_file :
    json.dump(new_data, json_file, indent=2)

def read_data(path) :
  
  # Membaca data dari file JSON.

  # Fungsi ini akan membuka dan membaca konten file JSON yang berada di 
  # path yang diberikan dan mengembalikan data dalam format Python (dict atau list).
  # Args:
  #   path (str): Lokasi file JSON yang akan dibaca.
  # Returns:
  #   dict di dalam list: Data yang dibaca dari file JSON.
  
  with open(path, "r") as file :
    return json.load(file)

def print_header(header, width_param) :
  
  # Mencetak header dalam format panel dengan teks yang dipusatkan.

  # Fungsi ini membuat tampilan header dengan ukuran yang dapat disesuaikan sesuai parameter.
  # Args:
  #   header (str): Teks header yang akan ditampilkan.
  #   width_param (int): Lebar panel untuk menampilkan teks header.
  
  # Inisialisasi/membuat object dari class Text yang ditampung ke dalam variabel text
  text = Text(header, justify="center")
  
  # Memberi desain pada text
  text.stylize("bold")
  
  # Inisialisasi/membuat object dari class Panel yang ditampung ke dalam variabel panel
  panel = Panel(text, width= width_param)
  
  # Inisialisasi/membuat object dari class Console yang ditampung ke dalam variabel console
  console = Console()
  
  # Menampilkan header ke terminal
  console.print(panel)
  
def print_data_motorcycles(data) :
  
  # Mmebuat dictionary untuk menampung data
  temp_data = {
    "IDservis": [],
    "name_of_motorcycle": [],
    "owner": [],
    "servis":[],
    "kilometer" : [],
    "sparepart" : [],
    "status": [],
    "keterangan": []
  }
  
  for motorcycle in data :
    temp_data["IDservis"].append(motorcycle["IDservis"])
    temp_data["name_of_motorcycle"].append(motorcycle["name_of_motorcycle"])
    temp_data["owner"].append(motorcycle["owner"])
    temp_data["servis"].append(motorcycle["servis"])
    temp_data["kilometer"].append(motorcycle["kilometer"])
    temp_data["sparepart"].append(motorcycle["sparepart"])
    temp_data["status"].append(motorcycle["status"])
    temp_data["keterangan"].append(motorcycle["keterangan"])

  # Menampilkan tabel
  print(tabulate(temp_data, headers="keys", tablefmt="fancy_grid"))

def print_motorcycles_admin() :
  data_motorcycles = read_data("./databases/motorcycle.json")
  temp_data = []
  for motorcycle in data_motorcycles :
    if motorcycle["display"] == "on" : 
      temp_data.append(motorcycle)
  print_data_motorcycles(temp_data)

def print_motorcycles_user(name) :
  temporary = []
  
  # Mengecek apakah nama dari pengguna sesuai dengan nama yang ada di data dan property display bernilai "on"
  for motorcycle in read_data("./databases/motorcycle.json") :
    if motorcycle["owner"].lower() == name.lower() and motorcycle["display"] == "on" : 
      temporary.append(motorcycle)
      
  # Menampilkan data
  print_data_motorcycles(temporary)

