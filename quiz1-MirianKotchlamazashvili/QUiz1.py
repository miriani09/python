import random

# TASK 1
# thisDict = {}
# for i in range(10):
#     randNum = random.randint(1, 100)
#     thisDict[randNum] = (randNum % 10) + (randNum // 10)
# print(thisDict)
# print(max(thisDict.values()))

# ------------------------------------------------------------------------

# TASK2
# myList = []
# for i in range(20):
#     rand = random.randint(5, 15)
#     myList.append(rand)
# print("ყველაზე ხშირად განმეორებადი :", max(myList, key=myList.count))
# print("სულ განსხვავებული ელემენტები :", len(set(myList)))
# print(myList)


# TASK3
texts = 'აბგდევზთიკლმნოპრჟსტუფქღყშცძწჰ'
myList = []
vowel = ["ა,ე,ი,ო,უ"]
for i in range(20):
    myList.append(''.join(random.choice(texts) for j in range(5, 10)))
    for k in vowel:
        if k in vowel:
            print(max(myList, key=myList.count))
print(myList)
