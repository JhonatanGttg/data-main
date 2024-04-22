import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class DataManipulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Manipulador de Dados")
        
        # Criar botão para upload de arquivo
        self.upload_button = ttk.Button(root, text="Carregar Arquivo", command=self.upload_file)
        self.upload_button.pack()
        
        # Inicializar variável para armazenar o DataFrame
        self.df = None
        
        # Inicializar variáveis para armazenar widgets
        self.columns_combobox = None
        self.output_text = None
    
    def upload_file(self):
        # Abrir janela de diálogo para seleção de arquivo
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        
        # Verificar se o usuário selecionou um arquivo
        if file_path:
            # Carregar arquivo CSV
            self.df = pd.read_csv(file_path)
            
            # Criar a caixa de seleção de colunas
            self.create_widgets()
    
    def create_widgets(self):
        # Remover botão de upload, se existir
        if self.upload_button:
            self.upload_button.pack_forget()
        
        # Criar a caixa de seleção de colunas
        self.column_label = ttk.Label(self.root, text="Selecione a(s) coluna(s):")
        self.column_label.pack()
        
        self.columns_combobox = ttk.Combobox(self.root, values=self.df.columns.tolist(), state="readonly", width=30)
        self.columns_combobox.pack()
        
        # Botão para exibir os dados
        self.show_button = ttk.Button(self.root, text="Exibir Dados", command=self.display_data)
        self.show_button.pack()
        
        # Texto para exibir os dados
        self.output_text = tk.Text(self.root, height=20, width=50)
        self.output_text.pack()
    
    def display_data(self):
        # Limpar o texto antes de exibir novos dados
        self.output_text.delete('1.0', tk.END)
        
        # Obter as colunas selecionadas
        selected_columns = self.columns_combobox.get().split(', ')
        
        # Verificar se as colunas selecionadas existem no DataFrame
        for col in selected_columns:
            if col not in self.df.columns:
                tk.messagebox.showerror("Erro", f"A coluna '{col}' não existe no arquivo CSV.")
                return
        
        # Exibir os dados das colunas selecionadas
        if len(selected_columns) == 1:
            self.output_text.insert(tk.END, self.df[selected_columns[0]].to_string(index=False))
        else:
            self.output_text.insert(tk.END, self.df[selected_columns].to_string(index=False))
        

root = tk.Tk()
app = DataManipulator(root)
root.mainloop()
