import math
import ProblemaFlutuar, ProblemaMola


def main():
    menu()

def menu():

    while (True):
        
        print("What problem do you want to solve?")
        print("Press 1 to solve Floatation")
        print("Press 2 to solve Springs")
        print("Press 3 to exit program")
        

        t = input()

        if (t == "1"):
            ProblemaFlutuar.ProblemaFlutuar()
        elif (t == "2"):
            ProblemaMola.ProblemaMola()
        elif (t == "3"):
            exit()
        
        
            
            
main()
