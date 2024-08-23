import math
print(">>====================================<<")
print("||                                    ||")
print("||  Welcome to Dek Depe's Calculator  ||")
print("||                                    ||")
print(">>====================================<<")
print("")


nama = input("Nama: ")
tanggal_lahir = input("Tanggal lahir: ")
jurusan = input("Jurusan: ")
kelompok_mentoring = int(input("Kelompok mentoring: "))
motto = input("Motto: ")
alas = int(input("Masukan alas (cm): "))
tinggi = int(input("Masukan tinggi (cm): "))
print("")

luas =  0.5 * alas * tinggi
miring = math.sqrt((math.pow(alas,2))+(math.pow(tinggi,2)))
keliling = math.ceil(alas + tinggi + miring)

print('Halo {} dari jurusan {}.'.format(nama, jurusan))
print('{} berasal dari kelompok mentoring {}.'.format(nama, kelompok_mentoring))
print('{} lahir pada {} dengan motto "{}"'.format(nama, tanggal_lahir, motto))
print('Luas dari segitiga yang dimiliki {} adalah {} cm^2'.format(nama, luas))
print('Keliling dari segitiga yang dimiliki {} adalah {} cm dengan sisi miring sepanjang {}'.format(nama, keliling, miring))

print("")
print(">>==========================================<<")
print("||                                          ||")
print("||  Thanks for using Dek Depe's Calculator  ||")
print("||                                          ||")
print(">>==========================================<<")
