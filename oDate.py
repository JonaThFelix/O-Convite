from tkinter import  *
import tkinter as tk
import tkinter.messagebox
import random

# layout geral da aplicação
root = tk.Tk()
root.geometry('300x300') 
root.title('Em busca da Pequena')
root.configure(background='pink')

def houver(event):
    x = random.randint(0,200)
    y = random.randint(0,200)
    nao.place(x=x,y=y)

def onClick(): 
    tk.messagebox.showinfo("John Diz...",  "Ótimo, Agora é comigo !!!")
    

# título
pergunta = tk.Label(root, text="Quando vamos sair?")
pergunta.pack(anchor='n', padx=20)
pergunta.place(x=80,y=20)


# configuração dos botões
nao = tk.Button(root, text="Não Sei",bg="red",fg="yellow")
nao.place(x=180, y=100)
nao.bind("<Enter>", houver)

sim = tk.Button(root, text="Quando vc quiser",command=onClick)
sim.place(x=50, y=100) 

root.mainloop()
