#Struktur data dengan mapping
#Standart syntax = dictionary  = {key : value, key : value} OR
                  #dictionary  = {key : value,
                                # key : value,
                                # key : value}
member1 = {"ID" : 100001,
           "Name" : "BUDI SETIAWAN",
           "Alamat" : "Jogjakarta",
           "Status Member" : "GOLD"
           }
member2 = {"ID" : 100002,
           "Name" : "BAMBANG BUDI SETIAWAN",
           "Alamat" : "Jogjakarta",
           "Status Member" : "SILVER"
           }
#print standart
print(member1)

#print with key
print(member1["ID"])
print(member1["Name"])

#Print key from Dictionary
print(member1.keys())

#Print Isi Dictionary
print(member1.values())

#Print All Items
print(member1.items())

#Menggabungkan list atau Nesting List
memberList = {1:member1,2:member2}

#Print
print(memberList[1])
print(memberList[2])