#I.S.: Pengguna memasukan bulan dan tahun penggajian, beserta tiga data karyawan yang tediri dariNIK, Nama, Gaji pokok
#F.S.: Menampilkan data gaji karyawan dan total gaji yang harus dibayar perusahaan

# import os
#badan program 
#memasukan bulan dan tanggal penggajian
Bulan = input('Bulan (Nama Bulan) : ')
Tahun = input('Tahun (yyy)        : ')

#memasukan data karyawan kesatu
print('----------------DATA KARYAWAN KESATU-----------------')
Nama1 = input('Masukan Nama       :')
NIK1  = input('Masukan NIK        :')
GajiPokok1 = float(input('Masukan Gaji Pokok :'))
#menghitungan PPN, Tunjangan dan gaji bersih
PPN1 = 0.1 * GajiPokok1
Tunjangan1 = 0.2 * GajiPokok1
GajiBersih1 = GajiPokok1 + Tunjangan1 - PPN1
# os.system('cls')
print('Nama                        :', Nama1)
print('NIK                         :', NIK1)
print(f'Gaji Pokok                  : Rp. {GajiPokok1:>13,.1f}')
print(f'Pajak 10%                   : Rp.{PPN1:>13,.1f}')
print(f'Tunjangn 20%                : Rp.{Tunjangan1:>13,.1f}')
print(f'Gaji Bersih                 : Rp.{GajiBersih1:>13,.1f}')
# os.system('pause')

#memasukan data karyawan kedua
print('----------------DATA KARYAWAN KEDUA-----------------')
Nama2 = input('Masukan Nama       :')
NIK2  = input('Masukan NIK        :')
GajiPokok2 = float(input('Masukan Gaji Pokok :'))
#menghitungan PPN, Tunjangan dan gaji bersih
PPN2 = 0.1 * GajiPokok2
Tunjangan2 = 0.2 * GajiPokok2
GajiBersih2 = GajiPokok2 + Tunjangan2 - PPN2
#menampilkan data karyawan
# os.system('cls')
print('Nama                        :', Nama2)
print('NIK                         :', NIK2)
print(f'Gaji Pokok                  : Rp.{GajiPokok2:>13,.1f}')
print(f'Pajak 10%                   : Rp.{PPN2:>13,.1f}')
print(f'Tunjangn 20%                : Rp.{Tunjangan2:>13,.1f}')
print(f'Gaji Bersih                 : Rp.{GajiBersih2:>13,.1f}')
# os.system('pause')

#memasukan data karyawan ketiga
print('----------------DATA KARYAWAN KETIGA-----------------')
Nama3 = input('Masukan Nama       :')
NIK3  = input('Masukan NIK        :')
GajiPokok3 = float(input('Masukan Gaji Pokok :'))
#menghitungan PPN, Tunjangan dan gaji bersih
PPN3 = 0.1 * GajiPokok3
Tunjangan3 = 0.2 * GajiPokok3
GajiBersih3 = GajiPokok3 + Tunjangan3
# os.system('cls')
print('Nama                        :', Nama3)
print('NIK                         :', NIK3)
print(f'Gaji Pokok                  : Rp.{GajiPokok3:>13,.1f}')
print(f'Pajak 10%                   : Rp.{PPN3:>13,.1f}')
print(f'Tunjangn 20%                : Rp.{Tunjangan3:>13,.1f}')
print(f'Gaji Bersih                 : Rp.{GajiBersih3:>13,.1f}')
# os.system('pause')

TotalGaji = GajiBersih1 + GajiBersih2 + GajiBersih3

print('')
print('                                     LAPORAN PENGGAJIAN')
print('                                     ------------------')

print(f'Bulan/Tahun:  {Bulan:.8}/{Tahun}')
print('________________________________________________________________________________________________________')
print('|_____________________________________Penggajian Karyawan______________________________________________|')
print('|------------------------------------------------------------------------------------------------------|')
print('|      NIK     |    Nama Karyawan    |   Gaji Pokok      |     Pajak    |   Tunjangan  |  Gaji Bersih  |')
print('|--------------|---------------------|-------------------|--------------|--------------|---------------|')
print(f'|  {NIK1:8}    | {Nama1:20}|Rp.{GajiPokok1:>13,.0f}   |Rp.{PPN1:>11,.1f}|Rp.{Tunjangan1:>11,.1f}|Rp.{GajiBersih1:>11,.1f} |')
print('|--------------|---------------------|-------------------|--------------|--------------|---------------|')
print(f'|  {NIK2:8}    | {Nama2:20}|Rp.{GajiPokok2:>13,.0f}   |Rp.{PPN2:>11,.1f}|Rp.{Tunjangan2:>11,.1f}|Rp.{GajiBersih2:>11,.1f} |')
print('|--------------|---------------------|-------------------|--------------|--------------|---------------|')
print(f'|  {NIK3:8}    | {Nama3:20}|Rp.{GajiPokok3:>13,.0f}   |Rp.{PPN3:>11,.1f}|Rp.{Tunjangan3:>11,.1f}|Rp.{GajiBersih3:>11,.1f} |')
print('|------------------------------------------------------------------------------------------------------|')
print('|______________________________________________________________________________________________________|')
print('')
print(f'Total Gaji : Rp.{TotalGaji:,.1f}')