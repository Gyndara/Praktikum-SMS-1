#penjumlahan angka 1 sampai 10
#I.S.: diberikan harga pencacah (i) sama dengan 10
#F.S.: menampilkan hasil penjumlahan 1+2+3+...+10

#badan program
print('<<< penjumlahan satu sampai 10 >>>')
print('----------------------------------')
print('<<< pengulangan for postif >>>')
print('')
print('Hasil = ', end='')
Hasil = 0
for i in range(1, 11):
    print(i, end='')
    if (i < 10):
        print('+', end='')
    Hasil = Hasil + i
print(f'\n      = {Hasil}', end='')

print('')

print('<<< penjumlahan satu sampai 10 >>>')
print('----------------------------------')
print('<<< pengulangan for negatif >>>')
print('')
print('Hasil = ', end='')
Hasil = 0
for i in range(10, 0, -1):
    print(i, end='')
    if (i > 1):
        print('+', end='')
    Hasil = Hasil + i
print(f'\n      = {Hasil}', end='')

print('')

print('<<< penjumlahan satu sampai 10 >>>')
print('----------------------------------')
print('<<< pengulangan while cacah naik >>>')
print('')
print('Hasil = ', end='')
Hasil = 0
i = 1
while (i <= 10):
    print(i, end='')
    if (i < 10):
        print('+', end='')
    Hasil = Hasil + i
    i = i + 1
print(f'\n      = {Hasil}', end='')

print('')

print('<<< penjumlahan satu sampai 10 >>>')
print('----------------------------------')
print('<<< pengulangan while cacah naik >>>')
print('')
print('Hasil = ', end='')
Hasil = 0
i = 10
while (i >= 1):
    print(i, end='')
    if (i > 1):
        print('+', end='')
    Hasil = Hasil + i
    i = i - 1
print(f'\n      = {Hasil}', end='')
