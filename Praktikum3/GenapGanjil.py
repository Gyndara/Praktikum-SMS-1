#program menentukan bilangan ganjil atau genap
#I.S.: pengguna memasukan bilangan
#F.S.: menampilkan apakah bilangan yang dimasukkan genap atau ganjil

#badan program
#memasukan sebuah bilangan
print(' <<<<<< GENAP GANJIL >>>>>>')
Bilangan = int(input('Masukan Bilangan : '))
Keterangan = 'Bilangan Ganjil'
#menentukan bilangan genap atau ganjil
if  (Bilangan % 2 == 0):
    Keterangan = 'Bilangan Genap'
#menampilkan isi keterangan
print('Bilangan        :', Bilangan, Keterangan)