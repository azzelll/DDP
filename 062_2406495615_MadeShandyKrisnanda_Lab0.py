print(">>====================================<<")
print("||                                    ||")
print("||  Welcome to Dek Depe's Calculator  ||")
print("||                                    ||")
print(">>====================================<<")

Nama = input("Nama: ")
TanggalLahir = input("Tanggal lahir: ")
Jurusan = input("Jurusan: ")
KelompokMentoring = int(input("Kelompok mentoring: "))
Motto = input("Motto: ")
Alas = int(input("Masukan alas (cm): "))
Tinggi = int(input("Masukan tinggi (cm): "))

import math
Luas =  0.5 * Alas * Tinggi
Miring = math.sqrt((Alas**2)+(Tinggi**2))
Keliling = math.ceil(Alas + Tinggi + Miring)


print('Halo {} dari jurusan {}.'.format(Nama, Jurusan))
print('{} berasal dari kelompok mentoring {}.'.format(Nama, KelompokMentoring))
print('{} lahir pada {} dengan motto "{}"'.format(Nama, TanggalLahir, Motto))
print('Luas dari segitiga yang dimiliki {} adalah {}cm^2'.format(Nama, Luas))
print('Keliling dari segitiga yang dimiliki {} adalah {} cm dengan sisi miring sepanjang{}'.format(Nama, Keliling, Miring))

print(">>==========================================<<")
print("||                                          ||")
print("||  Thanks for using Dek Depe's Calculator  ||")
print("||                                          ||")
print(">>==========================================<<")