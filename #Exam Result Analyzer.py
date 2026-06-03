#Exam Result Analyzer
marks = []
for i in range(1, 6):
    mark = int(input(f"Enter mark for Subject {i}: "))
    marks.append(mark)
if any(mark < 40 for mark in marks):
    print("Result: FAIL")
else:
    average = sum(marks) / 5
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")