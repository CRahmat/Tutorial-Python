#condition with Array
daftarMenu = ["SOTO","BAKSO","AYAM GORENG","AYAM BAKAR","BEBEK BAKAR","BEBEK GORENG"]
daftarHarga = [10000,12000,15000,17000,20000,25000]

beli = input("Massukan Menu Yang Di Beli : ")

if beli in daftarMenu :
    print("Menu Yang Di Pilih Tersedia!!!")
    if (beli == daftarMenu[0]):
        print("Anda Memilih Menu ",beli," Dengan Harga Rp",daftarHarga[0])
    if (beli == daftarMenu[1]):
        print("Anda Memilih Menu ",beli," Dengan Harga Rp",daftarHarga[1])
    if (beli == daftarMenu[2]):
        print("Anda Memilih Menu ",beli," Dengan Harga Rp",daftarHarga[2])
    if (beli == daftarMenu[3]):
        print("Anda Memilih Menu ",beli," Dengan Harga Rp",daftarHarga[3])
    if (beli == daftarMenu[4]):
        print("Anda Memilih Menu ",beli," Dengan Harga Rp",daftarHarga[4])
else:
    print("Menu Yang Anda Massukan Tidak Tersedia!!!!")
