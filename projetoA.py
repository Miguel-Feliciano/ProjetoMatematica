import math
import ProblemaFlutuar, ProblemaMola


def main():
    MainMenu()

def MainMenu():

        print("What problem do you want to solve?")
        print("1- Floatation")
        print("2- Springs")

        r = input()

        if (r == "1"):
            ProblemaFlutuar.ProblemaFlutuar()
        elif (r == "2"):
            ProblemaMola.ProblemaMola()
            
            
main()
