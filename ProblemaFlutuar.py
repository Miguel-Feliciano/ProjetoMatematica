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
           
            m = od*v #calculo da massa
            
            print("Mass is = " + str(m),"(Kg), " + "Object has a Density of = ", str(od),"(Kg/m3), " + "Volume is = " + str(v),"(m3),\n" 
                  + "Fluid has a Density of " + str(fd),"(Kg/m3), " + "Gravity is " + str(g),"(m/s2)")

            
            fg = m*g #calculo da força gravítica
            
            fb = fg/(fd*g) #calculo da força de buoyancy
            
            a = v**(1/3)  #calculo da aresta do cubo
            
            c = fb/(a*a) #calculo do calado
            
            
           
            print("The Object would float at: " + str(c) + " meters")
            
            
            print("Press 1 to set new Mass, Press 2 to set new Gravity, Press 3 to set new Fluid Density,\nPress 4 to set new Object Density, Press 5 to set new Volume or Press 5 to return to the menu")

            novavariavel = input()

            if(novavariavel == "1"):
                print("New Mass is... ")
                m = float(input())
                v = m/od
            elif(novavariavel == "2"):
                print("New Gravity is... ")
                g = float(input())
            elif(novavariavel == "3"):
                print("New Fluid Density is... ")
                fd = float(input()) 
            elif(novavariavel == "4"):
                print("New Object Density is... ")
                od = float(input())
            elif(novavariavel == "5"):
                print("New Volume is... ")
                v = float(input())
                m = od*v
            elif(novavariavel == "6"):
                break
            else:
                print("invalid input.")
                

