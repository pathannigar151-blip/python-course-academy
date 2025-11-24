# Input a number
num = int(input("Enter a number: "))

# Store original number
original = num
reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check if original and reverse are same
if original == reverse:
    print(original, "is a Palindrome number")
else:
    print(original, "is NOT a Palindrome number")
