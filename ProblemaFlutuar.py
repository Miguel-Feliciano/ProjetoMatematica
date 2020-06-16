import math

def ProblemaFlutuar():
    
    # variáveis
        a = float() #aresta do cubo
        m = float()  # massa
        c = float()  # calado
        v = float()  # volume1
        g = float()  # gravidade
        fb = float()  # força buoyancy
        fg = float()  # força gravítica
        od = float()  # object density
        fd = float()  # fluid density

        
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
            
            
            print("Mass is = " + str(m),"(Kg), " + "Object has a Density of = ", str(od),"(Kg/m3), " + "Volume is = " + str(v),"(m3), " 
                  + "Fluid has a Density of " + str(fd),"(Kg/m3), " + "Gravity is " + str(g),"(m/s2)")

            
            fg = m*g
            
            fb = fg/(fd*g)
            
            a = v**(1/3)
            
            c = fb/(a*a)
            
            
           
            print("The Object would float at: " + str(c))
            
            
            print("Press 1 to set new Mass, Press 2 to set new Gravity,Press 3 to set new Fluid Density,\n Press 4 to set new Object Density or Press 5 to set new Volume ")

            novoinput = input()

            if(novoinput == "1"):
                print("New Mass is... ")
                m = float(input())
                v = m/od
            elif(novoinput == "2"):
                print("New Gravity is... ")
                g = float(input())
            elif(novoinput == "3"):
                print("New Fluid Density is... ")
                fd = float(input()) 
            elif(novoinput == "4"):
                print("New Object Density is... ")
                od = float(input())
            elif(novoinput == "5"):
                print("New Volume is... ")
                v = float(input())
                m = od*v
            else:
                print("invalid input.")
                

