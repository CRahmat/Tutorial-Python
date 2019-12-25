
def adminMenu():
    listObat = {"ID": '', "Nama": '', "Harga": ''}
    print(50 * "=")
    print(15 * " ", "ADMIN MENU")
    print(50 * "=")
    print("1. INSERT DATA")
    print("2. LIST DATA")
    print("3. DELETE DATA")
    print("4. UPDATE DATA")
    print("5. CARI DATA")
    print("6. KEMBALI")
    choice = (int)(input("PILIH : "))
    if(choice == 1):
        print(50 * "=")
        print(15 * " ", "INPUT DATA")
        print(50 * "=")
        kodeObat = input("Kode Obat  : ")
        namaObat = input("Nama Obat  : ")
        hargaObat = input("Harga Obat : ")
        listObat = {"ID" : kodeObat, "Nama" : namaObat, "Harga" : hargaObat}
        print(listObat.items())
    elif(choice == 2):
        print(50 * "=")
        print(15 * " ", "LIST DATA")
        print(50 * "=")
        print("Kode Obat  : ",listObat.values())
        print("Nama Obat  : ",listObat.values())
        print("Harga Obat  : ",listObat.values())
