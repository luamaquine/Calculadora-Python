from tkinter import *
from tkinter import ttk

cor3 = "#38576b"

janela = Tk()
janela.title("Calculadora")
janela.geometry("300x302")
janela.configure(background="black")

#Criando Frames

frame_tela = Frame(janela, width=300, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=300)
frame_corpo.grid(row=1, column=0)

#variavel todos valores

todos_valores = ''

#criando funcao

def entrada_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores)

def resultado():

    global todos_valores
    resultado_final = eval(todos_valores)
    valor_texto.set(str(resultado_final))

def limpar():

    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#Criando Label

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable = valor_texto, width=20, height=2, padx=7, anchor="e", fg="white", font=('Ivy 18'), justify=RIGHT, bg=cor3)
app_label.place(x=0, y=0)

#Criando botoes

bt1 = Button(frame_corpo,command=limpar, text="C", width=16, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0, y=0)

bt2 = Button(frame_corpo, command=lambda: entrada_valores('%'), text="%", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt2.place(x=150, y=0)

bt3 = Button(frame_corpo, command=lambda: entrada_valores('/'), text="/", width=7, height=2, bg="orange", fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt3.place(x=230, y=0)

bt4 = Button(frame_corpo, command=lambda: entrada_valores('7'), text="7", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=0, y=50)

bt5 = Button(frame_corpo, command=lambda: entrada_valores('8'), text="8", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=75, y=50)

bt6 = Button(frame_corpo, command=lambda: entrada_valores('9'), text="9", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=150, y=50)

bt7 = Button(frame_corpo, command=lambda: entrada_valores('*'), text="*", width=7, height=2, bg="orange", fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=230, y=50)

bt8 = Button(frame_corpo, command=lambda: entrada_valores('4'), text="4", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt8.place(x=0, y=100)

bt9 = Button(frame_corpo, command=lambda: entrada_valores('5'), text="5", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt9.place(x=75, y=100)

bt10 = Button(frame_corpo, command=lambda: entrada_valores('6'), text="6", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt10.place(x=150, y=100)

bt11 = Button(frame_corpo, command=lambda: entrada_valores('-'), text="-", width=7, height=2, bg="orange", fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt11.place(x=230, y=100)

bt12 = Button(frame_corpo, command=lambda: entrada_valores('1'), text="1", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt12.place(x=0, y=150)

bt13 = Button(frame_corpo, command=lambda: entrada_valores('2'), text="2", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt13.place(x=75, y=150)

bt14 = Button(frame_corpo, command=lambda: entrada_valores('3'), text="3", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt14.place(x=150, y=150)

bt15 = Button(frame_corpo, command=lambda: entrada_valores('+'), text="+", width=7, height=2, bg="orange", fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt15.place(x=230, y=150)

bt16 = Button(frame_corpo, command=lambda: entrada_valores('0'), text="0", width=16, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt16.place(x=0, y=200)

bt17 = Button(frame_corpo, command=lambda: entrada_valores(','), text=",", width=7, height=2, bg="gray", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt17.place(x=150, y=200)

bt18 = Button(frame_corpo, command = resultado, text="=", width=7, height=2, bg="orange", fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt18.place(x=230, y=200)


janela.mainloop()  