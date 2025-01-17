#program menentukan indeks nilai
#I.S.: penggunan memasukan nilai
#F.S.: menampilkan indeks nilai [A/B/C/D/E]

#badan program
# Nilai = int(input('Masukan Nilai : '))

Nilai = float(input('Masukan Nilai : '))

if(Nilai >= 80) and (Nilai <= 100):
    Indeks = 'A'
else:
    if(Nilai >= 70) and (Nilai < 80):
        Indeks = 'B'
    else:
        if(Nilai >= 60) and (Nilai < 70):
            Indeks = 'C'
        else:
            if(Nilai >= 50) and (Nilai < 60):
                Indeks = 'D' 
            else:
                if(Nilai >= 40) and (Nilai < 50):
                    Indeks = 'E'
                else:
                    Indeks = 'Nilai hanya antara 0-100'

#menyederhanakan
print('Nilai  anda : ', Nilai)
print('Indeks anda : ', Indeks)