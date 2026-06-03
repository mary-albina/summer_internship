#Number Analysis
num= int(input("enter a positive integer: "))
sum =0
reverse=0
count= 0
while num> 0:
    digit = num % 10
    count += 1
    sum += digit
    reverse = reverse*10 + digit
    num = num//10
print("Number of digits:", count)
print("Sum of digits:", sum)
print("Reversed number:", reverse)

