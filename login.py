import customtkinter as ctk
from tkinter import *
from tkinter import messagebox


janela = ctk.CTk()


class Application_login():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()


    #Cor do sitema
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")


    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.iconbitmap("o-email.ico")
        janela.resizable(False,False)


    def tela_login(self):
        #carrega a foto
        img = PhotoImage(file="auto email.png")
        label_img = ctk.CTkLabel(master=janela, image=img)
        label_img.place(x=1, y=3)

        # TESTE IMAGEM COM BUTTON
        #img = PhotoImage(file="auto email.png")
        #label_img = ctk.CTkButton(master=janela, image=img, text=None, hover=None, fg_color=None)
        #label_img.place(x=1, y=3)

        # criação do frame
        login_frame = ctk.CTkFrame(master=janela, width=260, height=396)
        login_frame.pack(side=RIGHT)

        #Mensagem de "bem vindo no inicio"
        label = ctk.CTkLabel(master=login_frame, text='Faça o Login', font = ('Roboto', 20, 'bold'), text_color= ('white') )
        label.place(x=20, y=25)

        #campo do email
        email = ctk.CTkEntry(master=login_frame, placeholder_text= "Username", width =230, font=("Roboto", 14))
        email.place(x =20, y=105)

        #colocar a informação embaixo do campo do email
        label1= ctk.CTkLabel(master=login_frame, text="*Insira seu email", text_color="green", font=("Roboto", 12))
        label1.place(x=20, y=135)


        #campo da senha
        senha = ctk.CTkEntry(master=login_frame, placeholder_text= "Password", width =230, font=("Roboto", 14), show="*")
        senha.place(x =20, y=175)

        #colocar a informação embaixo do campo do email
        label2= ctk.CTkLabel(master=login_frame, text="*Insira sua senha", text_color="green", font=("Roboto", 12))
        label2.place(x=20, y=205)

        #botão para lembrar os dados de usuario
        checkbox=ctk.CTkCheckBox(master=login_frame, text="Lembrar-se de mim sempre")
        checkbox.place(x=20,y=235)
        
        #Mensagem para quando realizar o Login
        def login():
            msg = messagebox.showinfo(title="Estado de Login",message="Login Realizado com Sucesso")
            pass

        #botão do login
        botao_login = ctk.CTkButton(master=login_frame, text="Login", width=150, command=login)
        botao_login.place(x=50, y = 285)

        #mensagem botão cadastrar
        msg_cadastrar = ctk.CTkLabel(master=login_frame, text="Se não tem uma conta")
        msg_cadastrar.place(x=20, y=325)

        def tela_cadastro():
            #remover o frame de login
            login_frame.pack_forget()

            #criar tela de cadastro:
            cadastro_frame = ctk.CTkFrame(master=janela, width=260, height=396)
            cadastro_frame.pack(side=RIGHT)

            #Mensagem de cadastra-se 
            label = ctk.CTkLabel(master=cadastro_frame, text='Faça o seu Cadastro', font = ('Roboto', 20, 'bold'), text_color= ('white') )
            label.place(x=20, y=25)

            span =ctk.CTkLabel(master=cadastro_frame, text= "Por favor preecha todos os campos com dados Corretos.", font=("Roboto", 9), text_color="grey")
            span.place(x=25, y=65)

            #campos de preenhcer dados | 1 nome do usuario
            username_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text= "Nome do Usuario", width =230, font=("Roboto", 14))
            username_entry.place(x =20, y=105)
            #email que vai utilizar
            email_cadastro = ctk.CTkEntry(master=cadastro_frame, placeholder_text= "Email", width =230, font=("Roboto", 14))
            email_cadastro.place(x =20, y=145)
             #senha
            senha_cadastro = ctk.CTkEntry(master=cadastro_frame, placeholder_text= "Senha", width =230, font=("Roboto", 14), show="*")
            senha_cadastro.place(x =20, y=185)
             #confirmar senha
            confirm_senha = ctk.CTkEntry(master=cadastro_frame, placeholder_text= "Confirmar Senha", width =230, font=("Roboto", 14), show="*")
            confirm_senha.place(x =20, y=225)

            #chebox para verificar termos
            checkbox_Termos=ctk.CTkCheckBox(master=cadastro_frame, text="Aceito os Termos e Politicas")
            checkbox_Termos.place(x=20,y=265)
            
            #Função para voltar para a tela de login
            def back():
                #removendo o frama de cadastro
                cadastro_frame.pack_forget()
                # devolvendo o frame do login
                login_frame.pack(side=RIGHT)
                

            #botao voltar
            botao_back = ctk.CTkButton(master=cadastro_frame, text="Voltar", width=115,  fg_color= "gray", hover_color="#202020", command=back)
            botao_back.place(x=20, y = 315)

            #mensagem box para quando apertar em salvar e cadastrar o usuario
            def save_user():
                msg = messagebox.showinfo(title="Estado de cadastro", message="Parabens, Usuario Cadastrado com Sucesso.!!")
                pass



            #botao cadastro
            botao_save = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", width=115, 
                                       fg_color= "green" , hover_color="#014B05",command=save_user)
            botao_save.place(x=140, y =315)

            
        #botão de se registrar
        botao_registrar = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=100, fg_color="green", hover_color="#2D9334",command=tela_cadastro)
        botao_registrar.place(x=153, y = 325)



Application_login()
