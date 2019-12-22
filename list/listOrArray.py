#Print List
data = [1,2,3,4,5,6,7,8,9]
print(data)
#Akses List
print(data[0:5])
#Akses all Data
print(data[:])
#Manambah List
data2 = [10,11,12,13,14,15,16,17,18,19]
print(data+data2)
#Mengganti isi List
data2[0:5] = [20,21,22,23,24,25]
print(data+data2)
#Mancopy isi List ke Variable
data3 = data2[:]
print(data3)

#List dalam List
data4 = [data],[data2],[data3]
print(data4)

print(len(data))
print(len(data2))
print(len(data3))