# Menukar Dua Buah Angka Menggunakan Bantuan Variabel
# I.S.: pengguna memasukan angka kesatu dan angka kedua
# F.S.: menampilkan hasil dari pertukaran angka kesatu dengan angka kedua

#badan program
print('<< Menukar 2 Angka Dengan Batuan Variable >>')
Angka1 = int(input('Masukan angka kesatu:'))
Angka2 = int(input('Masukan angka kedua :'))
#menyimpan nilai angka kedua pada var I untuk disimpan sementara 
I = Angka2
#menukar value pada angka kedua dengan angka kesatu
Angka2 = Angka1
#mengambil value yang disimpan pada variabel sementara
Angka1 = I
#menampilkan hasil pertukaran
print('Angka kesatu:', Angka1)
print('Angka Kedua :', Angka2)