#import library karena tidak ada fungsi built in
#Prinsip dari antrian adalah FIFO(First In First Out)
from _collections import deque
Queue = deque(["Budi","Rani","Dian","Silvi","Hani"])
print("Antian saat ini : ",Queue)
print(80*"=")
#menambahkan data
Queue.append("Rima")
print("Antian saat ini : ",Queue)
print(80*"=")
Queue.append("Ice Bear")
print("Antian saat ini : ",Queue)
print(80*"=")
#Menghapus Antrian
out = Queue.popleft()
print("Antrian Keluar  : ",out)
print("Antian saat ini : ",Queue)
print(80*"=")
out = Queue.popleft()
print("Antrian Keluar  : ",out)
print("Antian saat ini : ",Queue)
print(80*"=")
out = Queue.popleft()
print("Antrian Keluar  : ",out)
print("Antian saat ini : ",Queue)
print(80*"=")
#menambahkan data
Queue.append("Pan Pan")
print("Antian saat ini : ",Queue)
print(80*"=")
Queue.append("Grizy")
print("Antian saat ini : ",Queue)
print(80*"=")