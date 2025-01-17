# progra pemilihan menu

import os

#badan program
print('Menu Pilihan')
print('------------')
print('1. kalkulator sederhana')
print('2. suku ke-n dari fibbponaci')
print('3. s = 2/3 - 5/7 + 12/21')
print('0. keluar')

Pilih = int(input('Masukan pilihan menu anda : '))
while (Pilih < 0) or (Pilih > 3):
    print('menu tidak ada')
    print('Menu Pilihan')
    print('------------')
    print('1. kalkulator sederhana')
    print('2. suku ke-n dari fibbponaci')
    print('3. s = 2/3 - 5/7 + 12/21')
    print('0. keluar')
    Pilih = int(input('Masukan pilihan menu anda : '))
    
while (Pilih != 0):
    os.system('cls')
    match (Pilih):
        case 1 :
            print('menu satu')
        case 2 :
            print('menu dua')
        case 3 :
            print('menu ketiga')
    os.system('pause')    

