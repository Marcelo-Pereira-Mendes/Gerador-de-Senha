def transformar_chave_para_senha(chave):
    # Mapeia as substituições para cada letra
    substituicoes = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15',
        'R': '#',
        'S': '%',
        'M': '$',
    }

    # Constrói a senha aplicando as substituições
    senha = ''.join(substituicoes.get(letra.upper(), letra) for letra in chave)
    return senha

# Solicita a entrada do usuário
chave = input('Digite a base da sua senha: ')

# Chama a função para transformar a chave em senha
senha = transformar_chave_para_senha(chave)

# Exibe a senha resultante
print(senha)
