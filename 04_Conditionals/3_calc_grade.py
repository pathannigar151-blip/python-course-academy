# Input marks from user
marks = float(input("Enter your marks (0 to 100): "))

# Use conditions to assign grade
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid Input! Please enter marks between 0 and 100.")

