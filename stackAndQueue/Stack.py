stack = ["Book1","Book2","Book3 ", "Book4"]
#PRINSIP STACK ADALAH LIFO(Last in First Out]

#Print
print("Kondisi Awal Stack : ",stack)
#Menambah Tumpukan
stack.append("Book5")
stack.append("Book6")
print("Setelah Di Tambahkan Data : ",stack)

#Mengambil Data
#Untuk remove, menghapus data dengan indek, untuk itu menggunakan fungsi pop

stack.pop()
print(stack.pop()," Telah Keluar!!!")
print("Tumpukan Sekarang : ",stack)