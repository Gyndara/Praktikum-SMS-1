# Menghitung Luas Segitiga
# I.S.:pengguna memasukan alas dan tinggi setiga
# F.S.:menampilkan luas segitiga

#badan program
Alas = float(input('Alas segitiga: '))
Tinggi = float(input('Tinggi segitiga: '))
#perhitungan luas segitiga
LuasSegitiga = 0.5 * Alas * Tinggi
#menampilkan hasil perhitungan
print(f'Luas segitiga : {LuasSegitiga:.2f} cm2')