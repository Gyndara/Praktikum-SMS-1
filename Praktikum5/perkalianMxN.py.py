#menghiutng perkalian M dan N
#I.S.: pengguna memasukan nilam M dan N
#F.s.: menampilkan hasil perkalian M dan N

#badan program
print('<<<<< PERKALIAN NILAI M DENGAN N >>>>>>')
print('---------------------------------------')
M = int(input('Masukan Nilai M : '))
while (M > 20) or (M < 0):
    print('Nilai antara 20 sampai 0')
    M = int(input('Masukan Nilai M : '))

N = int(input('Masukan Nilai N : '))
while (N > 15) or (N < -5):
    print('Nilai M : ', M)
    print('Nilai antara 15 sampai -5')
    N = int(input('Masukan Nilai N : '))
    
print('---------------------------------------')
    
if (M == 0 ) or (N == 0):
    Kali = 0
    print(f'{M} x {N} = ', Kali)
else:
    if (M == 1):
        Kali = N
        print(f'{M} x {N} = ', Kali)
    else:
        Kali = 0
        print(f'{M} x {N} = ', end='')
        for i in range(1, M+1):
            print(N, end='')
            Kali = Kali + N
            if(i < M):
                print(' + ', end='')
        print(f'\n      = {Kali}')
    