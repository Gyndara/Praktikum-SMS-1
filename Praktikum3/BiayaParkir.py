#I.S.: Pengguna Memasukan Jenis kendaraan, Nomor Polisi, Jam Masuk, Menit Masuk, Jam Keluar, Menit Keluar
#F.S.: Menampilkan Lama Parkir dan Biaya parkir yang perlu dibayar

#Badan Program
#Memasukan Jenis kendaraan, Nomor polisi
print('<<<<<<<<< BIAYA PARKIR KENDARAAN >>>>>>>>>')
JenisKendaraan = input('Masukan Jenis Kendaraan : ')
NoPol          = input('Masukan Nomor Polisi    : ')
#Memasukan Jam Masuk Parkir
JamMasuk       = input('Masuk (Jam:Menit)       : ')
JamMasuk, MenitMasuk = JamMasuk.split(':')
JamMasuk   = int(JamMasuk)
MenitMasuk = int(MenitMasuk)

#Memasukan Jam Keluar Parkir
JamKeluar      = input('Keluar (Jam:Menit)      : ')
JamKeluar, MenitKeluar = JamKeluar.split(':')
JamKeluar   = int(JamKeluar)
MenitKeluar = int(MenitKeluar)

#Validasi apakah menit keluar lebih besar dari menit masuk
if (MenitKeluar < MenitMasuk):
    MenitKeluar = MenitKeluar + 60
    JamKeluar = JamKeluar - 1
Menit = MenitKeluar - MenitMasuk

#Validasi apakah jam keluar lebih besar dari jam masuk
if (JamKeluar < JamMasuk):
    JamKeluar = JamKeluar + 12
Jam = JamKeluar - JamMasuk

#menampilkan lama parkir
print (f'Lama Parkir             : {Jam} Jam {Menit} Menit')

if (Menit > 0):
    Jam = Jam + 1
print('                         ', Jam, 'Jam')

#menghitung biaya parkir yang perlu dibayar
JenisKendaraan = JenisKendaraan.upper()
if (JenisKendaraan == 'MOTOR'):
    BiayaParkir = 1500 + (Jam - 1) * 500
else:
    BiayaParkir = 3000 + (Jam - 1) * 1000
    
#menampilkan biaya parkir yang perlu dibayar
print ('Biaya Parkir            : Rp.', BiayaParkir )

                                        
                                    