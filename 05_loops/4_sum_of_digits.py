# Input a number
num = int(input("Enter a number: "))

sum_digits = 0
product_digits = 1

# Process each digit
for digit in str(num):
    sum_digits += int(digit)
    product_digits *= int(digit)

# Print results
print("Sum of digits:", sum_digits)
print("Product of digits:", product_digits)

