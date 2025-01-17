#program faktorial
#I.S.: pengguna memasukkan nilai yang akan difaktorialkan
#F.S.: Menampilkan hasil faktorial


#memasukan angka fak
def IsiN(N):
    print('menghitung faktorial (rekursif)')
    N = int(input('Masukkan nilai yang akan difaktorialkan : '))
    #validase
    while (N < 0):
        print('Nilai tidak boleh kurang dari 0')
        print('menghitung faktorial (rekursif)')
        N = int(input('Masukkan nilai yang akan difaktorialkan : '))
    return N

#subrutin rekrusif
def faktorial(N):
    if (N == 0) or (N == 1):
        return 1
    else:
        return N * faktorial(N-1)
    
#subrutin menampilkan hasil perhitungan    
def TampilFaktorial(N):
    print(f'{N}! = {faktorial(N)}')

N = 0
N = IsiN(N)
TampilFaktorial(N)

# def fak(N):
#     N = int(input('Masukkan nilai N : '))
#     while (N < 0):
#         print('Nilai tidak boleh kurang dari 0')
#         N = int(input('Masukkan nilai N : '))
        
# def faktorial(N):
#     if (N == 0):
#         return