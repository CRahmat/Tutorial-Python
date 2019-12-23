import timeit
#List
list = [1,2,3,4,5,6,7,8,9]

#tuples
tuple = (1,2,3,4,5,6,7,8,9)

#Untuk print tipe data(mengetahui data yang digunakan)
print(type(list))
print(type(tuple))

#PERBEDAAN LIST DAN TUPPLES
    #1.Isi dari tuple tidak dapat di ubah nilainya

#Menambahkan data
list.append(10)
#tuple.append(2) ERROR

#Menambahkan data
list.remove(10)
#tuple.remove(2) ERROR

#CARA PRINT FUNCTION DARI TYPE DATA
print(dir(list))
print(dir(tuple))

#FUNGCTION DARI TUPLE
#1. Index
#2. Count

#TUPLE AKAN LEBIH RINGAN DARIPADA LIST DALAM PROSESNYA
#Print waktu proses
time_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=10000000)
time_tupple = timeit.timeit(stmt= "(1,2,3,4,5,6,7,8,9)",number=10000000)
print("Waktu proses list : ",time_list)
print("Waktu proses tuple : ",time_tupple)