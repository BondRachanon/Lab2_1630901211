Array=[5,7,9,11,13]
print(Array)
print("----------------------")
Array_Length=len(Array)
print(Array_Length)
print("----------------------")
for i in range(0,Array_Length-1):
    sum = Array[i]+Array[i+1]
    print(sum)