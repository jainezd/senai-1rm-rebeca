def maior (num1, num2, num3):
    if num1 > num2 and num3:
        print(num1, "É o maior")
    if num2 > num1 and num3:
         print(num2,"É o maior ")
    if num3 > num1 and num2:
         print(num3,"É o maior ")

    return (".")
num1 = int (input ('Informe o primeiro número: '))
num2 = int (input ('Informe o segundo número: '))
num3 = int (input ('Informe o terceiro número: '))

print(maior(num1, num2, num3))
 
         
