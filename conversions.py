
def convertcm(a):
    return a * 0.01


def convertinch(a):
    return a * 2.54


def convertmeter(a):
    return a * 3.2808


print("1 = convert cm to m \n"
      "2 = convert inch to cm\n"
      "3 = convert meters to feet")

ans1 = int(input("Pick the number of what conversion you would like to carry out: "))
usr_input = input("Type the value you want converted: ")
if ans1 == 1:
    print(convertcm(usr_input))
elif ans1 == 2:
    print(convertinch(usr_input))
elif ans1 == 3:
    print(convertmeter(usr_input))
else:
    print("Please input a valid measurement!")