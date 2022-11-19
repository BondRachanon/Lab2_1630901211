Array=[[7,5,10,14,3,9,7],[9,10,3,4,2,5,7,1]]
Array1=Array[0]
Array2=Array[1]
print(Array)
print("---------------------------------------------------------------------")
print("\nLength1:",len(Array[0]))
print("\nLength2:",len(Array[1]))
print("---------------------------------------------------------------------")

Array[0].insert(7,15)
print(Array)
print("---------------------------------------------------------------------")


Location_of_Seven1=Array[0].index(7)
Location_of_Seven2=Array[1].index(7)
print("\nLocation of seven in [1]:",Location_of_Seven1)
print("---------------------------------------------------------------------")

print("\nLocation of seven in [2]:",Location_of_Seven2)
print("---------------------------------------------------------------------")

Array[0].append(1)
Array[1].append(14)
print(Array,end=" ")

Array3=Array1.copy()
print(",",Array3,)

print("---------------------------------------------------------------------")
Array1.extend(Array2)
print("\nMerge new Array(1 and 2 ):",Array1)
print("---------------------------------------------------------------------")

Value=Array1.count(7)
print("\nValue is :",Value)
print("---------------------------------------------------------------------")

Array3.sort()
print("\nArray3rd sort is :",Array3)
print("---------------------------------------------------------------------")

Array3.remove(7)
print("\nArray3rd remove(7) is :",Array3)
print("---------------------------------------------------------------------")

Array4=Array3.copy()
print("\nArray4th is :",Array4)
print("---------------------------------------------------------------------")

Array4.reverse()
print("\nArray4th reverse  is :",Array4)
print("---------------------------------------------------------------------")
print("\nArray3rd is :",Array3,"Array4th is :",Array4)
