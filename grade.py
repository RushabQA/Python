mark1 = int(input("Enter your chemistry mark out of 100: "))
mark2 = int(input("Enter your physics mark out of 100: "))

tmark = ((mark1 + mark2) / 200 ) * 100
print(tmark)

if tmark < 40:
    print("You failed")
elif tmark >= 40:
    print("D")
elif tmark >= 50:
    print("C")
elif tmark >= 60:
    print("B")
elif tmark >= 70:
    print("A")