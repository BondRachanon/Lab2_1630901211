Array1=[["Number ID","Name","Count","Status"],[]]
print(Array1)
print(" ")
print("\nLength of array is:",len(Array1))
print(" ")

Array1.insert(1,[1,"Rubber",0,"Out of stock"])
Array1.insert(2,[2,"Ruler",5,"In stock"])
Array1.insert(3,[3,"Pencil",1,"In  stock"])
print(Array1)

Array1[1][2] = Array1[1][2] - 0
Array1[2][2] = Array1[2][2] - 1
Array1[3][2] = Array1[3][2] - 1
for i in Array1:
  for n in i:
    if i[2] == 0:
        i[3] = "Out of stock"
print(Array1)
Array2=[["Number ID","Name","Count","Status",]]
Array2.insert(4,[4,"Pen",10,"In  stock"])
Array2.insert(5,[5,"Colour Pencil",5,"In  stock"])
Array2.insert(6,[6,"A4 Paper",0,"Out of stock"])

print(Array2)
for i in Array2:
    for n in i:
        if n == "In stock":
            print(i)
for i in Array2:
    if i[3] == "In stock":
        print(i)
Array2[1][2] = Array2[1][2] - 2
Array2[2][2] = Array2[2][2] - 1
Array2[3][2] = Array2[3][2] - 0
for i in Array2:
    if i[2] == 0:
        i[3] = "Out of stock"
print(Array2)



