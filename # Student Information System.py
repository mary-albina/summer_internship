# Student Information System
name = input("enter your name: ")
age = input("enter your age: ")
math = float(input("enter your math marks: "))
science = float(input("enter your science marks: "))
english = float(input("enter your english marks: "))
total = math + science + english

print("***********************************************")
print("REPORT")
print("Name: " + name)
print("Age: " + age)
print("Math Mark: " + str(math))
print("Science Mark: " + str(science))
print("Science Mark: " + str(english))
print("Total= " + str(total))
print("Average= " + str((total/3)))