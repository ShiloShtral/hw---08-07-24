x: int = int(input("whats your grade?"))
if x in range(0 , 40):
    print("try harder next time...")

elif x in range(41, 60):
    print("you're getting there, need some more work")

elif x in range(61, 80):
    print("pretty good")

elif x in range(81 , 95):
    print("awesome!")

elif x in range(95 , 100):
    print("excelent your are a star!")
elif x < 0:
    print("illigal grade")
elif x > 100:
    print("illigal grade")

