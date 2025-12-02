import tkinter as tk
import ProjetoChatbot as pc

#criando a janela princ

main_window = tk.Tk()

#dando um titulo

main_window.title('ChatBot | CTRL+PLAY')

#tamanho da janela

main_window.geometry('500x700')

#inserindo a janela na grade

main_window.grid()

#criando frame dentro da main window

frame = tk.Frame(main_window)

#inserindo  o frame na grade

frame.grid

#criando um label dentro do frame com una mensagem de instrucao para o usuario

l_indentif = tk.Label(frame)
l_indentif.grid(row=0, column=0)

#criar input

e_mensagem = tk.Entry(frame)
e_mensagem.grid(row=0, column=1)

frame2 = tk.Frame(main_window)
frame2.grid(row=1, column=0)

#variavel armazem

v = tk.StringVar()
tk.Label(frame2, textvariable=v).grid()

nome_maquina = 'ChatBot'
v.set('Seja bem vindo! Qual o seu nome?')
entrada_sujestao = False
enrtrada_nome_usuario = False
nome_usuario = ''

def roda_ChatBot():
    global entrada_sujestao
    global entrada_nome_usuario
    global nome_usuario
    global hisorico_conversa

    hisorico_conversa = v.get()


    if entrada_nome_usuario:
        nome_usuario= e_mensagem.get()
        saudacao = pc.saudacao_GUI(nome_maquina)
        v.set(hisorico_conversa)
        enrtrada_nome_usuario = False

    else:
        texto = e_mensagem.get()
        hisorico_conversa += '\n' + nome_usuario + ': ' + texto
        v.set(hisorico_conversa)

        if entrada_sujestao:
            pc.salvar_sugestao(texto)
            entrada_sujestao = False
            historico_conversa += '\n' + '\n Obrigado pela sugestão!'
            v.set(historico_conversa)

        else:
            resposta = pc.busca_resposta_GUI('Cliente: ' + texto + '\n')
            
            if resposta == 'Desculpe, não sei o que falar...':
                historico_conversa += '\n Me desculpe, não sei o que falar... o que voce esperava? \n'
                v.set(historico_conversa)
                entrada_sujestao = True
            else:
                historico_conversa += '\n' + pc.exibe_resposta_GUI(texto, resposta, nome_maquina)
                v.set(historico_conversa)

#criando botao de enviar mensagem
b_enviar = tk.Button(frame, text='Enviar', command=roda_ChatBot)
b_enviar.grid(row=0, column=2)

main_window.mainloop()
