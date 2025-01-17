#Program toko penjualan
#I.S.: Pengguna memasukan kode produk, jumlah produk, dan diskon jika produk lebih dari 10
#F.S.: Menampilkan data produk, jumlah produk, harga satuan, harga total, total bayar, uang pembayaran, uang kembalian dan diskon
import os
#badan program
#memasukan kode produk yang dibeli

print('_______________________________________________')
print('|________________TOKO PENJUALAN_______________|')
print('|__Kode Produk__|_Nama Produk_|_Harga Satuan__|')
print('|---------------|-------------|---------------|')
print('| PK01          | Pakaian     | Rp.75,000     |')
print('|---------------|-------------|---------------|')
print('| TS02          | Tas         | Rp.75,000     |')
print('|---------------|-------------|---------------|')
print('| SP03          | Sepatu      | Rp.75,000     |')
print('|---------------|-------------|---------------|')
print('| AK04          | Aksesoris   | Rp.75,000     |')
print('|---------------|-------------|---------------|')
print('|_____________________________________________|')

KodeProduk = str(input('Masukan Kode Produk : ')).upper()
if(KodeProduk != 'PK01') and (KodeProduk != 'TS02') and (KodeProduk != 'SP03') and (KodeProduk != 'AK04'):
    print('Produk tidak tersedia pada toko')
else:
    print(f'Produk {KodeProduk} tersedia pada toko')
    
    #memasukan jumlah produk yang dibeli
    Jumlah = int(input('Masukan Jumlah Produk : '))
    Diskon = 0
    StatusDiskon = 'T'

    #menghitung apakah jumlah produk yang dibeli lebih >= 10
    if(Jumlah >= 10):
        StatusDiskon = input('Status Diskon [Y/T] : ').upper()
    
    #memasukan besaran diskon 
    if(StatusDiskon == 'Y'):
        Diskon = float(input('Besaran Diskon : '))
        StatusDiskon = 'Y'
    os.system('pause')
    os.system('cls')
    
    if(KodeProduk =='PK01'):
        NamaBarang = 'Pakaian'
        HargaSatuan = 75000
    else:
        if(KodeProduk == 'TS02'):
            NamaBarang = 'Tas'
            HargaSatuan = 65000
        else:
            if(KodeProduk == 'SP03'):
                NamaBarang = 'Sepatu'
                HargaSatuan = 157000
            else:
                if(KodeProduk == 'AK04'):
                    NamaBarang = 'Aksesoris'
                    HargaSatuan = 45000

    #menghitung total harga
    HargaTotal = Jumlah * HargaSatuan
    BesaranDiskon = (Diskon/100) * HargaTotal
    TotalBayar = HargaTotal - BesaranDiskon
    print('Jumlah Produk       : ', Jumlah)
    print(f'Harga Satuan        : Rp.{HargaSatuan:,.0f}')
    print(f'Total Bayar         : Rp.{TotalBayar:,.0f}')
    
    Bayar = float(input('Masukan Jumlah uang : '))

    if(Bayar <= TotalBayar):
        print('UANG ANDA KURANG')
    else:
        UangKembali = Bayar - TotalBayar
        os.system('pause')
        os.system('cls')

        #menampilkan data
        print('       <<<<<< TOKO BISMA >>>>>>')
        print('Kode produk      : ', KodeProduk)
        print('Nama Produk      : ', NamaBarang)
        print('Jumlah produk    : ', Jumlah)
        print('Status diskon    : ', StatusDiskon)
        print(f'Harga Satuan     : Rp.{HargaSatuan:,.0f}')
        print(f'Harga Total      : Rp.{HargaTotal:,.0f}')
        print(f'Diskon {Diskon:.0f}%       : Rp.{BesaranDiskon:,.0f}')
        print('________________________________________')
        print(f'Tota Bayar       : Rp.{TotalBayar:,.0f}')
        print(f'Uang Pembayaran  : Rp.{Bayar:,.0f}')
        print(f'Kembalian        : Rp.{UangKembali:,.0f}')


