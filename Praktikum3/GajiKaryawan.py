NamaKaryawan = input('Masukan Nama Karyawan :')
LamaBekerja  = int(input('Lama Bekerja          :'))
UpahPerjam = 250000
GajiAwal = LamaBekerja * UpahPerjam
if (LamaBekerja > 40 ):
    TotalGaji = (LamaBekerja - 40) * UpahPerjam
    TotalGaji = GajiAwal + UpahPerjam
    GajiAwal = TotalGaji 

print('      <<<< TOTAL GAJI >>>>')
print('Nama Karyawan :', NamaKaryawan )
print('Lama Bekerja  :', LamaBekerja)
print('Total Gaji    :', GajiAwal)
    

