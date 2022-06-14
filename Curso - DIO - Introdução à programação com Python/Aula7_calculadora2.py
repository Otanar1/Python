class Calculadora:
#    def __init__(self):
#        pass # como init não pode ficar vazio, "pass" preenche sem informação
        
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao (self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora ()
#print(calculadora.valor_a)
#print(calculadora.valor_b)
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(int(calculadora.divisao(100, 2)))
print(calculadora.multiplicacao(10 ,5))

# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10, 2))