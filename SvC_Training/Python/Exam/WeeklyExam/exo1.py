from math import sqrt

#cette fonction calcule les racines d'un polynôme de degre 2 à discriminant positif
def afficher_solutions_doubles(a,b,c,delta):
    if delta < 0:
        print("il n'y a pas de solutions réelles")
    elif delta ==0:
        x = -b/(2*a)
        print("il y a une seule solution x= {}".format(x))
    else:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        print("il y a deux solutions réelles: x1= {} et x2= {}".format(x1,x2))
    
        

    

def resolution_eq_du_second_degré(a,b,c):

    #eliminer les mauvais input
    try:
        a,b,c = float(a), float(b), float(c)
    except:
        print ("error: arguments must be integer or float")
        return
    
    #distinguer selon les valeurs de a,b et c
    if(a==0 and b ==0 and c==0):
        print("0 =0 est vérifiée pour tout réel")
    elif(a==0 and b==0 and c!=0):
        print("{} =0 est absurde!".format(c)) 
    elif(a==0 and b!=0):
        x = c/b
        print( "il y a une seule solution x= {}".format(x))
    else:
        delta = b**2 - 4*a*c
        afficher_solutions_doubles(a,b,c,delta)
        
print ("entrer a,b et c")
a = input("entrer a: ")
b = input("entrer b: ")
c = input("entrer c: ")
resolution_eq_du_second_degré(a,b,c)
print( "pour entrer de nouvelles valeurs, utilisez la méthode >>>resolution_eq_du_second_degré(a,b,c)>>>")



      
