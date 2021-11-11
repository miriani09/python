# # task1
# inp = input("enter text: ")
# print(len(inp))

# task2
# inp1 = input("enter text one: ")
# inp2 = input("enter text second: ")
# output = inp1 + inp2
# print(output)

# task3
# inp = input("enter text: ")
# print(inp.count("a"))

# task4
# inp1 = "Banana", "Watermelon", "Apple"
# print(sorted(inp1))

# task5
# text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების."
# first20 = text[0:20]
# print(first20)
# print(first20.count("ს"))

# task9
# text = "Hello, this is example of string. Please, write this text and do some exercises."
# find = text.replace("is", "were")
# print(find)

# task10
# text = "Hello, this is example of string. Please, write this text and do some exercises."
# print(len(text))

# task11
# text = "Have a nice day"
# for i in range(len(text)):
#     print(text[-i])

# task12
# text = "miriani@gmail.com"
# print(text.find("@"))

# task13
# inp = input("enter name: ")
# inp2 = input("enter surname: ")
# print(f"{inp}.{inp2}@gmail.com")

import numpy as np
import random

# task14
# vec1 = np.array([1, 2, 3])
# vec2 = np.array([4, 5, 6])
# print(vec1 + vec2)
# vec3 = np.array([random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10)])
# vec4 = np.array([random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10)])
# print(vec3 + vec4)

# task15
# matrix1 = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
# matrix2 = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
# print(matrix1 + matrix2)

# task16
# vec1 = np.array([1, 2, 3])
# vec2 = np.array([4, 5, 6])
# print(vec1 * vec2)

# task17
# matrix1 = np.array([[1, 2, 3],
#                     [4, 5, 6],
#                     [7, 8, 9]])
# matrix2 = np.array([[1, 2, 3],
#                     [4, 5, 6],
#                     [7, 8, 9]])
# print(np.matmul(matrix1, matrix2))

# task18
# matrix3x3 = np.random.randint(10, size=(3, 3))
# print(matrix3x3)

# 19
import numpy.core.defchararray

# task20

# task21
# matrix10x10 = np.random.randint(10, size=(10, 10))
# print(np.where(matrix10x10 < 1, 1, matrix10x10))

# task22
print(np.kron([[1, 0] * 4, [0, 1] * 4] * 4, np.ones((10, 10))))

#task23
