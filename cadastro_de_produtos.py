from tkinter import *
import sqlite3

conn = sqlite3.connect("store.db")
c = conn.cursor()

result = c.execute("SELECT MAX(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Cadastro de Produtos", font=("ubuntu 25 bold"))
        self.heading.place(x=465, y=10)

        self.name_1 = Label(master, text="Produto: ", font=("Liberation_Serif 14 bold"))
        self.name_1.place(x=10, y=100)

        self.stock_1 = Label(master, text="Quantidade em estoque: ", font=("Liberation_Serif 14 bold"))
        self.stock_1.place(x=10, y=140)

        self.cp_1 = Label(master, text="Preço de custo: ", font=("Liberation_Serif 14 bold"))
        self.cp_1.place(x=10, y=180)

        self.sp_1 = Label(master, text="Preço de venda: ", font=("Liberation_Serif 14 bold"))
        self.sp_1.place(x=10, y=220)

        self.vendor_1 = Label(master, text="Fornecedor: ", font=("Liberation_Serif 14 bold"))
        self.vendor_1.place(x=10, y=260)

        self.vendor_phone_1 = Label(master, text="Telefone Fornecedor: ", font=("Liberation_Serif 14 bold"))
        self.vendor_phone_1.place(x=10, y=300)

        self.id_1 = Label(master, text="Código: ", font=("Liberation_Serif 14 bold"))
        self.id_1.place(x=10, y=340)

        self.name_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.name_e.place(x=300, y=100)

        self.stock_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.stock_e.place(x=300, y=140)

        self.cp_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.cp_e.place(x=300, y=180)

        self.sp_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.sp_e.place(x=300, y=220)

        self.vendor_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.vendor_e.place(x=300, y=260)

        self.vendor_phone_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.vendor_phone_e.place(x=300, y=300)

        self.id_e = Entry(master, width = 25, font=("Liberation_Serif 14"))
        self.id_e.place(x=300, y=340)

        self.btn_add = Button(master, text="Cadastrar", font=('Liberation_Serif 12 bold'), width = 13, height=2, command=self.get_items)
        self.btn_add.place(x=435, y=400)

        self.btn_clear = Button(master, text="Limpar", font=('Liberation_Serif 12 bold'), width = 8, height=2, command=self.clear_all)
        self.btn_clear.place(x=300, y=400)

        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=100)
        self.tBox.insert(END, "Código do Ultimo Cadastro: " + str(id))

        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, ** kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)

        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name=='' or self.cp=='' or self.stock=='' or self.sp=='':
            tkinter.messagebox.showinfo("FAVOR PREENCHER TODOS OS CAMPOS!")
        else:
            sql = "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phone) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()

            self.tBox.insert(END, "\n\nProduto:" + str(self.name) + "cadastrado no banco de dados com Código: " + str(self.id_e.get()))

            tkinter.messagebox.showinfo("CADASTRO REALIZADO COM SUCESSO!")

    def clear_all(self, *args, ** kwargs):
        num = id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)

root = Tk()
b = Database(root)

root.geometry("1280x720+0+0")
root.title("FORMULÁRIO DE CADASTRO")
root.mainloop()