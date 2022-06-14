
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
#    x = a

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
except:
    print('Erro desconhecido')

else:
    print('Executa quando não ocorrer nenhuma exceção')

finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
    print('Arquivo fechado')
