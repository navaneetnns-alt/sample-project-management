print("Welcome to Grade Calculator!")
name = input("Enter student name: ")
mark1 = int(input("Enter mark for Subject 1: "))
mark2 = int(input("Enter mark for Subject 2: "))
mark3 = int(input("Enter mark for Subject 3: "))

avg = (mark1 + mark2 + mark3) / 3

if avg >= 90:
    grade = 'A'
elif avg >= 75:
    grade = 'B'
elif avg >= 60:
    grade = 'C'
elif avg >= 45:
    grade = 'D'
else:
    grade = 'F'

print(f"\nStudent Name: {name}")
print(f"Average Marks: {avg}")
print(f"Grade: {grade}")
