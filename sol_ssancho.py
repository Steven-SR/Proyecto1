''' -Dominio:
   Dos numeros naturales, Cϵ[1,20] y Rϵ[1,5]
   -Codominio:
   Todos los pares de números que tengan como cociente al dividirse C
   y además cada digito aparece un máximo de R veces
'''
def busca_nums(C,R):        
    print(C,R)
    for a in range (1000,100000):
        b=a*C
        if b>100000:
            break
        if b<10000:
            n=b*1000000+a
        else:
            n=b*100000+a
        if ocurre(str(n),R):
            print(f"{b}/{a}={C}")
''' -Dominio:
   Un stirng compuesto de los digitos de ambos números
   y R el maximo numero de repeticiones
   -Codominio:
   Verdadero si cada digito aparece menos de R veces
   Falso si alguno aparece más de R veces
'''
def ocurre(n,R):
    for num in range(10):
        i=n.count(str(num))
        if i>R:
            return False
    return True

def inputs():
    T=int(input())
    for i in range(T):
        c,r=input().split()
        busca_nums(int(c),int(r))



inputs()
