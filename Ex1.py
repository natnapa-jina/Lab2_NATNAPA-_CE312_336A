array = [5,7,9,11,13]
num = 0

print(array)

array_Length = len(array)
print("length of integer array = ",len(array))

for a in range (0,len(array),1):
    num = num + array[a]
    
print("summation of array = ",num)