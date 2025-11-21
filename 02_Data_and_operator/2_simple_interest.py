# Input principal, rate, and time
principal=float(input("Enter your principal Amount:"))
rate=float(input("Enter your rate intrest:"))
time=float(input("Enter your time year:"))

# Calculate simple interest
interest=(principal*rate*time)/100

# Print the interest
print("simple interest",interest)
