import tkinter as tk
import numpy as np
import time
root = tk.Tk()
try:
    dicMain =  np.load('bancoDeDados.npy').item()
    today = (time.strftime("%d/%m/%Y"))
    janelaPai = tk.Toplevel(root)
    janelaPai.title('Clínica Oncológica')
    janelaPai.geometry('400x200+0+0')
    if today in dicMain:
        display = tk.LabelFrame(janelaPai,text = 'Agendamentos para hoje ('+today+')')
        for lista in dicMain[today]:
            for item in lista:
                left = tk.Label(display, text='Paciente:  '+item+
                                '\nHorário da Consulta:  '+lista[item][4]+'\n'
                                +'Especialista: '+lista[item][8]+'\n')
                left.pack()
    else:
        display = tk.LabelFrame(janelaPai,text = 'Não existem agendamentos para hoje.')
    display.pack(fill='both',expand = 'yes')
except:
    dicMain = dict()


class Main:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Cadastrar Consulta', width = 25, command = self.cad)
        self.button2 = tk.Button(self.frame, text = 'Remover', width = 25, command = self.remove)
        self.button3 = tk.Button(self.frame, text = 'Pesquisar', width = 25, command = self.find)
        self.button6 = tk.Button(self.frame, text = 'Listar', width = 25, command = self.show)        
        self.button5 = tk.Button(self.frame, text = 'Salvar', width = 25, command = self.save)
        self.button4 = tk.Button(self.frame, text = 'Sair', width = 25, command = self.dest)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button6.pack()
        self.button5.pack()
        self.button4.pack()
        self.frame.pack()
    def cad(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Cadastra(self.newWindow)

    def remove(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Remove(self.newWindow)

    def find(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Pesquisa(self.newWindow)
        
    def save(self):
        self.novaJ = tk.Toplevel(self.master)
        try:
            np.save('bancoDeDados.npy',dicMain)
            out = tk.Label(self.novaJ,text = 'Agenda Salvada!')
        except:
            out = tk.Label(self.novaJ,text = 'ERROR')
        out.pack()

    def show(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Listagem(self.newWindow)
        
    def dest(self):
        self.master.destroy()

class Cadastra:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.getNome = tk.Entry(self.master)
        gNome = tk.Label(self.master,text = 'Nome: ')
        
        self.getIdade = tk.Entry(self.master)
        gIdade = tk.Label(self.master,text = 'Idade: ')
        
        self.getNasc = tk.Entry(self.master)
        gNas = tk.Label(self.master,text = 'Nascimento: ')
        
        self.getSexo = tk.Entry(self.master)
        gSexo = tk.Label(self.master,text = 'Sexo: ')

        self.getConsulta = tk.Entry(self.master)
        gConsulta = tk.Label(self.master,text = 'Dia da Consulta: ')

        self.getHora = tk.Entry(self.master)
        gHora = tk.Label(self.master,text = 'Horário: ')

        self.getEnd = tk.Entry(self.master)
        gEnd = tk.Label(self.master,text = 'Endereço: ')
        
        self.getRg = tk.Entry(self.master)
        gRg = tk.Label(self.master,text = 'RG: ')
        
        self.getCpf = tk.Entry(self.master)
        gCpf = tk.Label(self.master,text = 'CPF: ')
        
        self.getTelefone = tk.Entry(self.master)
        gTelefone = tk.Label(self.master,text = 'Telefone: ')

        self.getEsp = tk.Entry(self.master)
        gEsp = tk.Label(self.master,text = 'Especialista: ')


        self.getNome.place(x = 100,y = 10,width = 135)
        gNome.place(x = 7,y=10)
        
        self.getIdade.place(x = 100,y = 50,width = 135)
        gIdade.place(x = 7,y=50)
        
        self.getNasc.place(x = 100,y = 93,width = 135)
        gNas.place(x = 3,y=93)
        
        self.getSexo.place(x = 100,y = 135,width = 135)
        gSexo.place(x = 7,y=135)
        
        self.getConsulta.place(x = 100,y = 190,width = 135)
        gConsulta.place(x = 1,y=190)

        self.getHora.place(x = 100,y = 230,width = 135)
        gHora.place(x = 3,y=230)

        self.getEnd.place(x = 100,y = 280,width = 135)
        gEnd.place(x = 3,y=280)

        self.getRg.place(x = 100,y = 310,width = 135)
        gRg.place(x = 3,y=310)

        self.getCpf.place(x = 100,y = 370,width = 135)
        gCpf.place(x = 1,y=370)

        self.getTelefone.place(x = 100,y = 410,width = 135)
        gTelefone.place(x = 3,y=410)

        self.getEsp.place(x = 100,y = 440,width = 135)
        gEsp.place(x = 3,y=440)
        
        self.getAll = tk.Button(self.frame,text = 'Cadastrar',command = self.getCadastro)

        self.getAll.grid(row = 1,column = 4)
        self.frame.pack()
        self.master.geometry('700x500')
        
    def close_windows(self):
        self.master.destroy()
    def getCadastro(self):
        nome = str(self.getNome.get())
        diaC = str(self.getConsulta.get())
        end = str(self.getEnd.get())
        idade = str(self.getIdade.get())
        nas = str(self.getNasc.get())
        hora = str(self.getHora.get())
        sex = str(self.getSexo.get())
        tel = str(self.getTelefone.get())
        rg = str(self.getRg.get())
        cpf = str(self.getCpf.get())
        esp = str(self.getEsp.get())
        self.getNome.delete(0,tk.END)
        self.getConsulta.delete(0,tk.END)
        self.getEnd.delete(0,tk.END)
        self.getSexo.delete(0,tk.END)
        self.getHora.delete(0,tk.END)
        self.getIdade.delete(0,tk.END)
        self.getNasc.delete(0,tk.END)
        self.getTelefone.delete(0,tk.END)
        self.getRg.delete(0,tk.END)
        self.getCpf.delete(0,tk.END)
        self.getEsp.delete(0,tk.END)
        car = [idade,nas,sex,end,hora,tel,rg,cpf,esp]
        dic = {nome:car}
        lis = [dic]
        novaJ = tk.Toplevel(self.master)
        out = tk.Label(novaJ,text = 'Paciente Cadastrado!')
        if diaC in dicMain:
            dicMain[diaC].append(dic)
            out.pack()
        else:
            d = {diaC:lis}
            dicMain.update(d)
            out.pack()

class Remove:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        alt = self.master.winfo_screenheight()
        y = alt - 250
        
        self.getN = tk.Entry(self.master)
        gN = tk.Label(self.master,text = 'Paciente: ')
        self.getDestroyNome = tk.Button(self.frame,
                                text = 'Remover Paciente',
                                command = self.getDN)
        
        self.getData = tk.Entry(self.master)
        gData = tk.Label(self.master,text = 'Dia: ')
        self.getDestroyData = tk.Button(self.frame,
                                text = 'Remover Dia',command = self.getD)

        self.getN.place(x = 60,y = 10,width = 160)
        gN.place(x = 3,y = 10)
        self.getDestroyNome.pack(side = tk.RIGHT)

        self.getData.place(x = 30,y = 50,width = 135)
        gData.place(x = 3,y = 50)
        self.getDestroyData.pack(side = tk.LEFT)
        
        self.master.geometry("400x145+0+%d" %(y))
        self.frame.pack(side = tk.BOTTOM)
    def getDN(self):
        top= tk.Toplevel(self.master)
        apagado = False
        user = str(self.getN.get())
        self.getN.delete(0,tk.END)
        for key in dicMain:
            for lista in dicMain[key]:
                cont = 0
                for item in lista:
                    if item == user:
                        apagado = True
                        try:
                            dicMain[key].pop(cont)
                            t1 = tk.Label(top,text = 'Usuário removido')
                        except:
                            t1 = tk.Label(top.master,text = 'ERROR')
                    cont= cont+1
        if not apagado:
            t1 = tk.Label(top,text = 'Usuário não foi encontrado')
        t1.pack(fill='both',expand = 'yes')
    def getD(self):
        to = tk.Toplevel(self.master)
        dia = str(self.getData.get())
        self.getData.delete(0,tk.END)
        if dia in dicMain:
            try:
                dicMain.pop(dia)
                d1 = tk.Label(to,text = 'Dia Removido')
            except:
                d1 = tk.Label(to,text = 'ERROR')
        else:
            d1 = tk.Label(to,text = 'Dia não encontrado')
        d1.pack(fill='both',expand = 'yes')
class Pesquisa:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        alt = self.master.winfo_screenheight()
        y = alt - 250
        larg = self.master.winfo_screenwidth()
        x = larg - 500
        
        self.getData = tk.Entry(self.master)
        gData = tk.Label(self.master,text = 'Dia: ')
        self.getFindData = tk.Button(self.frame,
                                text = 'Pesquisar Dia',command = self.day)

        self.getPeople = tk.Entry(self.master)
        gPeople = tk.Label(self.master,text = 'Paciente: ')
        self.getFindPeople = tk.Button(self.frame,
                                text = 'Pesquisar Paciente',command = self.pp)

        self.getData.place(x = 30,y = 20,width = 135)
        gData.place(x = 2,y = 20)
        self.getFindData.pack(side = tk.LEFT)

        self.getPeople.place(x =70,y = 80,width = 135)
        gPeople.place(x = 2,y = 80)
        self.getFindPeople.pack(side = tk.LEFT)

        self.master.geometry("400x145+%d+%d" %(x,y))
        self.frame.pack(side = tk.BOTTOM)


    def day(self):
        d = str(self.getData.get())
        self.getData.delete(0,tk.END)
        top= tk.Toplevel(self.master)
        top.geometry('400x500')
        if d in dicMain:
            display = tk.LabelFrame(top,text = 'Agendamentos para: '+d)
            for lista in dicMain[d]:
                for item in lista:
                    left = tk.Label(display, text='Paciente:  '+item+
                                '\nHorário da Consulta:  '+lista[item][4]+'\n'
                                    +'Especialista: '+lista[item][8]+'\n')
                    left.pack()
        else:
            display = tk.LabelFrame(top,text = 'Não existem agendamentos para '+d)
        display.pack(fill='both',expand = 'yes')

    #car = [idade,nas,sex,end,hora.tel,rg,cpf,esp]
    def pp(self):
        ind = ['Idade: ','Nascimento: ','Sexo: ','Endereço: ','Hora: ','Telefone: ','RG: ','CPF: ','Especialista: ']
        achado = False
        p = str(self.getPeople.get())
        self.getPeople.delete(0,tk.END)
        top = tk.Toplevel(self.master)
        top.geometry('400x500')
        for dia in dicMain:
            for lista in dicMain[dia]:
                if p in lista:
                    achado = True
                    display = tk.LabelFrame(top,text = 'Dia da consulta: '+dia)
                    for item in lista:
                        left = tk.Label(display, text='Paciente:  '+item)
                        left.pack()
                        cont = 0
                        for obj in lista[item]:
                            t = tk.Label(display, text=ind[cont]+''+obj)
                            cont+=1
                            t.pack()
        if not achado:
            display = tk.LabelFrame(top,text = 'Não foi encontrado o paciente '+p)
        display.pack(fill='both',expand = 'yes')

class Listagem:

    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        larg = self.master.winfo_screenwidth()
        x = larg - 810
        ind = ['Idade: ','Nascimento: ','Sexo: ','Endereço: ','Hora: ','Telefone: ','RG: ','CPF: ','Especialista: ']
        for dia in dicMain:
            display = tk.LabelFrame(self.master,text = 'Dia da consulta: '+dia)
            for lista in dicMain[dia]:
                for item in lista:
                    left = tk.Label(display, text='Paciente:  '+item+
                                    '\nHorário da Consulta:  '+lista[item][4]+'\n'
                                +'Especialista: '+lista[item][8]+'\n')
                    left.pack()
                    cont = 0
            display.pack(fill='both',expand = 'yes')

        self.master.geometry('800x800+%d+10' %(x))

def main():
    larg = root.winfo_screenwidth()
    alt = root.winfo_screenheight()
    x = (larg/2) - (650/2)
    y = (alt/2) - (190/2)
    root.geometry("650x190+%d+%d" %(x,y))
    app = Main(root)
    root.title('Clínica Oncológica')
    root.mainloop()

if __name__ == '__main__':
    main()
