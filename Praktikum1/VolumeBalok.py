# Menghitung Volume Balok
# I.S.: pengguna memasukan panjang, lebar dan tinggi balok
# F.S.: menampilkan volume balok

#badan program
print('<< Volume Balok >>')
Panjang  = float(input('Masukan panjang (inci):'))
Lebar    = float(input('Masukan lebar   (inci):'))  
Tinggi   = float(input('Masukan tinggi  (inci):'))
Konversi = 2.54
#perhitungan konversi inci ke cm3
KonversiPanjang = Panjang * Konversi
KonversiLebar   = Lebar   * Konversi
KonversiTinggi  = Tinggi  * Konversi
#perhitungan volume balok
VolumeBalok = KonversiPanjang * KonversiLebar * KonversiTinggi
print(f'Volume Balok : {VolumeBalok:.2f} cm3')