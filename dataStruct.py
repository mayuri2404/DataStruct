myList = ["C","C++","Java","python","pHp"]
list2 = ["Node Js","angular"]
print(myList)
#assigning values by append
myList.append("Javascript")
print(myList)
#assigning value by insert at specific index
myList.insert(2,"pearl")
print(myList)
#assigning a list other list
myList.extend(list2)
print(myList)

myTuple = ("mango","apple","cherry","melon","grapes")
print(myTuple)
#accessing element by referring positive index
print(myTuple[2])
#accessing element by referring negative index
print(myTuple[-2])
#accessing element by range of index
print(myTuple[1:-1])

myDict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6}
print(myDict)
#deleting element using del
del myDict["D"]
print(myDict)
#deleting element using pop()
myDict.pop("F")
print(myDict)
