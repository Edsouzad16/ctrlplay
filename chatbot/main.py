import ProjetoChatbot as pc

nome_maquina = 'Chatbot'

pc.saudacoes(nome_maquina)

while True:
    texto = pc.recebe_texto()

    resposta = pc.busca_resposta(nome_maquina, texto)

    if pc.exibe_resposta(resposta, nome_maquina) == 'fim':
        break