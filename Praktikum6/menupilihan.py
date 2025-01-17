#program menu pilihan
#I.S.: pengguna memasukan menu yang ini dituju
#F.S.: menampilkan menu pilihan yang dipilih oleh user
import os


def IsiPilihan(PilihMenu):
    print('menu pilihan')
    print('1. kalkulator')
    print('2. suku ke n deret fibbonaci')
    print('3. s = 2/3 - 5/7 + 16/21')
    print('0. keluar')
    PilihMenu = int(input('pilihan anda : '))
    
    while (PilihMenu < 0) or (PilihMenu > 3):
        print('Menu tidak ada, ulangi')
        os.system('pause')
        os.system('cls')
        print('menu pilihan')
        print('1. kalkulator')
        print('2. suku ke n deret fibbonaci')
        print('3. s = 2/3 - 5/7 + 16/21')
        print('0. keluar')
        PilihMenu = int(input('Masukkan pilihan menu : '))
        
    return PilihMenu

def MenuPilihan(PilihMenu):
    while (PilihMenu != 0):
        match (PilihMenu):
            case 1 : 
                print('kalkulator sederhana')
                Angka1 = int(input('masukkan angka kesatu : '))
                Angka2 = int(input('masukkan angka kedua : '))
                operator = input('operator (+,-,x,:) : ')
                # while (operator != '+') and (operator != '-') and (operator != 'x') and (operator != ':'):
                #     print('operator tidak tersedia')
                #     os.system('pause')
                #     os.system('cls')
                #     print('angka kesatu :', Angka1)
                #     print('angka kedua :', Angka2)
                #     operator = input('operator (+,-,x,:) : ')
                return Angka1, Angka2, operator
            case 2 :
                print('suku ke-n dari deret fibbonaci')
                N = int(input('masukkan banyak N : '))
            case 3 :
                print('menghitung S = 2/3 - 5/7 + 16/21')
                S = int(input('masukkan banyak S : '))
        os.system('pause')
        os.system('cls')
        
# def IsiKalkulator(Angka1, Angka2, operator):
    
def hitung(PilihMenu, Angka1, Angka2, operator):
    if (operator == '+'):
        Hasil = Angka1 + Angka2
    else:
        if (operator == '-'):
            Hasil = Angka1 - Angka2
        else:
            if (operator == 'x'):
                Hasil = Angka1 * Angka2
            else:
                Hasil = Angka1 / Angka2
    return Hasil

def TampilHasil(Angka1, Angka2, operator):
     print(f'{Angka1} {operator} {Angka2} =')
     print(f'                             = {hitung(Angka1, Angka2, operator)}')
     
def fibonacci(N):
    hasilFibo = 0
    for i in range(N, 0, -1):
        hasilFibo = hasilFibo + i
        print(i, end='')
        if (i > 1):
            print('+', end='')
    print('\n', end='')
    return hasilFibo

def TampilFibo(N):
    print(f'{N} = {fibonacci(N)}')
    
# def MenghitungS(S)
#     penyebut = 1
#     s = 0
#     for i in range()
        
#program utama
PilihMenu = 0
PilihMenu = IsiPilihan(PilihMenu)
Angka1 = hitung(PilihMenu, Angka1, Angka1, operator)
Angka2 = MenuPilihan(Pilih)
operator = MenuPilihan(Pilih)
N = 0

TampilHasil(Angka1, Angka2, operator)
TampilFibo(Pilih, N)