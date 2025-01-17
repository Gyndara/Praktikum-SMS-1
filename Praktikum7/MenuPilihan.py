#program menu pilihan
#I.S. : pengguna memilih salah satu nomor menu
#F.S. : menampilkan hasil sesuai nomor menu yang dipilih
import os

#subrutin menampilkan menu pilihan 
def MenuPilihan(Pilih):
    print('Menu Pilihan')
    print('1. A pangkat B')
    print('2. Barisan 1,3,3,6,18,24')
    Pilih = int(input('Masukkan menu pilihan : '))
    os.system('cls')
    while (Pilih < 0) or (Pilih > 2):
        print(f'Menu {Pilih} tidak tersedia, ulangi..')
        os.system('pause')
        os.system('cls')
        print('Menu Pilihan')
        print('1. A pangkat B')
        print('2. Barisan 1,3,3,6,18,24')
        Pilih = int(input('Masukkan menu pilihan : '))
        os.system('cls')
    return Pilih
        
#subrutin memasukkan harga A
def IsiA(A):
    A = int(input('Masukkan nilai A : '))
    return A

#subrutin memasukkan harga B
def IsiB(A, B):
    B = int(input('Masukkan nilai B : '))
    while (B < 0):
        print('nilai B tidak boleh negatif')
        os.system('pause')
        os.system('cls')
        print('A pangkat B')
        print(f'nilai A = {A}')
        B = int(input('Masukkan nilai B : '))
    return B

#subrutin rekursif hasil perhitungan
def Pangkat(A,B):
    if (B == 0):
        return 1
    else:
        if (B == 1):
            return A
        else:
            return A * Pangkat(A, B-1)

#subrutin menampilkan hasil a pangkat b        
def TampilAPangkatB(A, B):
    A = IsiA(A)
    B = IsiB(A, B)
    print(f'{A} pangkat {B} = {Pangkat(A,B)}')
    print('\n')
    print('enter untuk melanjutkan')
    os.system('pause')
    os.system('cls')
    
#subrutin memasukkan banyak suku yang akan ditampilkan
def BanyakSuku(N):
    N = int(input('Masukkan banyak suku : '))
    while (N < 0) or (N > 20):
        print('Nilai banyak suku tidak boleh kurang dari 1 atau lebih dari 20')
    return N
        
def SukuKeN(N):
    if (N == 1):
        return 1
    else:
        if (N == 2):
            return 3
        else:
            if (N % 2 == 1):
                return SukuKeN(N-2) * SukuKeN(N-1)
            else:
                return SukuKeN(N-2) + SukuKeN(N-1)
    
#subrutin menampilkan barisan 1, 3, 3, 6, 18, 24
def TampilBarisan(N):
    N = BanyakSuku(N)
    print(f'Barisan sebanyak {N} suku adalah')
    for i in range (1, N+1):
        print(SukuKeN(i), end='')
        if i < N :
            print(', ', end='')
    print('\n')
    print('enter untuk melanjutkan')
    os.system('pause')
    os.system('cls')
    
#badan program utama
Pilih = 0
Pilih = MenuPilihan(Pilih)
while (Pilih != 0):
    match Pilih :
        case 1 :
            print('A pangkat B')
            A = 0
            B = 0
            TampilAPangkatB(A,B)
        case 2 : 
            print('Barisan 1, 3, 3, 6, 18, 24')
            N = 0
            TampilBarisan(N)
    Pilih = MenuPilihan(Pilih)
    