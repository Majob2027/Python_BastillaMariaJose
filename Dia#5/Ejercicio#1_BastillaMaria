#Ejercicio



def pares(t_n,n,k):
    pairs=set()
    for i in range(n):
     for j in range(i+1,n):
         if (t_n[i]+t_n[j]) % k ==0:
             pairs.add((min(t_n[i],t_n[j]))), max (t_n[i],t_n)
         return len(pairs)

t=int(input())
for case in range(t):
    texto=input("")
    numeros=input("")
    n=0
    k=0
    t_n=list()
    textolista=texto.split(" ")
    numerolista=numeros.split("")
    n=int(textolista[0])
    k=int(textolista[1])
    for p in range (n):
        num=int(numerolista[p])
        t_n.append(num)
    result = pares (t_n,n,k)
    print("case{}:{}".format(case+1,result))    
                           
    

      
