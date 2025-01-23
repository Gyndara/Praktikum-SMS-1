import os

def MenuUtama(Pilih):
    print('<< Menu Utama >>')
    print('1. Mengisi data mahasiswa')
    print('2. Sorting NIM (Bubble sort ascending)')
    print('3. Sorting Nama (Bubble sort descending)')
    print('4. Sorting Nilai Akhir (Maximum sort ascending)')
    print('5. Sorting Nilai Indeks (Minimum sort ascending)')
    print('0. Keluar')
    Pilih = int(input('Masukkan pilihan menu : '))
    while (Pilih < 0) or (Pilih > 5):
        print('Menu tidak ada')
        Pilih = int(input('Masukkan pilihan menu : '))
    return Pilih

def IsiData():
    Kelas = input('Masukkan kelas: ')
    MataKuliah = input('Masukkan mata kuliah: ')
    data_mahasiswa = []  # List untuk menyimpan data mahasiswa
    
    while True:
        Nim = input('Masukkan NIM (ketik "STOP" untuk berhenti): ')
        if Nim.upper() == 'STOP':
            break
        Nama = input('Masukkan Nama: ')
        NilaiAkhir = float(input('Masukkan Nilai Akhir: '))
        
        # Menentukan Indeks Nilai
        if NilaiAkhir >= 80:
            IndeksNilai = 'A'
        elif NilaiAkhir >= 70:
            IndeksNilai = 'B'
        elif NilaiAkhir >= 60:
            IndeksNilai = 'C'
        else:
            IndeksNilai = 'D'
        
        # Menyimpan data mahasiswa ke dalam list
        data_mahasiswa.append({
            "NIM": Nim,
            "Nama": Nama,
            "Nilai Akhir": NilaiAkhir,
            "Indeks Nilai": IndeksNilai
        })
    
    return Kelas, MataKuliah, data_mahasiswa

def BubbleSortAscending(data, key):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]

def BubbleSortDescending(data, key):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j][key] < data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]

def MaximumSortAscending(data, key):
    for i in range(len(data)):
        max_idx = i
        for j in range(i + 1, len(data)):
            if data[j][key] < data[max_idx][key]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]

def MinimumSortAscending(data, key):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j][key] < data[min_idx][key]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def TampilkanData(data):
    print(f"{'NIM':<15}{'Nama':<20}{'Nilai Akhir':<15}{'Indeks Nilai':<10}")
    for row in data:
        print(f"{row['NIM']:<15}{row['Nama']:<20}{row['Nilai Akhir']:<15}{row['Indeks Nilai']:<10}")


data_mahasiswa = []
Pilih = 0
Pilih = MenuUtama(Pilih)
while Pilih != 0:
    match Pilih:
        case 1:
            print('Mengisi data mahasiswa')
            Kelas, MataKuliah, data_mahasiswa = IsiData()
        case 2:
            print('Sorting NIM menggunakan Bubble Sort Ascending')
            BubbleSortAscending(data_mahasiswa, "NIM")
        case 3:
            print('Sorting Nama menggunakan Bubble Sort Descending')
            BubbleSortDescending(data_mahasiswa, "Nama")
        case 4:
            print('Sorting Nilai Akhir menggunakan Maximum Sort Ascending')
            MaximumSortAscending(data_mahasiswa, "Nilai Akhir")
        case 5:
            print('Sorting Indeks Nilai menggunakan Minimum Sort Ascending')
            MinimumSortAscending(data_mahasiswa, "Indeks Nilai")
    
    print('\nData Mahasiswa:')
    TampilkanData(data_mahasiswa)
    
    Pilih = MenuUtama(Pilih)
print("Keluar dari program.")

