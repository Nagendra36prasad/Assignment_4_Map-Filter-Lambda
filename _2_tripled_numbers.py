# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:  [3, 6, 9, 12, 15, 18, 21]

def triple_numbers(numbers):
    return list(map(lambda x: x*3, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]

tripled_numbers = triple_numbers(numbers)

print(tripled_numbers)

# without using 'lamda' function and  we can directly write a code using map function

numbers = [1, 2, 3, 4, 5, 6, 7]
def triple_numbers(numbers):
    return numbers *3
result = list(map(triple_numbers, numbers))

print("Result : ",result)