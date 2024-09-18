# Input nama Mahasiswa
nama = input("Masukkan nama Anda : ")

# Input umur Mahasiswa 
umur = int(input("Masukkan umur Anda :"))

# Input Apakah Mahasiswa Memiliki kepercayaan
kepercayaan = bool(input("Apakah Anda menganut sebuah kepercayaan(True(Iya)/False(Tidak))? CASE SENSITIVE : "))

# Input berat badan Mahasiswa
berat_badan = float(input("Masukkan berat badan Anda : "))

# Tambahkan semua variabel yang tipe data int atau float
total_numerik = umur + berat_badan

# Print data yang telah diinput
print("=" * 60)
print("Bio Data Anda".center(60))
print("=" * 60)
print("Nama".ljust(20, " ") + f": {nama}\n" + "Umur".ljust(20, " ") + f": {umur}\n" + "Kepercayaan".ljust(20, " ") + f": {kepercayaan}\n" 
    + "Berat badan".ljust(20, " ") + f": {berat_badan}\n" + "Total numerik".ljust(20, " ") + f": {total_numerik}")
print("=" * 60)



