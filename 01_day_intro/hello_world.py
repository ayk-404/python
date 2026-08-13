# skip Exercises 1 & 2
# Exercise 3: 
'''
1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
2. Find an Euclidean distance between (2, 3) and (10, 8) 
'''
# 3.1
int = 3
float = 3.14
complex = 2 + 3j
sting = "Hello"
boolean = True
list = [1, 2, 3, 4]
tuple = (1, 2, 3, 4)
set = {1, 2, 3, 4}
dictionary = {"name": "John", "age": 30}
# 3.2
import math
a = (2,3)
b = (10,8)

def euclidean_distance(x,y): 
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

print(euclidean_distance(a,b))
