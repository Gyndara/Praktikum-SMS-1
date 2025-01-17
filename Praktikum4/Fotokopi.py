#Program pembayara fotokopi
#I.S.: pengguna memasukan tanggal, status konsumen (langganan), jumlah
#F.S.: menampilkan harga perlembar dan total harga yang harus dibayar 

import os
#badan program
#memasukan tanggal dan status langganan
Tanggal = str(input('Masukan Tanggal [dd/mm/yyyy] : '))
Langganan = input('Langganan [Y/T] : ').upper()
#validasi apakah seorang langganan atau bukan
if(Langganan != 'Y') and (Langganan != 'T'):
    print('Status langganan hanya bisa disi Y atau T')
else:
    print('Anda sebagai langganan : ', Langganan)

#memasukan jumlah lembar fotokopi
Jumlah = int(input('Masukan jumlah : '))

os.system('pause')
os.system('cls')

#menghitung total biaya fotkopi jika sebagai langganan dan bukan langganan
if(Langganan == 'Y'):
    HargaSatuan = 200
else:
    if(Jumlah < 100):
        HargaSatuan = 300
    else:
        HargaSatuan = 250
TotalBayar = Jumlah * HargaSatuan

print('  <<<< FOTO KOPI MAJU MUNDUR >>>>')
print('Tanggal                : ', Tanggal)
print('Status langganan [Y/T] : ', Langganan)
print('Jumlah lembar fotokopi : ', Jumlah)
print('Harga Satuan           : ', HargaSatuan)
print('______________________________________')
print('Total Harga            : ', TotalBayar)