# List Standar
listBarang = ["Smartphone", "Leptop", "Headshet", "Monitor", "Computer"]
print(listBarang)
print(120 * "=")
# manipulasi list
# Menambah list paling belakang
listBarang.append("Charger")
print(listBarang)
print(120 * "=")

# Menambah list per karakter
listBarang.extend("Baterai")
print(listBarang)
print(120 * "=")

# Menambah list sesuai index yang di tentukan
listBarang.insert(3, "Kartu SIM")
print(listBarang)
print(120 * "=")

# Menjumlahkan element dalam list
jumlah = listBarang.count("Computer")
print("Jumlah Barang Computer adalah ", jumlah)
print(120 * "=")

# Menghapus data dalam list
hapus = listBarang.remove("Kartu SIM")
print(listBarang)
print(120 * "=")

# Membalik isi dalam List
listBarang.reverse()
print(listBarang)
print(120 * "=")

# Merubah isi list dan sub list dengan append
Stuff = listBarang
Stuff.append("Bunga")
print(listBarang)
print(Stuff)

# Merubah sub list tanpa mengubah parent list
Stuff = listBarang.copy()
Stuff.append("Bunga")
print(listBarang)
print(Stuff)

#Mengurutkan isi dari list
listBarang.sort()
print(listBarang)

#Menghapus data dari list terakhir
listBarang.pop()
listBarang.pop()
listBarang.pop()
listBarang.pop()
listBarang.pop()
listBarang.pop()
print(listBarang)

#Menghapus semua isi dari list
listBarang.clear()
print(listBarang)   

