import math
import ProblemaFlutuar, ProblemaMola


def main():
    menu()

def menu():

        print("What problem do you want to solve?")
        print("Press 1 to solve Floatation")
        print("Press 2 to solve Springs")

        t = input()

        if (t == "1"):
            ProblemaFlutuar.ProblemaFlutuar()
        elif (t == "2"):
            ProblemaMola.ProblemaMola()
            
            
main()
