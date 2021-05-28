from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
import math
from main import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        Novo_BD.cria_BD(self)
        Novo.cria(self)
        self.telas()
        self.tela_config()
        self.tela_menu()
        self.tela_create_fisico()
        self.tela_pesquisa()
        
        root.mainloop()
    
    def pesquisa_to_menu(self):
        self.Pesquisa.forget()
        self.Menu.pack(fill='both',expand=1)
    def change_to_ClientType(self):
        self.ClientType.place(relx=0.5, rely=0.5, anchor='c')
        self.Menu.forget()
    def change_to_CreateFisico(self):
        self.CreateFisico.pack(fill='both', expand=1)
        self.Menu.forget()
    def change_to_Pesquisa(self):
        self.Pesquisa.pack(fill='both', expand=1)
        self.Menu.forget()
    def create_to_ClientType(self):
        self.Menu.pack(fill='both', expand=1)
        self.CreateFisico.forget()
    def calendario1(self):
        self.calendar1 = Calendar(self.form, locale="pt_br")
        self.calendar1.place(relx=0.32, rely=0.5)
        self.calDataInicio = Button(self.calendar1, text="Inserir Data", command=self.set_calendario1)
        self.calDataInicio.pack()
    def set_calendario1(self):
        dataIni = self.calendar1.get_date()
        self.calendar1.destroy()
        self.entry_data_inicio.delete(0,END)
        self.entry_data_inicio.insert(END, dataIni)
        self.calDataInicio.destroy()
    def calendario2(self):
        self.calendar2 = Calendar(self.form, locale="pt_br")
        self.calendar2.place(relx=0.52, rely=0.5)
        self.calDataFim = Button(self.calendar2, text="Inserir Data", command=self.set_calendario2)
        self.calDataFim.pack()
    def set_calendario2(self):
        dataFim = self.calendar2.get_date()
        self.calendar2.destroy()
        self.entry_data_fim.delete(0,END)
        self.entry_data_fim.insert(END, dataFim)
        self.calDataFim.destroy()
    def valor_total_check(self,a,b,c):
        try:
            if (self.val_total.get() != ""):
                self.calc_lucro(1,1,1)
                self.message_error.config(text="")
                self.vt_entry.config(bg='white')
                self.print_qnt_par.config(text="{}x".format(int(self.val_qnt_parcelas.get()),monetary=True))

                va_parcelado = round((float(self.val_total.get()) - float(self.val_pago.get()))/(int(self.val_qnt_parcelas.get())),2)
                self.vp_entry.config(text="{:,}".format(va_parcelado))
            
        except ValueError:
            self.vt_entry.config(bg='firebrick1')
            self.message_error.config(text="Utilize apenas números e ponto.")
    def valor_pago_check(self,a,b,c):
        try:
            if (self.val_pago.get() != ""):   
                self.calc_lucro(1,1,1)             
                self.message_error.config(text="")
                self.va_entry.config(bg='white')
                self.print_qnt_par.config(text="{}x".format(int(self.val_qnt_parcelas.get())))
                va_parcelado = round((float(self.val_total.get()) - float(self.val_pago.get()))/(int(self.val_qnt_parcelas.get())),2)
                self.vp_entry.config(text="R${:,}".format(va_parcelado))
            
        except ValueError:
            self.va_entry.config(bg='firebrick1')
            self.message_error.config(text="Utilize apenas números e ponto.")        
    def calc_lucro(self,a,b,c):
        var_luco = round(float(self.val_pago.get()) - float(self.val_pgo_materiais.get()) - float(self.val_pgo_deco.get()) - float(self.val_pgo_mdo.get()),2)
        self.lucro_inst.config(text="R$ {:,}".format(var_luco))
        if var_luco >= 0:
            self.lucro_inst.config(fg='green4')
        else:
            self.lucro_inst.config(fg='red3')
    def tela_config(self):
        self.root.state('zoomed')
        self.root.config(bg='White')
        self.root.geometry('1280x700')
        self.root.minsize(width=1280, height=700)
        self.root.title("OPERAÇÕES ARQUITETURA")
        self.Menu.pack(fill='both',expand='1')

    def insere_projeto(self):
        self.nome = self.nome_entry.get()
        self.cpf = self.cpf_entry.get()
        self.rg = self.rg_entry.get()
        self.tipo_proj = self.var_tipo_proj.get()
        self.met1 = self.entry_met1.get()
        self.met2 = self.entry_met2.get()
        self.met3 = self.entry_met3.get()
        self.data_contratacao = self.entry_data_inicio.get()
        self.data_finalizacao = self.entry_data_fim.get()
        self.valor_total = self.vt_entry.get()
        self.valor_pago = self.va_entry.get()
        self.vencimento_fatura = self.dia_de_vencimento.get()
        self.quantidade_parcelas = self.qnt_parcelas.get()
        self.val_pago_materiais = self.pago_materiais.get()
        self.val_pago_maodeobra = self.pago_obra.get()
        self.val_pago_decoracao = self.pago_decoracao.get()
        self.val_parcelado = self.vp_entry["text"]

        Novo_Projeto.insere_Novo_Projeto(self, self.tipo_proj, self.met1, self.met2, self.met3, self.data_finalizacao, Etapa, self.nome, self.data_contratacao, self.telefone, self.valor_total, self.valor_pago, self.val_parcelado, self.vencimento_fatura, self.quantidade_parcelas, self.val_pago_materiais, self.val_pago_maodeobra, self.val_pago_decoracao)


    def select_projetos(self):
        self.listaCli.delete(*self.listaCli.get_children())
        lista = Ler_Projeto.leia_proj(self)
        for i in lista or []:
            self.listaCli.insert("",END, values=i)
        
    def telas(self):
        self.Menu = Frame(self.root)
        self.Menu.configure(bg='White')
        self.CreateFisico = Frame(self.root)
        self.CreateFisico.configure(bg='White')
        self.Pesquisa = Frame(self.root)
        self.Pesquisa.configure(bg='White')

    def tela_menu(self):
        self.logo = ImageTk.PhotoImage(Image.open("src/logo.jpeg"))
        self.menu_frame = LabelFrame(self.Menu, borderwidth = 0)
        self.menu_frame.config(bg='White')
        self.menu_frame.pack(fill='both', expand=1)
        self.logo_menu = Label(self.menu_frame, image=self.logo, bg='white')
        self.logo_menu.place(relx=0.32, rely=0)
        self.btn_create = Button(self.menu_frame,text='Novo Projeto',command=self.change_to_CreateFisico, height=5, width=55, bg='white')
        self.btn_create.place(relx=0.4, rely=0.50, relwidth=0.2)
        self.btn_read = Button(self.menu_frame,text='Ver Projetos',command=self.change_to_Pesquisa,height=5, width=55, bg='white')
        self.btn_read.place(relx=0.4,rely=0.65, relwidth=0.2)

    def tela_create_fisico(self):
        self.header = LabelFrame(self.CreateFisico, borderwidth = 2)
        self.header.config(bg='white')
        self.header.place(relx=0.5, rely=0.02, anchor='c',relwidth=1, relheight=0.05)

        Button(self.header, text='Voltar', command=self.create_to_ClientType, bg='white').place(relx=0, rely=0, relheight=1)
        Label(self.header, text='Sistema de Arquitetura', bg='white').place(relx=0.43, rely=0, relheight=1)

        #form frame
        self.form = LabelFrame(self.CreateFisico, borderwidth = 0)
        self.form.config(bg='white')
        self.form.place(relx=0, rely=0.045, relwidth=1, relheight=1)

        Label(self.CreateFisico, image=self.logo, bg='white').place(relx=0.32, rely=0.115, relheight=0.2)

        # Dados dos Clientes
        self.lb_nome = Label(self.form,text="Nome:", bg='white')
        self.lb_nome.place(relx=0.2, rely=0.35)
        self.nome_entry = Entry(self.form, font=('Arial',10))
        self.nome_entry.place(relx=0.24, rely=0.35, relwidth=0.5)
        
        self.cpf = Label(self.form, text="CPF/CNPJ:", bg='white')
        self.cpf.place(relx=0.2, rely=0.4)
        self.cpf_entry = Entry(self.form, font=('Arial',10))
        self.cpf_entry.place(relx=0.245, rely=0.4)

        self.rg = Label(self.form, text='RG:', bg='white')
        self.rg.place(relx=0.355, rely=0.4)
        self.rg_entry = Entry(self.form, font=('Arial',10))
        self.rg_entry.place(relx=0.375, rely=0.4)

        # tipos de construção
        self.var_tipo_proj = IntVar()
        self.tipo = Label(self.form, text="Tipo de Projeto:", bg='white')
        self.tipo.place(relx=0.5, rely=0.4)
        self.reforma = Radiobutton(self.form, text='Reforma', variable=self.var_tipo_proj,value=1, bg='white')
        self.reforma.place(relx=0.56, rely=0.4)
        self.construcao = Radiobutton(self.form, text='Nova Construção', variable=self.var_tipo_proj, value=2, bg='white')
        self.construcao.place(relx=0.62, rely=0.4)

        # Metragens
        self.lb_met1 = Label(self.form, text='Metragem 1:', bg='white')
        self.lb_met1.place(relx=0.2, rely=0.45)
        self.entry_met1 = Entry(self.form, font=('Arial',10))
        self.entry_met1.place(relx=0.255,rely=0.45, width=100)

        self.lb_met2 = Label(self.form, text='Metragem 2:', bg='white')
        self.lb_met2.place(relx=0.4, rely=0.45)
        self.entry_met2 = Entry(self.form, font=('Arial',10))
        self.entry_met2.place(relx=0.455,rely=0.45, width=100)

        self.lb_met3 = Label(self.form, text='Metragem 3:', bg='white')
        self.lb_met3.place(relx=0.6, rely=0.45)
        self.entry_met3 = Entry(self.form, font=('Arial',10))
        self.entry_met3.place(relx=0.655,rely=0.45, width=100)

        ## DATAS
        self.data_inicio = Label(self.form, text='Data de Contratação:', bg='white')
        self.data_inicio.place(relx=0.2, rely=0.50)
        self.entry_data_inicio = Entry(self.form, justify="left", font=('Arial',10))
        self.entry_data_inicio.place(relx=0.29,rely=0.5)
        self.btn_calendar1 = Button(self.entry_data_inicio, text='Calendario', command=self.calendario1)
        self.btn_calendar1.pack(fill='both',expand='1', padx=(100,0))


        self.data_fim = Label(self.form, text='Data de Finalização:', bg='white')
        self.data_fim.place(relx=0.42, rely=0.50)
        self.entry_data_fim = Entry(self.form, font=('Arial',10))
        self.entry_data_fim.place(relx=0.5,rely=0.5)
        self.btn_calendar2 = Button(self.entry_data_fim, text='Calendario', command=self.calendario2)
        self.btn_calendar2.pack(fill='both',expand='1', padx=(100,0))



        # Dados dos valores
        self.val_total = StringVar()
        self.val_total.set(0.0)
        self.val_pago = StringVar()
        self.val_pago.set(0.0)
        self.val_pago.trace('w',self.valor_pago_check)
        self.val_total.trace('w',self.valor_total_check)
        self.val_parcelar = DoubleVar()
        self.val_qnt_parcelas = IntVar()
        self.val_qnt_parcelas.set(1)
        self.val_qnt_parcelas.trace('w',self.valor_pago_check)
        self.val_dia_vencimento = IntVar()

        self.val_pgo_materiais = DoubleVar()
        self.val_pgo_materiais.trace('w',self.calc_lucro)
        self.val_pgo_mdo = DoubleVar()
        self.val_pgo_mdo.trace('w',self.calc_lucro)
        self.val_pgo_deco = DoubleVar()
        self.val_pgo_deco.trace('w',self.calc_lucro)

        self.message_error = Label(self.form, text="", bg='white', fg='red', font=("Arial",13))
        self.message_error.place(relx=0.28, rely=0.62)


        Label(self.form, text="Valor Total:", bg='white').place(relx=0.2, rely=0.555)
        self.vt_entry = Entry(self.form, bg='white', fg='green4', font=("Arial",13),textvariable=self.val_total, justify="center")
        self.vt_entry.place(relx=0.25, rely=0.555, height=25, width=100)

        Label(self.form, text="Valor Pago:", bg='white').place(relx=0.33, rely=0.555)
        self.va_entry = Entry(self.form, bg='white', fg='green4', font=("Arial",13), textvariable=self.val_pago, justify="center")
        self.va_entry.place(relx=0.38, rely=0.555, height=25, width=100)
        
        Label(self.form, text='Dia de Vencimento da Parcela:', bg='white').place(relx=0.459, rely=0.555)
        self.dia_de_vencimento = Entry(self.form, bg='white', font=('Arial',13), justify='center',textvariable = self.val_dia_vencimento)
        self.dia_de_vencimento.place(relx=0.574, rely=0.555, width=50, height=25)

        Label(self.form, text="Qnt. de Parcelas:", bg='white').place(relx=0.619, rely=0.555)
        self.qnt_parcelas = Entry(self.form, bg="white", font=('Arial',13), justify='center',textvariable=self.val_qnt_parcelas)
        self.qnt_parcelas.place(rely=0.555, relx=0.689, height=25, width=50)

        Label(self.form, text="Valor Pago em Materiais:", bg='white').place(relx=0.2, rely=0.61)
        self.pago_materiais = Entry(self.form, bg='white',textvariable=self.val_pgo_materiais, font=('Arial', 13), fg='red3', justify='center')
        self.pago_materiais.place(relx=0.295, rely=0.61, height=25, width=100)
        
        Label(self.form, text="Valor de mão de obra:", bg='white').place(relx=0.4, rely=0.61)
        self.pago_obra = Entry(self.form, bg="white",textvariable=self.val_pgo_mdo, font=('Arial',13), fg='red3', justify='center')
        self.pago_obra.place(relx=0.485, rely=0.61, height=25, width=100)

        Label(self.form, text="Valor em Decoração:", bg='white').place(relx=0.59, rely=0.61)
        self.pago_decoracao = Entry(self.form, bg="white",textvariable=self.val_pgo_deco, font=('Arial', 13), fg='red3', justify='center')
        self.pago_decoracao.place(relx=0.67, rely=0.61, height=25, width=100)


        Label(self.form, text="Valor Parcelado:", bg='white', font=('Arial',13)).place(relx=0.2, rely=0.683)
        self.print_qnt_par = Label(self.form, text="1x",justify='right', bg='white',font=('Arial',11), fg='green4')
        self.print_qnt_par.place(relx=0.292, rely=0.687, width=35)
        self.vp_entry = Label(self.form, bg='white',text="R$", fg='green', font=("Arial",16), justify="center")
        self.vp_entry.place(relx=0.315, rely=0.68)

        Label(self.form, text="Lucro inicial:", bg='white', font=('Arial',12)).place(relx=0.2, rely=0.745)
        self.lucro_inst = Label(self.form, text="R$",bg='white', fg='green4', font=('Arial',15))
        self.lucro_inst.place(relx=0.27, rely=0.742)

        Label(self.form, text="Etapa:", bg='white').place(relx=0.4, rely=0.682)
        self.entry_etapa = Entry(self.form, bg='white')
        self.entry_etapa.place(relx=0.44, rely=0.682, width=250, height=100)

        self.submit = Button(self.form, text="Inserir", command=self.insere_projeto)
        self.submit.place(relx=0.67, rely=0.7, height=50, width=100)

    def tela_pesquisa(self):
        
        ## HEADER
        self.header = LabelFrame(self.Pesquisa, borderwidth = 2)
        self.header.config(bg='white')
        self.header.place(relx=0.5, rely=0.02, anchor='c',relwidth=1, relheight=0.05)

        Button(self.header, text='Voltar', command=self.pesquisa_to_menu, bg='white').place(relx=0, rely=0, relheight=1)
        Label(self.header, text='Sistema de Arquitetura', bg='white').place(relx=0.43, rely=0, relheight=1)

        ## TREE VIEW

        self.listaCli = ttk.Treeview(self.Pesquisa, height=10, column=("Nome", "CPF/CNPJ", "Telefone", "Tipo", "Metragem 1", "Metragem 2", "Metragem 3", "Data de Contratação", "Data de Conclusão", "Valor Total", "Valor Pago", "Valor Parcelado", "Qnt. de Parcelas", "Gasto em Material", "Gasto em mão de obra", "Gasto em Decoração"))
        
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Nome")
        self.listaCli.heading("#2", text="CPF/CNPJ")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Tipo de Construção")
        self.listaCli.heading("#5", text="Metragem 1")
        self.listaCli.heading("#6", text="Metragem 2")
        self.listaCli.heading("#7", text="Metragem 3")
        self.listaCli.heading("#8", text="Data de Contratação")
        self.listaCli.heading("#9", text="Data de Conclusão")
        self.listaCli.heading("#10", text="Valor Total")
        self.listaCli.heading("#11", text="Valor Pago")
        self.listaCli.heading("#12", text="Valor Parcelado")
        self.listaCli.heading("#13", text="Qnt. de Parcelas")
        self.listaCli.heading("#14", text="Gasto em Material")
        self.listaCli.heading("#15", text="Gasto em Mão de Obra")
        self.listaCli.heading("#16", text="Gasto em Decoração")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=300)
        self.listaCli.column("#2", width=150)
        self.listaCli.column("#3", width=100)
        self.listaCli.column("#4", width=150)
        self.listaCli.column("#5", width=50)
        self.listaCli.column("#6", width=50)
        self.listaCli.column("#7", width=50)
        self.listaCli.column("#8", width=50)
        self.listaCli.column("#9", width=50)
        self.listaCli.column("#10", width=50)
        self.listaCli.column("#11", width=50)
        self.listaCli.column("#12", width=50)
        self.listaCli.column("#13", width=50)
        self.listaCli.column("#14", width=50)
        self.listaCli.column("#15", width=50)
        self.listaCli.column("#16", width=50)

        self.listaCli.place(relx=0, rely=0.4, relwidth=1, relheight=0.85)
        self.select_projetos()

Application()
