sub1 = int(input("Enter first subject marks "))
sub2 = int(input("Enter Second subject marks "))
sub3 = int(input("Enter Third subject marks "))
total = sub1 + sub2 + sub3
avg = total / 3

if (avg >= 90 and avg <= 100):
    print("Grade A")
elif (avg >= 80 and avg <= 90):
    print("Grade B")
elif (avg >= 70 and avg <= 80):
    print("Grade C")
elif (avg >= 60 and avg <= 70):
    print("Grade D")
else:
    print("Fail")