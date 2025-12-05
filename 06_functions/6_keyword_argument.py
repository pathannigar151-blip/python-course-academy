def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Rahul", age=20, city="Delhi")