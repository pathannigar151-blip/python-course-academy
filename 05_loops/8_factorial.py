num=int(input("Enter a number: "))
fact=1
n=num

while num >=1:
    fact = fact *num
    num =num - 1

print(f"fact of {n} is {fact}")