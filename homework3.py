#find sum of all the elements in an array
array = [1, 2, 3, 4, 5]
sum_of_elements = sum(array)
print(sum_of_elements)

#find max element in an array
my_list = [10, 6, 8, 2, 4, 12, 3]
max_value = my_list[0]
for x in my_list:
    if x > max_value:
        max_value = x
print(max_value) 

#find 2max element in an array
data = [11, 22, 1, 2, 5, 67, 21, 32]
max1 = max2 =data[0]
for num in data:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print("Second largest number:", max2)

#find reverse an arraywithout builtin function
array = [1, 2, 3, 4, 5]
reversed_array = []
for i in range(len(array) - 1, -1, -1):
    reversed_array.append(array[i])
print(reversed_array)

#find the sum of squares of given number
number = 457
sum = 0
while number != 0:
    rem = number % 10
    sqr = rem ** 2
    sum += sqr
    number = number // 10
print("Result:", sum)

#find sum of squares of even and odd digits
number = int(input("Enter an integer: "))
even_sum, odd_sum = 0, 0
while number != 0:
    digit = number % 10
    if digit % 2 == 0:
        even_sum += digit ** 2
    else:
        odd_sum += digit ** 2
    number //= 10
print(f"Sum of squares of even digits: {even_sum}")
print(f"Sum of squares of odd digits: {odd_sum}")