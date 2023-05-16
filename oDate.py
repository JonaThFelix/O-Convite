from tkinter import  *
import tkinter as tk
import tkinter.messagebox
import random
import customtkinter

# layout geral da aplicação
root = customtkinter.CTk()
root.title('Em busca da Pequena')
largura = 400
altura = 400

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura  / 2

root.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
root._set_appearance_mode('System')
root.resizable(False,False)
root.configure(background='pink')

def houver(event):
    x = random.randint(0,200)
    y = random.randint(0,200)
    nao.place(x=x,y=y)

def onClick(): 
    tk.messagebox.showinfo(" Diz...",  "Ótimo, o resto eu resolvo !!!")


# título
pergunta = customtkinter.CTkLabel(root, text="Quando vamos Sair?")
pergunta.pack(anchor='n', padx=20)
pergunta.place(x=130,y=40)


# configuração dos botões
nao = customtkinter.CTkButton(root, text="Não Sei",text_color='yellow',fg_color="red")
nao.place(x=180, y=100)
nao.bind("<Enter>", houver)

sim = customtkinter.CTkButton(root, text="Quando vc quiser",fg_color='pink',text_color='black', hover_color='#DC143C',command=onClick)
sim.place(x=50, y=100) 

root.mainloop()
