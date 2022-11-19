#lab2 Ex2
arry1 = [7,5,10,14,3,9,7]
arry2 = [9,10,3,4,2,5,7,1]

print(arry1)
print(arry2)

arry1_Length = len(arry1)
print("length of integer array = ",len(arry1))
arry2_Length = len(arry2)
print("length of second array = ",len(arry2))

arry1.append(15)
print(arry1)

index_of_seven = arry1.index(7)
index_of_seven = arry2.index(7)
print("index of 7 in arry1 = ", arry1.index(7))
print("index of 7 in arry2 = ",arry2.index(7))

arry1.append(1)
print(arry1)

arry2.append(14)
print(arry2)

arry3 = arry1.copy()
print(arry3)

arry3.extend(arry2)
print(arry3)

Value = arry3.count(7)
print("Count value of 7 in 3rdArray =",arry3.count(7))

arry3 = arry3
arry3.sort()
print("Sort 3rdArray =",arry3)

n = 0
while(n==0):
    if arry3.count(7) != 0 :
        arry3.remove(7)
    else:
        n = 1
print(arry3)

arry4 = arry3.copy()
print(arry4)

arry4.reverse()
print(arry4)

print("arry3 = ",arry3)
print("arry4 = ",arry4)