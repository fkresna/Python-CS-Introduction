# File: chaos.py
def main ():
    print ("This program illustrates a chaotic function")
    x=eval (input("enter a number between 0 and 1: "))
    y = eval (input("enter a number between 0 and 1: "))
    n = eval(input("enter how many chaos number that you want"))
    print ("index\t"+str(x)+"\t"+str(y))
    for i in range (n):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print(str(i)+"\t"+str(x)+"\t"+str(y))

main()