import math

def ProblemaMola():
    
    #variaveis
    
        g = float()  # gravidade
        m = float()  # massa
        r = float() # comprimento em repouso
        k = float() # constante da mola
        g = float()  # gravidade
        fg = float() # força gravítica
        l = float() # cumprimento da mola em equilíbrio
       
        
        print("Insert Gravity: ")
        g = float(input())
        print("Insert Mass: ")
        m = float(input())
        print("Insert Spring Constant: ")
        k = float(input())
        print("Insert Resting Length: ")
        r = float(input())
        
        while (True):
            
            print("Mass = " + str(m),"Kg, " + "Gravity is " + str(g),"m/s2, " + 
                  "Resting Length = " + str(r),"m, " + "Spring Constant = " + str(k), "N/m")
        
            fg = m*g
            
            h = (-k *(-r)) + (-fg)
           
            l = h/k
            
            
            print("Spring would stretch to" + str(l) + "(m)")
        
            print("Press 1 to set new Gravity: ")
            print("Press 2 to set new Mass: ")
            print("Press 3 to set new Spring Constant: ")
            print("Press 4 to set new Resting Length: ")
            

            novoinput = input()

            if(novoinput == "1"):
                print("New Gravity is... ")
                g = float(input())
            elif(novoinput == "2"):
                print("New Mass is... ")
                m = float(input())
            elif(novoinput == "3"):
                print("New Spring Constan is... ")
                k = float(input()) 
            elif(novoinput == "4"):
                print("New Resting Length is... ")
                r = float(input())
            
            else:
                print("invalid input.")


