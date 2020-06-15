import math


def main():
    MainMenu()

def MainMenu():

        print("What problem do you want to solve?")
        print("1- Floatation")
        print("2- Springs")

        r = input()

        if (r == "1"):
            problemaflotuar()
        elif (r == "2"):
            problemamola()

def problemaflotuar():

    # variáveis
        m = float()  # massa
        c = float()  # calado
        v = float()  # volume1
        g = float()  # gravidade
        fb = float()  # força buoyancy
        fg = float()  # força gravítica
        od = float()  # object density
        fd = float()  # fluid density

        print("Insert Mass:")
        m = float(input())
        print("Insert Gravity:")
        g = float(input())
        print("Insert Object Density:")
        od = float(input())
        print("Insert Fluid Density:")
        fd = float(input())
        print("Insert Object Volume")
        v = float(input())
        
        while (True):
            m = od*v
            print(m)
            
            v = m/od
            print(v)
              
            
            print("Object Properties: Mass = " + str(m),"(Kg), " + "Density = ", str(od),"(Kg/m3), " + "Volume = " + str(v)),"(m3)"
            print("Fluid has density of " + str(fd),"(Kg/m3), " + "Gravity is " + str(g),"(m/s2)")

            fg = m*g
            print(fg)

            fb = fg*fd*g
            print(fb)
            
            fg = fb
            
            print("The Object would float at: " + str(fb))
            
            print("1. Set new Mass: ")
            print("2. Set new Gravity: ")
            print("3. Set new Fluid Density: ")
            print("4. Set new Object Density: ")
            print("5. Set new Volume: ")

            response = input()

            if(response == "1"):
                print("New Mass is... ")
                m = float(input())
            elif(response == "2"):
                print("New Gravity is... ")
                g = float(input())
            elif(response == "3"):
                print("New Fluid Density is... ")
                fd = float(input()) 
            elif(response == "4"):
                print("New Object Density is... ")
                od = float(input())
            elif(response == "5"):
                print("New Volume is... ")
                v = float(input())
            else:
                print("invalid input.")
        
def problemamola():
    
    #variaveis
    
        g = float()  # gravidade
        m = float()  # massa
        r = float() # comprimento em repouso
        k = float() # constante da mola
        g = float()  # gravidade
        fg = float() # força gravítica
        l = float() # cumprimento da mola em equilíbrio
    
        print("Insert Gravity: ")
        fg = float(input())
        print("Insert Mass: ")
        m = float(input())
        print("Insert Spring Constant: ")
        k = float(input())
        print("Insert Resting Length: ")
        r = float(input())
        
        while (True):
            
            print("Object Properties: Mass = " + str(m),"(Kg), " + "Gravity is " + str(g),"(m/s2)")
            print("Resting Length = " + str(r),", " + "Spring Constant = " + str(k))
        
        
        
        print(fg)
        
        #(fg/k)+cr = l
        print(l)

        
        
        


main()
