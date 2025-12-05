english=float(input("Enter marks of English:"))
hindi=float(input("Enter marks of Hindi:"))
Science=float(input("Enter marks of Science:"))

def total(eng,hin,sci):
    return eng+hin+sci

def average(t):
    return t/3

def grade(avg):
    if avg>=90:
      return "1st number" 
    elif avg>=80:
      return "2nd number"
    elif avg>=70:
      return "3rd number"
    else:
      return "fail"

t=total(english,hindi,Science)
avg=average(t)
grade=grade(avg)

print("Total Marks=",t)
print("Average Marks=",avg)
print("Grade=",grade)