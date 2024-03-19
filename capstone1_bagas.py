
A0001 = {
    "Nama ": "Ghia Glaseria",
    "Alamat": "Jakarta",
    "Kamar": '001',
    "Usia": 23
}
A0002 = {
    "Nama ": "Benyamin suep",
    "Alamat": "Jakarta",
    "Kamar": '002',
    "Usia": 34
}
A0003 = {
    "Nama ": "Vincent Desta",
    "Alamat": "Jakarta",
    "Kamar": '003',
    "Usia": 21
}
List = { 
    "A0001": A0001,
    "A0002": A0002,
    "A0003": A0003
}
from prettytable import PrettyTable

def daftarpasien():
    table = PrettyTable()
    table.field_names = ["ID_pasien", "Nama", "Alamat", "Kamar", "Usia"]
    for pasien_id, pasien_data in List.items():
        table.add_row([
            pasien_id,
            pasien_data["Nama "],
            pasien_data["Alamat"],
            pasien_data["Kamar"],
            pasien_data["Usia"]
        ])
    print("\nDaftar Pasien\n")
    print(table)


def menampilkandaftar():
    menuHalaman1 = input('''\n
        Daftar Pilihan Menu :
        1. Tampilkan Seluruh daftar pasien
        2. Cari Data Pasien Berdasarkan ID_pasien
        3. Kembali ke Menu Utama

        Silahkan Memasukkan Angka Pilihan Menu Anda : ''')

    if menuHalaman1 == '1':
        daftarpasien()
        menampilkandaftar()
    elif menuHalaman1 == '2':
        while True:
            cariPasien = input('\nSilahkan Memasukkan Kode ID_pasien Yang Ingin Dicari : ')
            if cariPasien in List.keys():
                print('\nHasil Pencarian Daftar Pasien Berdasarkan ID_pasien\n')
                header = ["ID_pasien", "Nama", "Alamat", "Kamar", "Usia"]
                rows = [[cariPasien, List[cariPasien]["Nama "], List[cariPasien]["Alamat"], List[cariPasien]["Kamar"], List[cariPasien]["Usia"]]]
                table = PrettyTable(header)
                for row in rows:
                    table.add_row(row)
                print(table)
                cariLagi = input('\nApakah Ada Lagi ID pasien Yang Ingin Dicari? (YES/NO): ').upper()
                if cariLagi == 'NO':
                    menuUtama()
                elif cariLagi == 'YES':
                    continue
            else:
                print('\n~ Tidak Ada Kode ID pasien Tersebut ~')
                continue
    else:
        menuUtama()


def Menambahdaftar():
    menuHalaman2 = input('''\n
        Daftar Pilihan Menu :
        1. Tambah daftar pasien
        2. Kembali kemenu utama

        Silahkan Memasukkan Angka Pilihan Menu Anda : ''')
    
    if menuHalaman2 == '1':
        while True:
            daftarpasien()
            print('\nMenambah Daftar Pasien')
            
            # Membuat ID_pasien baru dengan nomor urut
            ID_pasienBaru = f"A{int(max([int(key[1:]) for key in List.keys()])+1):04}"
            
            daftarTemplate = {
                "Nama ": "namapasien",
                "Alamat": "alamatpasien",
                "Kamar": 0,
                "Usia": 0
            }
            pasienBaru = dict.fromkeys(daftarTemplate.keys())
            pasienBaru["ID_pasien"] = ID_pasienBaru
            
            pasienBaru["Nama "] = input('Silahkan Masukkan Nama Pasien (Maksimal 20 karakter): ')[:20]
            pasienBaru["Alamat"] = input('Silahkan Masukkan Alamat Pasien (Maksimal 20 karakter): ')[:20]
            while True:
                kamar = input('Silahkan Masukkan Kamar (3 digit angka) : ')
                if len(kamar) == 3 and kamar.isdigit():
                    pasienBaru["Kamar"] = int(kamar)
                    break
                else:
                    print("Silahkan masukkan 3 digit angka untuk kamar.") 
            while True:
                usia = input('Silahkan Masukkan Usia Pasien (Maksimal 2 digit): ')
                if usia.isdigit() and int(usia) < 100:
                    pasienBaru["Usia"] = int(usia)
                    break
                else:
                    print("Silahkan masukkan usia dengan format angka dan maksimal 2 digit.") 
                    
            List.update({ID_pasienBaru: pasienBaru})
            daftarpasien()
            print('\n')
            tambahLagi = input('~ Data Pasien Baru Telah Tersimpan ~\nApakah Anda Mau Menambahkan Lagi? (YES/NO): ').upper()
            if tambahLagi == 'NO':
                menuUtama()
    elif menuHalaman2 == '2': 
        menuUtama()

                  
def mengeditdaftar():
    menuHalaman3 = input('''\n
        Daftar Pilihan Menu :
        1. Mengedit daftar pasien
        2. Kembali kemenu utama

        Silahkan Memasukkan Angka Pilihan Menu Anda : ''')
    
    if menuHalaman3 == '1':
        while True:
            editPasien = input('\nSilahkan Masukkan ID_pasien Yang Ingin Di Edit : ')
            if editPasien not in List:
                print('\n~ Tidak Ada Pasien Dengan Kode ID_pasien Tersebut ~')
                continue
            else:
                print('\nPilihan Data Pasien Yang Akan Di Edit\n')
                headers = ["ID_pasien", "Nama", "Alamat", "Kamar", "Usia"]
                table = PrettyTable(headers)
                table.add_row([
                    editPasien,
                    List[editPasien]["Nama "],
                    List[editPasien]["Alamat"],
                    List[editPasien]["Kamar"],
                    List[editPasien]["Usia"]
                ])
                print(table)
                
                confirmation = input('\nApakah anda yakin ingin mengedit? (ya/tidak): ')
                if confirmation.lower() == 'ya':
                    while True:
                        keysUpdate = input('\nSilahkan Masukkan Nama Kolom Data Yang Ingin Di Edit: ')
                        if keysUpdate not in headers:
                            print("\nKolom yang dimasukkan tidak valid.")
                            continue
                        updateData = input(f'\nSilahkan Masukkan Update Data Terbaru untuk Kolom "{keysUpdate}": ')
                        List[editPasien][keysUpdate] = updateData

                        # Menampilkan data yang telah diedit
                        print('\nData Pasien Yang Telah Di Edit\n')
                        table_edit = PrettyTable(headers)
                        table_edit.add_row([
                            editPasien,
                            List[editPasien]["Nama"],
                            List[editPasien]["Alamat"],
                            List[editPasien]["Kamar"],
                            List[editPasien]["Usia"]
                        ])
                        print(table_edit)

                        moreEdit = input('\nAda lagi yang mesti diedit? (ya/tidak): ')
                        if moreEdit.lower() != 'ya':
                            break
                        
                    print("\nPengeditan selesai.")
                    break


def menghapusdaftar():
    menuHalaman4=input('''\n

        Daftar Pilihan Menu :
                       
        1. Menghapus daftar pasien
        2. Kembali kemenu utama

        Silahkan Memasukkan Angka Pilihan Menu Anda : ''')
    if(menuHalaman4 == '1') :
        while(True):
            daftarpasien()
            ID_pasien = input('\nSilahkan Masukkan Kode ID_pasien Yang Ingin Dihapus : ')
            if ID_pasien not in List:
                print('\n~ Tidak Ada Pasien Dengan Kode ID_pasien Tersebut ~')
                continue
            else :
                break
        while(True):
            yakinHapus = input('\nApakah Anda Yakin Mau Menghapus Data Ini? (YES/NO): ').upper()
            if(yakinHapus == 'NO'):
                print(f"\n~ Pasien Dengan Kode ID_pasien {ID_pasien} Tidak Berhasil Dihapus ~ ")
                menuUtama()
            elif(yakinHapus == 'YES'): 
                List.pop(ID_pasien)
                daftarpasien()
                print(f"\n~ Pasien Dengan Kode ID_pasien: {ID_pasien} Sudah Berhasil Dihapus ~")
                menuUtama()
    elif(menuHalaman4 == '2'): 
        menuUtama()


def menuUtama():
    pilihanMenu = input('''\n
    Selamat Datang di Rumah Sakit Surya

    Daftar Pilihan Menu :
    1. Menampilkan Daftar Pasien
    2. Menambah Daftar Pasien
    3. Mengedit Data Pasien
    4. Menghapus Data Pasien
    5. Exit Program

    Silahkan Memasukkan Angka Pilihan Menu Anda : ''')

    if(pilihanMenu == '1') :
        menampilkandaftar()
    
    elif(pilihanMenu == '2') :
        Menambahdaftar()

    elif(pilihanMenu == '3') :
        mengeditdaftar()

    elif(pilihanMenu == '4') :
        menghapusdaftar()
        
    elif(pilihanMenu == "5") :
        print('\n~ Anda Telah Berhasil Keluar Dari Program ~\n')
        exit()

menuUtama()