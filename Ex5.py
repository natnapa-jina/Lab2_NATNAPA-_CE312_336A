#lab2 Ex5
array = [["Number ID","Name","Count","Status"],[]]
array= list(array)
print(array)
print("\n")
array[1] = ([1,"Rubber",0,"Out of stock"])
print(array[1])
array[1] = ([2,"Ruler",5,"In stock"])
print(array[1])
array[1] = ([3,"Pencil",1,"In stock"])
print(array[1])
array[1] = ([4,"Pen",10,"In stock"])
print(array[1])
array[1] = ([5,"Colour pencil",5,"In stock"])
print(array[1])
array[1] = ([6,"A4 Paper",0,"Out of stock"])
print(array[1])


array[1] = ([1,"Rubber",0,"Out of stock"])
array.append([2,"Ruler",5,"In stock"])
array.append([3,"Pencil",1,"In stock"])
array.append([4,"Pen",10,"In stock"])
array.append([5,"Color pencil",5,"In stock"])
array.append([6,"A4 Paper",0,"Out of stock"])

print("\n")

for j in range (1,len(array),1):
    if  array[j][2] == "In  stock":
        print(array[j])
print("\n")
        
for j in range (1,len(array),1):
    if  array[j][3] == "Out of stock":
        print(array[j])

