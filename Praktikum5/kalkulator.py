


A = int(input('Masukan nilai A : '))
B = int(input('Masukan nilai B : '))
Operasi = input('masukan operasi : ')

if (Operasi == '+'):
    Hasil = A + B
    print(F'{A} + {B} = ', Hasil)
elif(Operasi == '-'):
    Hasil = A - B
    print(F'{A} - {B} = ', Hasil)
elif(Operasi == ':'):
    Hasil = A / B
    print(F'{A} : {B} = ', Hasil)
elif(Operasi == 'x'):
    Hasil = A * B
    print(F'{A} x {B} = ', Hasil)
    