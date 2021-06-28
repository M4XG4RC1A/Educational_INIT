import random
import time

print("Welcome to math trainer")
operations = input("Select operations to practice (+,-,*,/): ")
while not(operations=="+" or operations=="-" or operations=="*" or operations=="/"):
    operations = input("Select operations to practice (+,-,*,/): ")
Problems = int(input("Select number of problems: "))
digits = int(input("Select number of max digits: "))

print("\n")

maxD = "9"*digits
Equations = []
Times = []
Result = []
OK = 0;
for i in range(Problems):
    Val1 = random.randint(0,eval(maxD))
    Val2 = random.randint(0,eval(maxD))
    Ec = "{}{}{}".format(str(Val1),operations,str(Val2))
    start = time.time()
    print("Calculate: {}".format(Ec))
    result = int(input("Result:  "))
    end = time.time()
    print("Real Result: {}\n".format(eval(Ec)))
    if result == eval(Ec):
        Result.append(str(result)+" CORRECT")
        OK = OK+1
    else:
        Result.append(str(result)+" INCORRECT")
    Equations.append(Ec)
    Times.append(start-end)

print("Game Over...\n\nResults:")
for i in range(Problems):
    print("{}: Time-{}, {}".format(str(Equations[i]),str(Times[i]),str(Result[i])))
print("\nTotal: {}/{}".format(str(OK),Problems))