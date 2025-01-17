print('<<< penjumlahan satu sampai 10 >>>')
print('----------------------------------')
print('<<< pengulangan while cacah naik >>>')
print('')
print('')
Hasil = 0
i = 1

batas = int(input('Masukan Bilangan : '))
while (i <= batas):
    print(i, end='')
    if (i < batas):
        print('+', end='')
    Hasil = Hasil + i
    i = i + 1
print(f'\n      = {Hasil}', end='')