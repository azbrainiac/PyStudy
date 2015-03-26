print("Hello")
print(2**10)
print(7 % 3)
print((5 >= 1) and (5 <= 10))

myList = [1, 2, 3, 4]
A = [myList]*3
print(A)
myList.append(5)
print(A)
B = A.pop()
print(A)
print(B)
A.insert(1, [5, 1])
print(A)
A.sort()
print(A)
A.reverse()
print(A)
del A[0]
print(A)
B = A.index([1, 2, 3, 4, 5])
print(B)
B = A.count(myList)
print(B)
A.remove(myList)
print(A)
print(myList[1:3])
C = (77).__add__(22)
print(C)
print(list(range(13, 5, -3)))
print("Vasya".upper().center(7)*2)
print("Vasya".split("a"))
print("Vasya".center(7))
print("VasyaVasya".count("aV"))

mySet = {2, "Carrot", True, 8.11}
print(mySet.pop())
print(mySet.pop())

myDict = {"Ukraine": "Kyiv", "Russia": "Moscow"}
print(myDict.keys())
print(len(myDict))
for s in myDict:
	print(myDict[s], "is the capital of", s)
	print("ha")
print("ho")
myDict["Poland"] = "Warsaw"
for s in myDict:
	print(myDict[s], "is the capital of", s)
listCap = myDict.values()
print(list(listCap))
print(listCap)