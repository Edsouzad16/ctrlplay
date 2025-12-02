import random

def saudacoes_GUI(nome):
    frases = [
        f'Boa tarde! Meu nome é {nome}. Como vai?',
        'Olá tudo bem?',
        'Tudo certo?'
    ]
    return frases[random.randint(0,2)]

def recebe_texto_GUI():
    texto = 'Cliente: ' + input('Cliente: ')
    palavras_proibidas = ['Bocó']

    for p in palavras_proibidas:
        if p in texto:
            print('Me respeite!!')
            return recebe_texto_GUI
        
        return texto
    
def busca_resposta_GUI(nome, texto):
    with open('dados.txt', 'a+') as conhecimento:
        conhecimento.seek(0)

        while True:
            viu = conhecimento.readline()

            if viu != '':
                if texto.replace('Cliente: ', '') == 'Tchau':
                    print(nome + ':Volte sempre!')
                    return 'fim'
                
                elif viu.strip() == texto.strip():
                    proxima_linha = conhecimento.readline()

                    if 'Chatbot: ' in proxima_linha:
                        return proxima_linha
            else:
                print('Desculpe, não sei o que falar...')
                conhecimento.write('\n' + texto)
                resposta_usuario = input('O que você esperava? \n')
                conhecimento.write('\n' + 'Chatbot: ' + resposta_usuario)
                return 'Hum...'

def exibe_resposta_GUI(resposta, nome):
    print(resposta.replace('Chatbot' , nome))

    if resposta == 'fim':
        return 'fim'
    return 'continua'

def salvar_sugestao(sugestao):
    with open('dados.txt' + 'a') as conhecimento:
        conhecimento.write('Chatbot: ' + sugestao + '\n')

def busca_resposta_GUI(texto):
    with open('dados.txt', 'a+') as conhecimento:
        conhecimento.seek(0)

        while True:
            viu = conhecimento.readline()

            if viu != '':
                if jaccard(texto, viu) >= 0.3:
                    proxima_linha = conhecimento.readline()

                    if 'Chatbot: ' in proxima_linha:
                        return proxima_linha
            else:
                conhecimento.write(texto)
                resposta_usuario = input('Me desculpe, nao sei o que falar... \n')

def jaccard(texto_usuario, texto_base):
    texto_usuario = limpa_texto(texto_usuario)
    texto_base = limpa_texto(texto_base)
    if len(texto_base) <1: return 0

    else:
        palavras_em_comum = 0
        for palavra in texto_usuario.split():
            if palavra in texto_base.split():
                palavras_em_comum += 1
        return palavras_em_comum / (len(texto_base.split()))

def limpa_texto(texto):
    texto = texto.lower()
    simbolos = [',', '.', '!', '?', ';', ':']

    for s in simbolos:
        texto = texto.replace(s, '')

    return texto