import math
import sys
print '----------------------------------------------'
print '-    Programa desenvolvido para calcular     -'
print '-         equacoes de segundo grau           -'
print '-           utilizando Bhaskara              -'
print '----------------------------------------------'

a=input ("Digite o A:")
b=input ("Digite o B:")
c=input ("Digite o C:")
d=((b**2)-4*a*c)
if d<0 :
    print ("Valor de delta negativo, raiz impossivel de ser extraida com numeros reais")
    sys.exit()
else : print "Delta vale %s." % d
m1=math.sqrt(d)
x1=(-b+m1)/(2*a)
x2=(-b-m1)/(2*a)
soma=-(b/a)
produto=c/a
print "Raiz aproximada de X1= %s." % x1
print "Raiz aproximada de X2= %s." % x2
print "O calculo da Soma eh igual a= %s." % soma
print "O calculo do produto eh igual a= %s." %produto
