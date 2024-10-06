import tkinter as tk
from tkinter import messagebox, simpledialog, font

alunos = []

class Aluno:
    def __init__(self, nome, idade, id, notas):
        self.nome = nome
        self.idade = idade
        self.id = id
        self.notas = notas
    
    def calculo_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0
    
    def status(self):
        media = self.calculo_media()
        return "Aprovado!" if media >= 6 else "Reprovado!"

class Professor:
    def __init__(self, nome, id=None):
        self.nome = nome
        self.id = id

    def adicionar_aluno(self):
        nome = simpledialog.askstring("Adicionar Aluno", "Nome do aluno:")
        idade = simpledialog.askinteger("Adicionar Aluno", "Idade do aluno:")
        id = simpledialog.askinteger("Adicionar Aluno", "ID do aluno:")
        notas_input = simpledialog.askstring("Adicionar Aluno", "Notas (separadas por espaço):")
        notas = list(map(float, notas_input.split())) if notas_input else []
        
        if nome and idade and id:
            aluno = Aluno(nome, idade, id, notas)
            alunos.append(aluno)
            messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")

    def remover_aluno(self):
        nome = simpledialog.askstring("Remover Aluno", "Nome do aluno a ser removido:")
        aluno = next((a for a in alunos if a.nome.lower() == nome.lower()), None)
        
        if aluno:
            alunos.remove(aluno)
            messagebox.showinfo("Sucesso", f"Aluno {nome} removido com sucesso!")
        else:
            messagebox.showwarning("Atenção", f"Aluno {nome} não encontrado.")

    def listar_alunos(self):
        criterio = simpledialog.askstring("Listar Alunos", "Buscar por (nome ou ID):")
        if not criterio:
            return

        filtered_alunos = [a for a in alunos if str(a.nome).lower() == criterio.lower() or str(a.id) == criterio]
        
        if not filtered_alunos:
            messagebox.showinfo("Lista de Alunos", "Nenhum aluno encontrado com esse critério.")
            return
        
        lista = "\n".join([f"Nome: {a.nome}, Idade: {a.idade}, ID: {a.id}, Média: {a.calculo_media():.2f}, Status: {a.status()}" for a in filtered_alunos])
        messagebox.showinfo("Lista de Alunos", lista)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Cadastro de Alunos")
        master.geometry("400x400")
        master.configure(bg="#f0f0f0")

        self.title_font = font.Font(family="Arial", size=16, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)

        self.label = tk.Label(master, text=f'Bem-vindo(a), {self.professor_nome()}', font=self.title_font, bg="#f0f0f0", pady=20)
        self.label.pack()

        self.adicionar_button = tk.Button(master, text="Adicionar Aluno", font=self.button_font, command=self.adicionar_aluno, bg="#4CAF50", fg="white", padx=20, pady=10, borderwidth=2, relief="raised")
        self.adicionar_button.pack(pady=10)

        self.listar_button = tk.Button(master, text="Listar Alunos", font=self.button_font, command=self.listar_alunos, bg="#2196F3", fg="white", padx=20, pady=10, borderwidth=2, relief="raised")
        self.listar_button.pack(pady=10)

        self.remover_button = tk.Button(master, text="Remover Aluno", font=self.button_font, command=self.remover_aluno, bg="#f44336", fg="white", padx=20, pady=10, borderwidth=2, relief="raised")
        self.remover_button.pack(pady=10)

        self.sair_button = tk.Button(master, text="Sair", font=self.button_font, command=master.quit, bg="#808080", fg="white", padx=20, pady=10, borderwidth=2, relief="raised")
        self.sair_button.pack(pady=20)

    def professor_nome(self):
        self.professor = Professor("Professor Exemplo")
        return self.professor.nome

    def adicionar_aluno(self):
        self.professor.adicionar_aluno()

    def listar_alunos(self):
        self.professor.listar_alunos()

    def remover_aluno(self):
        self.professor.remover_aluno()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
