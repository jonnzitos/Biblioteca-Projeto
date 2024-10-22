from tkinter .ttk import *
from tkinter import *
from tkinter import Tk,ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date
from datetime import datetime

#importando funcoes view
from view import *

co1 = "#b0b0b0" #cinza claro
co2 = "#1c1c1c" #cinza escuro 
co3 = "#202021" #cinza 
co6 = "#DCDCDC" #branco 

hoje = datetime.today

#criando janela
janela = Tk()
janela.title("")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=TRUE, height=TRUE)
janela.iconbitmap('logo.ico')
janela.title('Gerenciador de Biblioteca')

style = Style(janela)
style.theme_use("clam")





#frames

logo = Frame(janela, width=770, height=50, bg=co2, relief="flat")
logo.grid(row=0, column=0, columnspan=2, sticky=NSEW)

esquerda = Frame(janela, width=150, height=265, bg=co3, relief="solid")
esquerda.grid(row=1, column=0, sticky=NSEW)

direita = Frame(janela, width=600, height=330, bg=co1, relief="raised")
direita.grid(row=1, column=1, sticky=NSEW)

#logo
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(logo, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW,  bg=co2, fg=co1)
app_logo.place(x=5, y=0)

app_texto = Label(logo, text="ECIT CRISTIANO CARTAXO", compound=LEFT, padx=5, anchor=NW, font=('Verdana 18 bold'), bg=co2, fg=co6)
app_texto.place(x=50, y=7)

app_linha = Label(logo, width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 18 bold'), bg=co6, fg=co6)
app_linha.place(x=0, y=47)

#menu

#usuario
img_user = Image.open('user.png')
img_user = img_user.resize((18,18))
img_user = ImageTk.PhotoImage(img_user)
b_user = Button(esquerda, command=lambda:control('novo_usuario') , image=img_user, compound=LEFT, anchor=NW, text=' Cadastrar Aluno', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

#livro
img_livro = Image.open('livro.png')
img_livro = img_livro.resize((18,18))
img_livro = ImageTk.PhotoImage(img_livro)
b_livro = Button(esquerda, command=lambda:control('novo_livro') ,image=img_livro, compound=LEFT, anchor=NW, text=' Cadastrar Livro', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

#ver livros
img_livro1 = Image.open('livro1.png')
img_livro1 = img_livro1.resize((18,18))
img_livro1 = ImageTk.PhotoImage(img_livro1)
b_livro1 = Button(esquerda, command=lambda:control('ver_livros') , image=img_livro1, compound=LEFT, anchor=NW, text=' Exibir todos os Livros', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livro1.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

#ver usuarios
img_user1 = Image.open('user1.png')
img_user1 = img_user1.resize((18,18))
img_user1 = ImageTk.PhotoImage(img_user1)
b_user1 = Button(esquerda, command=lambda:control('ver_usuarios'), image=img_user1, compound=LEFT, anchor=NW, text=' Exibir todos os Alunos', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_user1.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

#emprestimo
img_emprestimo = Image.open('emprestimo.png')
img_emprestimo = img_emprestimo.resize((18,18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(esquerda, command=lambda:control('emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=' Alugar Livro', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

#devolver emprestimo
img_devolver = Image.open('devolver.png')
img_devolver = img_devolver.resize((18,18))
img_devolver = ImageTk.PhotoImage(img_devolver)
b_devolver = Button(esquerda, command=lambda:control('devolver'), image=img_devolver, compound=LEFT, anchor=NW, text=' Devolver Livro', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolver.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

#livros emprestados
img_emprestados = Image.open('emprestados.png')
img_emprestados = img_emprestados.resize((18,18))
img_emprestados = ImageTk.PhotoImage(img_emprestados)
b_emprestados = Button(esquerda, command=lambda:control('ver_emprestimos'), image=img_emprestados, compound=LEFT, anchor=NW, text=' Livros Alugados', bg=co2, fg=co6, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

#user
def novo_usuario():

    global img_salvar

    def add():
        nome = enome.get()
        sobrenome = esobrenome.get()
        telefone = etelefone.get()

        list = [nome, sobrenome, telefone]

        #verificando NULL
        for i in list:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        #inserir dados no bdd
        insert_user(nome, sobrenome, telefone)

        messagebox.showinfo('Sucesso', 'Usuario Cadastrado com Sucesso')

        #limpando dados preenchidos
        enome.delete(0,END)
        esobrenome.delete(0,END)
        etelefone.delete(0,END)

    app_ = Label(direita, text="Cadastrar Novo Aluno", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co6, fg=co6)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    
    lnome = Label(direita, text="Nome", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lnome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    enome = Entry(direita, width=25, justify='left', relief='solid')
    enome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    lsobrenome = Label(direita, text="Sobrenome", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lsobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    esobrenome = Entry(direita, width=25, justify='left', relief='solid')
    esobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    ltelefone = Label(direita, text="Telefone", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    ltelefone.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    etelefone = Entry(direita, width=25, justify='left', relief='solid')
    etelefone.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    #botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(direita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co2, fg=co6, font=('Ivy 11 bold'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)

    #ver usuarios
def ver_usuarios():

    app_ = Label(direita,text="Alunos Cadastrados",width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(direita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_users()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Nome', 'Sobrenome', 'Telefone']
    
    global tree

    tree = ttk.Treeview(direita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(direita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#livro
def novo_livro():
    
    global img_salvar

    def add():
        
        title = etitulo.get()
        author = eautor.get()
        gender = egenero.get()

        list = [title, author, gender]

         #verificando NULL
        for i in list:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        #inserir dados no bdd
        insert_book(title, author, gender)

        messagebox.showinfo('Sucesso', 'Livro Cadastrado com Sucesso')

        #limpando dados preenchidos
        etitulo.delete(0,END)
        eautor.delete(0,END)
        egenero.delete(0,END)

    app_ = Label(direita, text="Cadastrar Novo Livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co6, fg=co6)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    ltitulo = Label(direita, text="Titulo", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    ltitulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    etitulo = Entry(direita, width=25, justify='left', relief='solid')
    etitulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    lautor = Label(direita, text="Autor", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lautor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    eautor = Entry(direita, width=25, justify='left', relief='solid')
    eautor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    lgenero = Label(direita, text="Genero", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lgenero.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    egenero = Entry(direita, width=25, justify='left', relief='solid')
    egenero.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    #botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(direita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co2, fg=co6, font=('Ivy 11 bold'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)
def ver_livros():
    # Título da seção
    app_ = Label(direita, text="Livros Cadastrados", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    # Linha de separação
    app_linha = Label(direita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Dados dos livros
    dados = get_books()

    # Cabeçalhos das colunas
    list_header = ['ID', 'Titulo', 'Autor', 'Genero']
    
    global tree

    # Configuração do TreeView
    tree = ttk.Treeview(direita, selectmode="extended", columns=list_header, show="headings")

    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(direita, orient="vertical", command=tree.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posicionamento do TreeView e das barras de rolagem
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    direita.grid_rowconfigure(0, weight=12)

    # Configuração das colunas
    hd = ["nw", "nw", "nw", "nw"]
    h = [40, 150, 150, 100]  # Tamanho ajustado das colunas
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])  # Ajuste de largura das colunas
        n += 1

    # Inserção de dados no TreeView
    for item in dados:
        tree.insert('', 'end', values=item)

#emprestimo
def emprestimo():
    
    global img_salvar

    def add():
        
        iduser = eid_user.get()
        idlivro = eid_livro.get()

        list = [iduser, idlivro]

         #verificando NULL
        for i in list:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        #inserir dados no bdd
        insert_loan(iduser, idlivro, None, None)

        messagebox.showinfo('Sucesso', 'Aluguel realizado com Sucesso')

        #limpando dados preenchidos
        eid_user.delete(0,END)
        eid_livro.delete(0,END)

    app_ = Label(direita, text="Realizar novo Aluguel", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co6, fg=co6)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    lid_user = Label(direita, text="ID do Usuario", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lid_user.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    eid_user = Entry(direita, width=25, justify='left', relief='solid')
    eid_user.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    
    lid_livro = Label(direita, text="ID do Livro", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lid_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    eid_livro = Entry(direita, width=25, justify='left', relief='solid')
    eid_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(direita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co2, fg=co6, font=('Ivy 11 bold'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)
def ver_emprestimos():
    # Título da seção
    app_ = Label(direita, text="Livros Alugados", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    # Linha de separação
    app_linha = Label(direita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Dados dos livros
    dados = []

    books_on_loan = get_books_on_loan()

    for book in books_on_loan:
        dado = [f"{book[3]}", f"{book[0]}", f"{book[1]} {book[2]}", f"{book[4]}", f"{book[5]}" ]

        dados.append(dado)
    
                # Cabeçalhos das colunas
    list_header = ['ID', 'Titulo', 'Nome do Usuario', 'Data de Emprestimo','Data de Devolucao']
    
    global tree

    # Configuração do TreeView
    tree = ttk.Treeview(direita, selectmode="extended", columns=list_header, show="headings")

    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(direita, orient="vertical", command=tree.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posicionamento do TreeView e das barras de rolagem
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    direita.grid_rowconfigure(0, weight=12)

    # Configuração das colunas
    hd = ["nw", "nw", "ne", "ne" , "ne", "ne",]
    h = [20, 135, 120, 102, 100]  # Tamanho ajustado das colunas
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])  # Ajuste de largura das colunas
        n += 1

    # Inserção de dados no TreeView
    for item in dados:
        tree.insert('', 'end', values=item)
def devolver():
   
    global img_salvar

    def add():
        
        load_id = eid_emprestimo.get()
        data = edevolucao.get()

        list = [load_id, data]

         #verificando NULL
        for i in list:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        #inserir dados no bdd
        update_loan_return_date(load_id, data)

        messagebox.showinfo('Sucesso', 'Livro devolvido com Sucesso')

        #limpando dados preenchidos
        eid_emprestimo.delete(0,END)
        edevolucao.delete(0,END)

    app_ = Label(direita, text="Devolucao de Livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co3, fg=co6)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co6, fg=co6)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    lid_emprestimo = Label(direita, text="ID do Emprestimo", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    lid_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    eid_emprestimo = Entry(direita, width=25, justify='left', relief='solid')
    eid_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    
    ldevolucao = Label(direita, text="Data de Devolucao (AAAA-MM-DD)*", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co6)
    ldevolucao.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    edevolucao = Entry(direita, width=25, justify='left', relief='solid')
    edevolucao.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(direita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co2, fg=co6, font=('Ivy 11 bold'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)


#controlar menu
def control(i):
    
    #novo user
    if i == 'novo_usuario':
        for widget in direita.winfo_children():
            widget.destroy()
        novo_usuario()

    #ver users
    if i == 'ver_usuarios':
        for widget in direita.winfo_children():
            widget.destroy()
        ver_usuarios()

    #novo livro
    if i == 'novo_livro':
        for widget in direita.winfo_children():
            widget.destroy()
        novo_livro()
    
    #ver livros
    if i == 'ver_livros':
        for widget in direita.winfo_children():
            widget.destroy()
            ver_livros()

    #alugar
    if i == 'emprestimo':
        for widget in direita.winfo_children():
            widget.destroy()
            emprestimo()

    #ver alugados
    if i == 'ver_emprestimos':
        for widget in direita.winfo_children():
            widget.destroy()
            ver_emprestimos()
    
    #devolver
    if i == 'devolver':
        for widget in direita.winfo_children():
            widget.destroy()
            devolver()

janela.mainloop()
