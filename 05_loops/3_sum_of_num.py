# Input a number n
n = int(input("Enter a number: "))

# Sum of natural numbers
sum_natural = 0
for i in range(1, n + 1):
    sum_natural += i

# Sum of odd numbers
sum_odd = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum_odd += i

# Sum of even numbers
sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

# Print all three sums
print("Sum of natural numbers:", sum_natural)
print("Sum of odd numbers:", sum_odd)
print("Sum of even numbers:", sum_even)
