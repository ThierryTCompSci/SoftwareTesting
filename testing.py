import sys

def test1():
    grade1 = input("Please indicate grade 1: ")
    grade1=int(grade1)

    grade2 = input("Please indicate grade 2: ")
    grade2=int(grade2)

    grade3 = input("Please indicate grade 3: ")
    grade3=int(grade3)

    avg_grade=(grade1+grade2+grade3)/3
    print(avg_grade)

def test2():
    UserError=False
    grade1 = input("Please indicate grade 1: ")
    try:
        grade1=int(grade1)
    except ValueError:
        UserError=True
        print("The value you inserted has an incorrect type")

    if UserError==False:
        grade2 = input("Please indicate grade 2: ")
        try:
            grade2=int(grade2)
        except ValueError:
            UserError=True
            print("The value you inserted has an incorrect type")

    if UserError==False:
        grade3 = input("Please indicate grade 3: ")
        try:
            grade3=int(grade3)
        except ValueError:
            UserError=True
            print("The value you inserted has an incorrect type")

    if UserError==False:
        avg_grade=(grade1+grade2+grade3)/3
        print(avg_grade)

def test3():
    UserError=False
    grade1 = input("Please indicate grade 1: ")
    try:
        grade1=int(grade1)
        if((grade1<0) or (grade1>100)):
            print("The grade you inserted is out of bounds")
            sys.exit(0)
    except ValueError:
        UserError=True
        print("The value you inserted has an incorrect type")

    if UserError==False:
        grade2 = input("Please indicate grade 2: ")
        try:
            grade2=int(grade2)
            if((grade2<0) or (grade2>100)):
                print("The grade you inserted is out of bounds")
                sys.exit(0)
        except ValueError:
            UserError=True
            print("The value you inserted has an incorrect type")

    if UserError==False:
        grade3 = input("Please indicate grade 3: ")
        try:
            grade3=int(grade3)
            if((grade3<0) or (grade3>100)):
                print("The grade you inserted is out of bounds")
                sys.exit(0)
        except ValueError:
            UserError=True
            print("The value you inserted has an incorrect type")

    if UserError==False:
        avg_grade=(grade1+grade2+grade3)/3
        print(avg_grade)

def test4():
    grade1 = input("Please indicate grade 1: ")
    grade1=int(grade1)
    if((grade1<0) or (grade1>100)):
        print("The grade you inserted is out of bounds")
        sys.exit(0)

    grade2 = input("Please indicate grade 2: ")
    grade2=int(grade2)
    if((grade2<0) or (grade2>100)):
        print("The grade you inserted is out of bounds")
        sys.exit(0)

    grade3 = input("Please indicate grade 3: ")
    grade3=int(grade3)
    if((grade3<0) or (grade3>100)):
        print("The grade you inserted is out of bounds")
        sys.exit(0)

    avg_grade=(grade1+grade2+grade3)/3
    print(avg_grade)

print("This program calculate the average of grades (between 0 and 100)")
print("Type 1 to try the first version of the program")
print("Type 2 to try the second version of the program")
print("Type 3 to try the third version of the program")
print("Type 4 to try the fourth version of the program")
print("Type anything else to exit now")
choice = input("What is your choice? ")
if(choice=='1'):
    test1()
elif(choice=='2'):
    test2()
elif(choice=='3'):
    test3()
elif(choice=='4'):
    test4()

