salario = float (input ("Informe o valor do seu salário atual: "))

novo = float ( (salario * 10) / 100)
novo2 = float ( (salario * 15) / 100)

if salario > 8250: 
    print("Seu novo salário é: ", salario+novo)

else: 
    print ("Seu novo salário é: ", salario+novo2)
