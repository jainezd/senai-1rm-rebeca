

def somar(num1, num2):
    total = num1 + num2
    return total

def multiplicar(num1, num2):
    total = num1 * num2
    return total 

def maior (num1, num2):
    total = num1, num2
    return max(total)

def menor (num1, num2):
    total = num1, num2
    return min (total)

    
escolha = int(input('[1] somar [2] multiplicar [3] Maior número [4] Menor número: '))

num1 = float (input("Primeiro valor: "))
num2 = float (input("Segundo valor: "))

if escolha == 1:
    print(somar(num1, num2))
elif escolha == 2:
    print(multiplicar(num1, num2))
elif escolha == 3:
    print(maior (num1, num2))
elif escolha == 4:
    print(menor (num1, num2))


#print('Informe um número')

#soma = num1 + num2 

#multiplicar = num1 * num2 

