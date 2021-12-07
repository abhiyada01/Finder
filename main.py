from tkinter import *
from tkinter import messagebox
import sqlite3 as sl
from tkinter import filedialog
from pandas import read_csv
from pandas import DataFrame
import os
import sys

class main:

    def __init__(self, root):
        self.root =root

        self.del_state = 'by_default'
#====================Function=======================
        def iexit():
            iexts = messagebox.askyesno('Confirm', 'Are you want to close')
            if iexts == 1:
                self.root.destroy()
        def file_dir():
            diri = "C:\\Users\\Abhishek Kumar\\Desktop\\Project\\Pro2\\com_database.db"
            return diri
        def iclear():
            PartNameent.delete(0, 'end')
            PartNumberent.delete(0, 'end')
            PCBNameent.delete(0, 'end')
            PCBNumberent.delete(0, 'end')
            Boxent.delete(0, 'end')
            Description.delete(0, 'end')

        def cap(event):
            try:
                v_pnam.set((v_pnam.get()).upper())
                v_pnum.set((v_pnum.get()).upper())
                v_pcb_nam.set((v_pcb_nam.get()).upper())
                v_pcb_num.set((v_pcb_num.get()).upper())
                v_box.set((v_box.get()).upper())
                v_des.set((v_des.get()).upper())
            except:
                messagebox.showerror('Alert', 'Enter correct entry')
                
        def com_display():
            file = file_dir()
            conn = sl.connect(file)
            c = conn.cursor()
            c.execute('SELECT * FROM component')
            data = c.fetchall()
            com_list.delete(0, 'end')
            for row in data:
                com_list.insert('end', row, str('|'))
            conn.close()

        def com_search():
            if (len(PartNameent.get())) != 0 or (len(PartNumberent.get())) != 0 or (len(PCBNameent.get())) != 0 or (len(PCBNumberent.get())) != 0 or (len(Boxent.get())) != 0 or (len(Description.get())) != 0:
                file = file_dir()
                conn = sl.connect(file)
                c = conn.cursor()
                c.execute('SELECT * FROM component WHERE (part_name = ? OR part_num= ? OR pcbname= ? OR pcbnum= ? OR box_num= ?)',(PartNameent.get(),PartNumberent.get(),PCBNameent.get(),PCBNumberent.get(),Boxent.get()))
                data = c.fetchall()
                com_list.delete(0, 'end')
                for row in data:
                    com_list.insert('end', row, str('|'))
                conn.close()
            else:
                messagebox.showerror('warning','Atleast One should be filled except description')

        def com_rec(event):
            try:
                serrec = com_list.curselection()[0]
                data_r = com_list.get(serrec)
                
                PartNameent.delete(0, 'end')
                v_pnam.set(data_r[0])
                
                PartNumberent.delete(0, 'end')
                v_pnum.set(data_r[1])
                
                PCBNameent.delete(0, 'end')
                v_pcb_nam.set(data_r[2])
                
                PCBNumberent.delete(0, 'end')
                v_pcb_num.set(data_r[3])
                
                Boxent.delete(0, 'end')
                v_box.set(data_r[4])
                
                Description.delete(0, 'end')
                v_des.set(data_r[5])
                
                return data_r[0]
            except:
                pass

        

        def extra_win():
            try:
                ent = filedialog.askopenfilename(title = "Select a File", filetypes = (("CSV files", "*.csv*"),("all files", "*.*")))  
                data = read_csv(ent)
                df = DataFrame(data, columns = ['PartName','PartNumber', 'PCBName', 'PCBNumber', 'Box', 'Description'])
                print(df)
                file_connet = file_dir()
                conn = sl.connect(file_connet)
                c = conn.cursor()
                for row in df.itertuples():
                    part_name = row.PartName
                    part_num= row.PartNumber
                    pcbname = row.PCBName
                    pcbnum = row.PCBNumber
                    box_num = row.Box
                    description = row.Description
                    c.execute('INSERT INTO component VALUES(?,?,?,?,?,?)',(part_name,part_num,pcbname,pcbnum,box_num,description))
                conn.commit()
                conn.close()
            except Exception as e: 
                messagebox.showerror('warning',e)
                

        def del_data():
            if (len(PartNameent.get())) != 0:             
                serrec = com_list.curselection()[0]
                data_r = com_list.get(serrec)
                p_d = data_r[0]
                file = file_dir()
                conn = sl.connect(file)
                c = conn.cursor()
                c.execute("DELETE FROM component WHERE part_name = ?",(p_d,))
                conn.commit()
                conn.close()
                com_display()
                iclear()
        

            
        def adva_login():
            
            if self.del_state == 'by_default':
                butt3.config(text = 'Delete', command = del_data)
                self.del_state = 'Alredy'
            else:
                if self.del_state == 'Alredy':
                    butt3.config(text = 'Clear', command = iclear)
                    self.advance_log_text = 'Advance login'

            
#====================Menu============================
        menubar = Menu(self.root)

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = 'Advance login', command = adva_login)
        filemenu.add_command(label = 'Data Insert', command = extra_win)
        filemenu.add_separator()
        filemenu.add_command(label = 'Exit', command = self.root.destroy)
        menubar.add_cascade(label= 'Menu',menu = filemenu)
        self.root.config(menu = menubar)

        v_pnam = StringVar()
        v_pnum = StringVar()
        v_pcb_nam = StringVar()
        v_pcb_num = StringVar()
        v_box = StringVar()
        v_des = StringVar()
        
#===============================Frame==================================
        mainframe = Frame(self.root)
        mainframe.pack()
        tops = Frame(mainframe, width=768, height=576, bg="alice blue")
        tops.grid(row=0, column=0, columnspan =2)
        status = Frame(mainframe, width=768, height=576, bg="alice blue", bd = 10)
        status.grid(row=1, column=0, pady=4)
        listframe = Frame(mainframe, width=768, height=576, bg="alice blue")
        listframe.grid(row=1, column=1)
        buttonframe = Frame(mainframe, width=768, height=576, bg="alice blue")
        buttonframe.grid(row=2, column=0, columnspan =2)
#===============================Label & Entry=====================================
        tit = Label(tops,text= 'Component Management System', font = ('arial', 35, 'bold'))
        tit.pack()

        PartNamelbl = Label(status, text = 'Part Name',  font = ('arial', 15, 'bold'))
        PartNamelbl.grid(row =0, column =0, sticky = 'w')
        PartNameent = Entry(status, textvariable = v_pnam,  font = ('arial', 15, 'bold'))
        PartNameent.grid(row = 0, column = 1, padx =5, pady = 30)
        PartNameent.bind("<KeyRelease>", cap)
        
        PartNumberlbl = Label(status, text = 'Part Number',  font = ('arial', 15, 'bold'))
        PartNumberlbl.grid(row =1, column =0, sticky = 'w')
        PartNumberent = Entry(status, textvariable = v_pnum,  font = ('arial', 15, 'bold'))
        PartNumberent.grid(row =1, column = 1, padx =5, pady = 30)
        PartNumberent.bind("<KeyRelease>", cap)
        
        PCBNamelbl= Label(status, text = 'PCB Name',  font = ('arial', 15, 'bold'))
        PCBNamelbl.grid(row =2, column =0, sticky = 'w')
        PCBNameent = Entry(status, textvariable = v_pcb_nam,  font = ('arial', 15, 'bold'))
        PCBNameent.grid(row = 2, column =1, padx =5, pady = 30)
        PCBNameent.bind("<KeyRelease>", cap)
        
        PCBNumberlbl= Label(status, text = 'PCB Number',  font = ('arial', 15, 'bold'))
        PCBNumberlbl.grid(row =3, column =0, sticky = 'w')
        PCBNumberent = Entry(status,  textvariable = v_pcb_num,  font = ('arial', 15, 'bold'))
        PCBNumberent.grid(row=3, column=1, padx =5, pady = 30)
        PCBNumberent.bind("<KeyRelease>", cap)
        
        Boxlbl= Label(status, text = 'BOX Number',  font = ('arial', 15, 'bold'))
        Boxlbl.grid(row =4, column =0, sticky = 'w')
        Boxent = Entry(status, textvariable = v_box,  font = ('arial', 15, 'bold'))
        Boxent.grid(row=4, column=1, padx =5, pady = 30)
        Boxent.bind("<KeyRelease>", cap)
        
        Descriptionlbl= Label(status, text = 'Description',  font = ('arial', 15, 'bold'))
        Descriptionlbl.grid(row =5, column =0, sticky = 'w')
        Description = Entry(status, textvariable = v_des,  font = ('arial', 15, 'bold'))
        Description.grid(row=5, column=1, padx =5, pady = 30)
        Description.bind("<KeyRelease>", cap)
        
#=====================================Listbox====================================
        scroll = Scrollbar(listframe, orient="vertical")
        scroll.pack(side='right', fill='y')
        com_list = Listbox(listframe, width =60, height =17, setgrid= 0,selectmode = 'single',font =('arial', 20, 'bold'), yscrollcommand = scroll.set)
        com_list.pack(padx=10)
        com_list.bind("<<ListboxSelect>>", com_rec)
        scroll.config( command = com_list.yview )
        
#=====================================Button=======================================
        butt1 = Button(buttonframe, text = 'Display', font =('arial', 20, 'bold'),command=com_display )
        butt1.grid(row=0,column=0, padx =120, pady = 4)

        butt2 = Button(buttonframe, text = 'Search', font =('arial', 20, 'bold'), command = com_search)
        butt2.grid(row=0,column=1, padx =120, pady = 4)

        butt3 = Button(buttonframe, text = 'Clear', width =6, font =('arial', 20, 'bold'), command = iclear)
        butt3.grid(row=0,column=2, padx =120, pady = 4)

        butt4 = Button(buttonframe, text = 'Exit', font =('arial', 20, 'bold'), command = iexit)
        butt4.grid(row=0,column=3, padx =120, pady = 4)
        
if __name__ == '__main__':
    win = Tk()
    win.geometry('1350x740+0+0')
    win.iconbitmap('icon.ico')
    app = main(win)
    win.mainloop()
