# Input a number n
n = int(input("Enter a number: "))

# Print numbers from 1 to n
print("Natural numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i)

# Print numbers from n to 1 (reverse order)
print("Natural numbers from", n, "to 1:")
for i in range(n, 0, -1):
    print(i)