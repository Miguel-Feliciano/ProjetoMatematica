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
            
            print("Mass is " + str(m),"Kg, " + "Gravity is " + str(g),"m/s2, " + 
                  "Resting Length is " + str(r),"m, " + "Spring Constant is " + str(k), "N/m")
        
            fg = m*g #calculo da força gravítica
            
            h = (-k *(-r)) + (-fg) #calculo auxiliar para simplificar a formula
           
            l = h/k #calculo do cumprimento em equilibro
            
            
            print("Spring would stretch to " + str(l) + " meters")
        
           
            
            
          
            print("Press 1 to set new Gravity, Press 2 to set new Mass, Press 3 to set new Spring Constant,\n Press 4 to set new Resting Length or Press 5 to return to the menu")

            novavariavel = input()

            if(novavariavel == "1"):
                print("New Gravity is... ")
                g = float(input())
            elif(novavariavel == "2"):
                print("New Mass is... ")
                m = float(input())
            elif(novavariavel == "3"):
                print("New Spring Constan is... ")
                k = float(input()) 
            elif(novavariavel == "4"):
                print("New Resting Length is... ")
                r = float(input())
            elif(novavariavel == "5"):
                break
                
            
            else:
                print("invalid input.")


