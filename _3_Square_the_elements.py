# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list: [16, 25, 4, 81]


numbers = [4, 5, 2, 9]
def square_number(num):
  return num ** 2
result = list(map(square_number,numbers))
print("Result : ",result)
