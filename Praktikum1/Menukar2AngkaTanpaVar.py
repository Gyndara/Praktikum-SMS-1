# Menukar Dua Buah Angka Tanpa Variabel Bantuam
# I.S.: pengguna memasukan angka kesatu dan angka kedua
# F.S.: menampilkan hasil dari pertukaran angka kesatu dengan angka kedua

#badan program
print ('<< Menukar 2 Angka Tanpa Bantuan Variabel >>')
Angka1 = int(input('Masukan angka kesatu:'))
Angka2 = int(input('Masukan angka kedua :'))
#melakukan pertukaran menggunakan operasi artimatika
Angka1 = Angka1 + Angka2
Angka2 = Angka1 - Angka2
Angka1 = Angka1 - Angka2
#menampilkan hasil pertukaran
print('Angka kesatu:', Angka1)
print('Angka Kedua :', Angka2)