from tkinter import *
from tkinter import ttk
from tkinter import messagebox

alunos = [
    {
        "matricula": 1,
        "nome": "pedro henrique",
        "idade": 29,
        "curso": "JavaScript",
        "novato": False
    }
]

matricula_atual = 1
index = 0

def atualizarTabela() -> None:
    #limpando a tabela
    #get_children() -> retorna as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)

    for aluno in alunos:
        tabela.insert("", END, values=(aluno["matricula"],
                                       aluno["nome"],
                                       aluno["idade"],
                                       aluno["curso"],
                                       aluno["novato"]))


def adicionarAluno() -> None:
    global matricula_atual
    matricula_atual += 1
    nome = textNome.get()
    idade = int(textIdade.get())
    curso = comboCursos.get()
    novato = opcao.get()

    aluno = {
        "matricula": matricula_atual,
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "novato": novato
    }
    messagebox.showinfo("Sucesso!", "Aluno adicionado com sucesso!")
    alunos.append(aluno)

    # limpar os campos
    limparCampos()
    atualizarTabela()
def limparCampos() -> None:
    textNome.delete(0, END)
    textIdade.delete(0, END)
    comboCursos.set("")
    opcao.set(False)

def preecherCampos(event) -> None:
    linha_selecionada = tabela.selection()
    global index
    index = tabela.index(linha_selecionada)
    aluno = alunos[index]
    limparCampos()
    txtMatricula.config(state=NORMAL)
    txtMatricula.insert(END, str(aluno["matricula"]))
    txtMatricula.config(state=DISABLED)
    textNome.insert(END, aluno["nome"])
    textIdade.insert(END, str(aluno["idade"]))
    comboCursos.set(aluno["curso"])




janela = Tk()

janela.title("Alunos - Infinity")
#janela.geometry("800x650")
# ------------------------Texto Topo ------------------------------------
labelTitulo = Label(janela, font="Tahoma 18 bold", text="<-- Menu Cadastro -->", fg="black")
labelTitulo.grid(row=0, column=1, sticky=W)


# -------------------------- Matricula ----------------------------------------
labelMatricula = Label(janela, font="Tahoma 18 bold", text="Matricula:", fg="red")
labelMatricula.grid(row=1, column=0, sticky=W)

txtMatricula = Entry(janela, font="Tahoma 18", width=26, state=DISABLED)
txtMatricula.grid(row=1, column=1)

# -----------------------------Nome--------------------------------------
labelNome = Label(janela, text="Nome:", font="Tahoma 18 bold", fg="red")
labelNome.grid(row=2, column=0, sticky=W)

textNome = Entry(janela, font="Tahoma 18", width=26,)
textNome.grid(row=2, column=1)

# --------------------------- Idade---------------------------------------
labelIdade = Label(janela, text="Idade:", font="Tahoma 18 bold", fg="red")
labelIdade.grid(row=3, column=0, sticky=W)

textIdade = Entry(janela, font="Tahoma 18", width=26,)
textIdade.grid(row=3, column=1)

# ----------------------------- Curso -----------------------------------------
labelCurso = Label(janela, text="Curso", font="Tahoma 18 bold", fg="red")
labelCurso.grid(row=4, column=0, sticky=W)

textCurso = Entry(janela, font="Tahoma 18", width=26,)
textCurso.grid(row=4, column=1)


# -------------------------- Lista Cursos ttk --------------------------------------

cursos = ["JavaScript", "Python", "React", "NodeJs"]
comboCursos = ttk.Combobox(janela, font="Tahoma 18", values=cursos, width=24)
comboCursos.grid(row=4, column=1, )

# -------------------------- Novato ? ttk --------------------------------------

labelNovato = Label(janela, font="Tahoma 18 bold", fg="grey", text="Novato?")
labelNovato.grid(row=5, column=0,sticky=W)

opcao = BooleanVar(value=False)
checkNovato = ttk.Checkbutton(janela, width=26, variable=opcao)
checkNovato.grid(row=5, column=1, sticky=W)

# ------------------------------ Botoes ----------------------------------------
btnAdicionar = Button(janela, text="Adicionar", font="Tahoma 16", fg="white", height=1,
                      bg="green", command=adicionarAluno)
btnAdicionar.grid(row=6, column=0,)

btnEditar = Button(janela, text="Editar", font="Tahoma 16", fg="white", height=1, bg="black")
btnEditar.grid(row=6, column=1,)

btnExcluir = Button(janela, text="Excluir", font="Tahoma 16", fg="white", height=1, bg="red")
btnExcluir.grid(row=6, column=2,)

# -------------------------------- Tabela -----------------------------------
colunas = ["Matricula", "Nome", "Idade", "Curso", "Novato"]
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=110)

tabela.grid(row=7, columnspan=3)
tabela.bind("<ButtonRelease-1>", preecherCampos)




janela.mainloop()