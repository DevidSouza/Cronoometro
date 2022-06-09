from tkinter import *
from tkinter import ttk

# anchor é para alinhar
# state=disable desativa Entry

cor1 = '#01315e' # azul escuro
cor2 = '#0e0f0f' # preto
cor3 = '#f9f9f9' # branco
cor4 = '#1b59b7' # azul claro
cor5 = '#02a6d8' # azul bebe
cor6 = '#36bc3b' # verde claro

jan = Tk()
jan.title('')
jan.geometry('300x180')
jan.configure(bg=cor2)
jan.resizable(width=False, height=False)
jan.iconbitmap(default='imagens/relogio.ico')

global tempo
global rodando
tempo = '00:00:00'
rodando = False


# criando funções
def iniciar():
    global rodando, zera_botao, pausar_botao, tempo
    global seg, min, hor

    if rodando:
        iniciar_botao.place(x=5000)
        pausar_botao.place(x=65, y=130)
        zera_botao.place(x=165, y=130)

        tela_label['text'] = tempo
        hor, min, seg = map(int, tempo.split(':'))
        seg += 1
        if seg >= 59:
            min += 1
            seg = 0
        if min >= 59:
            hor += 1
            min = 0
        if hor >= 23:
            hor = 0
        hor, min, seg = '0'+str(hor), '0'+str(min), '0'+str(seg)
        tempo = f'{hor[-2:]}:{min[-2:]}:{seg[-2:]}'
        tela_label.after(1000, iniciar)


def rodar():
    global rodando
    rodando = True
    iniciar()


def pausar():
    global pausar_botao, zera_botao, rodando, tempo
    rodando = False

    pausar_botao.place(x=5000)
    retomar_botao.place(x=65)


def continuar():
    global rodando
    rodando = True

    pausar_botao.place(x=65)
    retomar_botao.place(x=5000)

    iniciar()


def zerar():
    global rodando, tempo
    rodando = False

    pausar_botao.place(x=6000)
    zera_botao.place(x=6000)
    retomar_botao.place(x=5000)

    tempo = '00:00:00'
    tela_label['text'] = tempo

    iniciar_botao.place(x=113, y=130)



# criando label
titulo_label = Label(jan, text='Cronômetro', fg=cor4, bg=cor2, font=('Arial 8 bold'))
titulo_label.place(x=8, y=8)

tela_label = Label(jan, text=tempo, fg=cor4, bg=cor2, font=('Times 55 bold'))
tela_label.place(x=15, y=35)

# criando botões
iniciar_botao = Button(jan, command=rodar, text='Iniciar', width=10, height=2, fg=cor4, bg=cor2, relief=RAISED, overrelief=RIDGE)
iniciar_botao.place(x=113, y=130)

pausar_botao = Button(jan, command=pausar, text='Pausar', width=10, height=2, fg=cor4, bg=cor2, relief=RAISED, overrelief=RIDGE)
pausar_botao.place(x=5000, y=130)

retomar_botao = Button(jan, command=continuar, text='Retomar', width=10, height=2, fg=cor4, bg=cor2, relief=RAISED, overrelief=RIDGE)
retomar_botao.place(x=5000, y=130)

zera_botao = Button(jan, command=zerar, text='Zerar', width=10, height=2, fg=cor4, bg=cor2, relief=RAISED, overrelief=RIDGE)
zera_botao.place(x=5000, y=130)

jan.mainloop()
