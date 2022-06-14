from ast import Mult


a = int(input('Entre com o primeiro valor'))
b = int(input('Entre com o segundo valor'))
soma = a + b
subtração = a - b
multiplicação = a * b
divisão = a / b
resto = a % b
resultado = ('Soma: {soma}'  
      '\nSubtração: {sub}'
      '\nMultiplicação: {mult}'
      '\nDivisão: {div}'
      '\nResto: {resto}'
        .format(soma=soma, 
                sub=subtração,
                mult=multiplicação,
                div=divisão,
                resto=resto))
print(resultado)

# x = '99'
# soma2 = int(x) + 1
# print(soma2)
