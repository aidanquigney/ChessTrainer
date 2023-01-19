import random
import time

intiger1 = 0
intiger2 = 0
combination = ""


numberletter = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

# resets the variables to a random int between 1 and 8. Note the global keyword to reset for the whole script. Creates the combination


def get_ints():
    global intiger1, intiger2, combination
    intiger1 = random.randint(1, 8)  # letter
    intiger2 = random.randint(1, 8)  # number
    combination = numberletter[intiger1] + str(intiger2)
    print(combination)

# tell if any input is odd


def isnumberodd(param):
    if (param % 2) == 0:
        return False
    else:
        return True

# if a square is black, returns true. Uses logic if associated number with letter and let are both even or both odd, square is black


def issquareblack():
    if isnumberodd(intiger1) == True and isnumberodd(intiger2) == True:
        return True
    elif isnumberodd(intiger1) != True and isnumberodd(intiger2) != True:
        return True
    else:
        return False

# Allows the user to input their answer...


def inputfunction():
    print(combination + " b or w")
    userinput = input()
    if userinput == "b" and issquareblack() == True:
        print("well done, heres another")
        time.sleep(2)
        get_ints()
        inputfunction()
    elif userinput == "w" and issquareblack() == False:
        print("well done, heres another")
        time.sleep(2)
        get_ints()
        inputfunction()
    else:
        print("Nope, try again")
        time.sleep(2)
        get_ints()
        inputfunction()


# run both functions
get_ints()
inputfunction()
