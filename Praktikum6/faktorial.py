#Program Menghitung Faktorial
#I.S.: Pengguna memasukkan harga yang akan difaktorkan
#F.S.: Menampilkan hasil faktorial N
import os

def IsiN(N):
    os.system('cls')
    print('PROGRAM MENGHITUNG FAKTORIAL N')
    N = int(input('harga yang akan difaktorialkan (N) : '))
    #validasi
    while (N < 0):
        print('Harga N tidak boleh negatif, ulangi')
        os.system('pause')
        os.system('cls')
        N = int(input('harga yang akan difaktorialkan : '))
    
    return N

def faktorial(N):
    if (N == 0) or (N == 1):
        return 1
    else:
        faktorialN = 1
        for i in range (N, 1, -1):
            faktorialN = faktorialN * i
            print(i, end='')
            if (i > 2):
                print('x', end='')
        print('\n', end='')
            
        return faktorialN

def Tampilfaktorial(N):
    print(f'{N}! = {faktorial(N)}') 

#badan program utama

N = 0
N = IsiN(N)

Tampilfaktorial(N)