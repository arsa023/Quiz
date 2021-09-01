choice = input("what area are u interested in: A:cars, B:computers, C:geography: ").lower()

score = 0
# Cars
if choice == "a":
    print("Your choice is cars, good luck!")

    car_q1 = input("In what country is Wolksvagen made: ").lower()
    if car_q1 == "germany":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    car_q2 = input("In what country is Ford made: ").lower()
    if car_q2 == "america":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    car_q3 = input("In what country is Peugeot made: ").lower()
    if car_q3 == "france":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    car_q4 = input("In What country is Punto made: ").lower()
    if car_q4 == "Italy":
        print("Correct")
        score += 1
    else:
        print("Incorrect")


# Computers
elif choice == "b":
    print("Your choice is computers, good luck!")

    cmpt_q1 = input("What does RAM stands for: ").lower()
    if cmpt_q1 == "random access memory":
        print("Correct")
        score += 1
    else:
        print("incorrect")

    cmpt_q2 = input("What does PSU stands for: ").lower()
    if cmpt_q2 == "power supply":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    cmpt_q3 = input("What does CPU st ands for: ").lower()
    if cmpt_q3 == "central processing unit":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    cmpt_q4 = input("Pascal is? ").lower()
    if cmpt_q4 == "programming langugage":
        print("Correct")
        score += 1
    else:
        print("Incorrect")




# geography
elif choice == "c":
    print("Your choice is geograpy, good luck!")

    geo_q1 = input("Where is Slovenia located: ").lower()
    if geo_q1 == "europe":
        print("Correct")
        score += 1
    else:
        print("incorrect")

    geo_q2 = input("What is the capital of Slovenia: ").lower()
    if geo_q2 == "ljubljana":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    geo_q3 = input("What is the capital of Serbia: ").lower()
    if geo_q3 == "belgrade":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("Your score is " + str(score))