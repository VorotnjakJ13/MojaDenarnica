##Moja Denarnica##

from tkinter import *

import os

class MojaDenarnica():

    
    def __init__(self, master):

        #osnovni seznami
        self.trans=[]
        self.dvigi=[]
        self.pologi=[]
        
        #glavni menu
        menu= Menu(master)
        master.config(menu=menu)
        #podmenu File
        file_menu=Menu(menu)
        menu.add_cascade(label='File', menu=file_menu)
        
        #dodamo izbire v file_menu
        '''dodati je treba še komande'''
        file_menu.add_command(label='Novo',command=self.file_new)
        file_menu.add_command(label='Shrani...', command=self.file_save)
        file_menu.add_command(label='Odpri...',command=self.file_open)
        file_menu.add_separator()
        file_menu.add_command(label='IZHOD',command=master.destroy)
        
        #podmenu PREGLED
        pregled_menu=Menu(menu)
        menu.add_cascade(label='Pregled',menu=pregled_menu)
        pregled_menu.add_command(label='Vsi pologi',command=self.vsi_pologi)
        pregled_menu.add_command(label='Vsi dvigi',command=self.vsi_dvigi)
        pregled_menu.add_command(label='Vsi pologi in dvigi',command=self.vsi_pologi_in_dvigi)
        
        #podmenu Graf
        #graf_menu=Menu(menu)
        #menu.add_cascade(label='Grafični Prikaz Stanja', menu=graf_menu)

        foo= Label(root,text='Vpiši znesek in izberi vrsto transakcije!'+'\n'
                   +'Vnos decimalnih števil je definiran z decimalno piko.')
        foo.grid(row=0,column=0)

        #definicija zneska, stanja
        self.znesek = DoubleVar(master, value=0)
        self.stanje = 0

        Label(master, text="Znesek:").grid(row=1, column=0)
        polje_znesek = Entry(master, textvariable=self.znesek)
        polje_znesek.grid(row=1, column=1)
        
        #gumbi      
        gumb_dvig=Button(master, text='Opravi dvig >> ',command=self.dvig)
        gumb_dvig.grid(row=2,column=1)
        
        gumb_polog=Button(master, text='Opravi polog >> ',command=self.polog)
        gumb_polog.grid(row=3,column=1)

        self.stanje = DoubleVar(master, value=0)
        Label(master,text='Stanje:').grid(row=4,column=0)
        label_stanje=Label(master, textvariable=self.stanje)
        label_stanje.grid(row=4,column=1)
        
######## funkcije dvig, polog

    def dvig(self):
        koliko = float(self.znesek.get())
        print(koliko)
        print(self.stanje)
        if self.stanje.get() - koliko >= 0:
            self.stanje.set(self.stanje.get()-koliko)
            self.dvigi.append(koliko*(-1))
            self.trans.append(koliko*(-1))
            print(self.trans)
            return self.stanje.get()
        return False
    
    def polog(self):
        
        koliko=float(self.znesek.get())
        self.stanje.set(self.stanje.get()+koliko)
        print(self.stanje)
        if True:
            self.pologi.append(koliko)
            self.trans.append(koliko)
            print(self.trans)
            
        return self.stanje.get()
    
######### OPEN,SAVE,NEW
    def file_new(self):
        self.stanje.set(0)
        self.trans.clear()
        self.dvigi.clear()
        self.pologi.clear()
        self.znesek.set(0)

    
    def file_open(self):    
        mask= \
              [('Denarnica datoteke','*.den'),
               ('All files','*.*')]
        file_in = filedialog.askopenfilename(filetypes=mask)
        
        if file_in == '':
            return
        
        
         ## DELA :-)
        with open(file_in,'r',encoding='utf8') as d:
            self.pologi.clear()
            self.dvigi.clear()
            self.trans.clear()
            trans=d.read().split('\n') #list , znotraj string
            
            for znesek in trans:
                self.trans.append(znesek)
            self.trans.remove(self.trans[-1])#pojavi se na koncu'', odstrani
            
            transakcije=[]
            for znesek in self.trans:
                transakcije.append(float(znesek))##string-->float
        
            self.trans.clear() ##naštima self.trans
            self.trans=transakcije

            for znesek in self.trans: ##naštima self.pologi/self.dvigi/self.stanje
                if znesek>0:
                    self.pologi.append(znesek)
                else:
                    self.dvigi.append(znesek)
                self.stanje.set(sum(self.trans))
                ##zdej lahko urejamo :-)
            
                         
        ### DELA :-)
    def file_save(self):
        mask= \
              [('Denarnica datoteke','*.den'),
               ('All files','*.*')]
        file_out=filedialog.asksaveasfilename(defaultextension='.den', filetypes=mask)       
        if file_out=='':
            return

        with open(file_out,'w',encoding='utf8') as f:
            for znesek in self.trans:
                print(znesek,file=f)
                
        f.close()
        
###### VSI POLOGI; VSI DVIGI, VSI POLOGI IN DVIGI
        ###DELA :-) 
    def vsi_pologi(self):
        popup= Toplevel()
        popup.title('Vsi Pologi...')
        seznam = ""
        for znesek in self.pologi:
            seznam = seznam + str(' + '+ str(znesek)+'\n')
        Message(popup,text=seznam).pack()
        izhod= Button(popup, text='Zapri', command=popup.destroy)
        izhod.pack()

    def vsi_dvigi(self):
        popup= Toplevel()
        popup.title('Vsi Dvigi...')
        seznam=''
        for znesek in self.dvigi:
            seznam = seznam + str(znesek)+'\n'
        Message(popup, text=seznam).pack()
        izhod= Button(popup, text = 'Zapri', command=popup.destroy).pack()

    def vsi_pologi_in_dvigi(self):
        popup= Toplevel()
        popup.title('Vsi Pologi in Dvigi...')
        seznam = ''
        for znesek in self.trans:
            seznam = seznam + str(znesek)+'\n'
        
        Message(popup,text=seznam).pack()
        izhod= Button(popup, text='Zapri', command=popup.destroy)
        izhod.pack()

       
root = Tk(className=''' Moja Denarnica''')
foo = Label(root, text= 'Avtor: Julija Vorotnjak')
foo.grid(row=5,column=3)

aplikacija = MojaDenarnica(root)
root.mainloop()


