data_mhs = [
    {"nama" :"ucup",
    "role" : "admin"
    },
    
    {"nama" :"micael",
    "role" : "users"
    }
]

print(data_mhs[0]['nama'])
print(data_mhs[1]['nama'])


# data_mhs = {
#     "nama" : "ucup",
#     "nim" : 1,
#     "matkul" : ["APD", "Kalkulus"]
# }

# for key in data_mhs :
#     print(key)
    
# for value in data_mhs.values() :
#     print(value)


# print(data_mhs)
# del data_mhs["nim"]

# cache = data_mhs.pop('nim')

# print(data_mhs, "dictionary")
# print(cache, "cache")

# data_mhs['id'] = cache

# print(len(data_mhs))

# for data in data_mhs :
#     print(data)

# for key_data, value_data in data_mhs.items() :
#     print(f"{key_data} : {value_data}")

# data_mhs["nama"] = 'michael'
# data_mhs["alamat"] = "Samarinda"
# data_mhs["alamat"] = "Tenggarong"

# data_mhs.update({"alamat" : "Samarinda"})
# data_mhs.update({"alamat" : "Tenggarong"})



# print(data_mhs.get('mapel', 'Gak Ada'))
# print(data_mhs['mapel'])

# print(data_mhs['nama'])
# print(data_mhs["nim"])

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)