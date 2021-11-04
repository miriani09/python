# f = open("myfiles/demofile.txt", "w")
# f.write("29, 34, -90")
# f.close()

# task2
# for i in range(100):
#     i += 1
#     f = open("myfiles/data1.txt", "a")
#     f.write(" " + str(i) + "")
#     f.close()

# # task3-task4
# for i in range(30):
#     f = open(f"myfiles1/demofile{i}.txt", "w")
#     f.write(f"programming{i}")
#     f.close()

# #task5+task6
# from random import random, randrange
# for i in range(100):
#     rand = randrange(100)
#     f = open(f"myfiles/data2.txt", "a")
#     f.write(str(rand) + " ")
#     f.close()

# task9
# for i in range(10000):
#     f = open(f"myfiles/data{i}.txt", "a")
#     f.write(str(i) + " ")
#     f.close()

# task10
# dict = {
#     0: 10,
#     1: 20
# }
# dict.update({2: 30, 3: 40})
# dict.pop(0)
# print(dict)

# task11
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# task12
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# if 1 in d.keys():
#     print("exists")
# else:
#     print("not exists")

# task13
# d = {"x": 10, "y": 20, "z": 30}
# for key, value in d.items():
#     print(key, "-=", value)

# task14
# d = {}
# for i in range(1, 11):
#     d.update({i: i ** 2})
# print(d)
