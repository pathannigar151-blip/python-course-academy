# Input a year
year = int(input("Enter a year: "))

# Check if divisible by 4
if year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
