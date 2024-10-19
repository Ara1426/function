def add(m,a):
    return m+a
def subtract(m,a):
    return m-a
def times(m,a):
    return m*a
def divide(m,a):
    return m/a

print("please select an operation")
print("1.add")
print("2.sub")
print("3.times")
print("4.divide")

choise=int(input("enter an option"))
num1=int(input("enter a number"))
num2=int(input("enter a number"))

if choise==1:
    print("additon",add(num1,num2))
elif choise==2:
    print("subtration",subtract(num1,num2))
elif choise==3:
    print("times",times(num1,num2))
elif choise==4:
    print("divion",divide(num1,num2))
else:
    print("invalide choise")

def function1():
    print("hello")

function1()

