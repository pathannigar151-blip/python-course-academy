num=int(input("Enter a number"))
n= num

lenght_of_num= len(str(num))
sum=0

while num !=0:
    dig=num%10
    sum=sum+(dig**lenght_of_num)
    num= num//10
    
ans= "armstrong" if sum== n else "Not armstrong"
print(f"{n} is{ans}")


                