import re
from validate_docbr import CPF

def nome_valido(nome_valido):
    return nome_valido.isalpha()

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def rg_valido(numero_rg):
    return len(numero_rg) == 9

def celular_valido(numero):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,numero)
    return resposta
