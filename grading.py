marks = int(input("Enter the marks: "))
if (marks <= 100 and marks >= 90):
    print("Grade A")
elif (marks < 90 and marks >= 85):
    print("Grade B")
elif (marks < 85 and marks >= 70):
    print("Grade C")
elif (marks < 70 and marks >= 55):
    print("Grade D")
elif (marks < 55 and marks >= 40):
    print("Grade E")
else:
    print("Grade F")