#program pemilu seleksi pemilu
#I.S.: pengguna memasukan umur dan status pernikahan
#F.S.: menampilkan apakah boleh atau tidak melakukan pemilihan

#badan program
print('<<<< SELEKSI PEMILU >>>>')
Umur= int(input('Masukan umur : '))
if(Umur < 17):
    Menikah = (input('Status Menikah [Y/T] : ')).upper()
    '''
    if(Menikah == 'Y'):
        print('Anda boleh ikut pemilu')
    else:
        print('Anda tidak boleh ikut pemilu')
    '''
    #menyederhanakan bentuk if
    match (Menikah):
        case 'Y' : print('Anda boleh ikut pemilu')
        case 'T' : print('Anda tidak boleh ikut pemilu')
        case _   : print('Status menikah hanya bisa disi Y atau T')
else:
    print('anda boleh ikut pemilu')