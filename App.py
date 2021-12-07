from tkinter import *
from tkinter import ttk
import sqlite3 as sl
from tkinter import messagebox

pad = 3


class application(object):

    def __init__(self, root):

        self.root = root

        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        v6 = StringVar()

        mainframe = Frame(self.root)
        mainframe.pack()

        stsfrm = Frame(mainframe, relief='sunken')
        stsfrm.grid(row=0, column=0, columnspan=2)
        entfrm = Frame(mainframe)
        entfrm.grid(row=1, column=0)
        listframe = Frame(mainframe)
        listframe.grid(row=1, column=1)
        btnfrm = Frame(mainframe)
        btnfrm.grid(row=2, column=0, columnspan=2)

        title = Label(stsfrm, text='Component Managrmrnt System', font=('arial', 35, 'bold'))
        title.pack(expand=1, side='top')

        # ****************************Function*****************

        def iclear():
            E1.delete(0, 'end')
            E2.delete(0, 'end')
            E3.delete(0, 'end')
            E4.delete(0, 'end')
            E5.delete(0, 'end')
            E6.delete(0, 'end')

        def iupper(event):
            v1.set((E1.get()).upper())
            v2.set((E2.get()).upper())
            v3.set((E3.get()).upper())
            v4.set((E4.get()).upper())
            v5.set((E5.get()).upper())

        def ifile():
            try:
                with open('file_directory.txt') as f:
                    t = f.readline()
                return t
            except Exception:
                messagebox.showerror('warning', 'Database fole is not found')

        def idisplay():
            try:
                file = ifile()
                conn = sl.connect(file)
                c = conn.cursor()
                c.execute('SELECT * FROM component')
                data = c.fetchall()
                iclear()
                com_list.delete(*com_list.get_children())
                for row in data:
                    com_list.insert('', 'end', values=row)
                conn.close()
            except Exception:
                messagebox.showerror('warning', 'File not connected')

        def com_rec(event):
            try:
                serrec = com_list.selection()[0]
                data_r = com_list.item(serrec)['values']

                E1.delete(0, 'end')
                v1.set(data_r[0])

                E2.delete(0, 'end')
                v2.set(data_r[1])

                E3.delete(0, 'end')
                v3.set(data_r[2])
                E4.delete(0, 'end')
                v4.set(data_r[3])

                E5.delete(0, 'end')
                v5.set(data_r[4])

                E6.delete(0, 'end')
                v6.set(data_r[5])
            except:
                pass

        def iupdate():
            if (len(E1.get())) != 0 and (len(E2.get())) != 0 and (len(E3.get())) != 0 and (len(E4.get())) != 0 and (
            len(E5.get())) != 0 and (len(E6.get())) != 0:
                file = ifile()
                file = ifile()
                conn = sl.connect(file)
                c = conn.cursor()
                c.execute('''UPDATE component SET part_name = ?, part_num= ?, pcbname= ?, pcbnum= ?, box_num= ?, description= ?
                          WHERE part_name = ?and part_num= ? and pcbname= ?''',
                          (E1.get(), E2.get(), E3.get(), E4.get(), E5.get(), E6.get(), E1.get(), E2.get(), E3.get()))

                iclear()
                idisplay()
                conn.commit()
                conn.close()
            else:
                messagebox.showerror('warning', 'All should be filled including description')

        def isearch():
            if (len(E1.get())) != 0 or (len(E2.get())) != 0 or (len(E3.get())) != 0 or (len(E4.get())) != 0 or (
            len(E5.get())) != 0 or (len(E6.get())) != 0:
                file = ifile()
                conn = sl.connect(file)
                c = conn.cursor()
                c.execute(
                    'SELECT * FROM component WHERE (part_name = ? OR part_num= ? OR pcbname= ? OR pcbnum= ? OR box_num= ?)',
                    (E1.get(), E2.get(), E3.get(), E4.get(), E5.get()))
                data = c.fetchall()
                iclear()
                com_list.delete(*com_list.get_children())
                for row in data:
                    com_list.insert('', 'end', values=row)
                conn.close()
            else:
                messagebox.showerror('warning', 'Atleast One should be filled except description')

        L1 = Label(entfrm, text='Part Name', font=('arial', 15, 'bold'))
        L1.grid(row=0, column=0, padx=10, pady=30, sticky='w')
        E1 = Entry(entfrm, textvariable=v1, font=('arial', 15, 'bold'))
        E1.grid(row=0, column=1)
        E1.bind("<KeyRelease>", iupper)

        L2 = Label(entfrm, text='Part Number', font=('arial', 15, 'bold'))
        L2.grid(row=1, column=0, padx=10, pady=30, sticky='w')
        E2 = Entry(entfrm, textvariable=v2, font=('arial', 15, 'bold'))
        E2.grid(row=1, column=1)
        E2.bind("<KeyRelease>", iupper)

        L3 = Label(entfrm, text='PCB Name', font=('arial', 15, 'bold'))
        L3.grid(row=2, column=0, padx=10, pady=30, sticky='w')
        E3 = Entry(entfrm, textvariable=v3, font=('arial', 15, 'bold'))
        E3.grid(row=2, column=1)
        E3.bind("<KeyRelease>", iupper)

        L4 = Label(entfrm, text='PCB Number', font=('arial', 15, 'bold'))
        L4.grid(row=3, column=0, padx=10, pady=30, sticky='w')
        E4 = Entry(entfrm, textvariable=v4, font=('arial', 15, 'bold'))
        E4.grid(row=3, column=1)
        E4.bind("<KeyRelease>", iupper)

        L5 = Label(entfrm, text='Box Number', font=('arial', 15, 'bold'))
        L5.grid(row=4, column=0, padx=10, pady=30, sticky='w')
        E5 = Entry(entfrm, textvariable=v5, font=('arial', 15, 'bold'))
        E5.grid(row=4, column=1)
        E5.bind("<KeyRelease>", iupper)

        L6 = Label(entfrm, text='Description', font=('arial', 15, 'bold'))
        L6.grid(row=5, column=0, padx=10, pady=30, sticky='w')
        E6 = Entry(entfrm, textvariable=v6, font=('arial', 15, 'bold'))
        E6.grid(row=5, column=1)

        # =====================================Listbox====================================
        scroll = Scrollbar(listframe, orient="vertical")
        scroll.pack(side='right', fill='y', padx=2)
        com_list = ttk.Treeview(listframe, columns=(1, 2, 3, 4, 5, 6), show='headings', height=20,
                                yscrollcommand=scroll.set)
        com_list.pack(fill='both', expand='yes', padx=10, pady=10)
        com_list.heading(1, text="Part Name")
        com_list.column(1, minwidth=0, width=150, stretch=NO)

        com_list.heading(2, text="Part Number")
        com_list.column(2, minwidth=0, width=150, stretch=NO)

        com_list.heading(3, text="PCB Name")
        com_list.column(3, minwidth=0, width=150, stretch=NO)

        com_list.heading(4, text="PCB Number")
        com_list.column(4, minwidth=0, width=150, stretch=NO)

        com_list.heading(5, text="Box Name")
        com_list.column(5, minwidth=0, width=90, stretch=NO)

        com_list.heading(6, text="Description")
        com_list.column(6, minwidth=0, width=150, stretch=NO)

        com_list.bind("<ButtonRelease-1>", com_rec)
        scroll.config(command=com_list.yview)

        B1 = Button(btnfrm, text='Display', font=('arial', 15, 'bold'), command=idisplay)
        B1.grid(row=0, column=0, padx=90, pady=10)

        B2 = Button(btnfrm, text='Search', font=('arial', 15, 'bold'), command=isearch)
        B2.grid(row=0, column=1, padx=90, pady=10)

        B3 = Button(btnfrm, text='Clear', font=('arial', 15, 'bold'), command=iclear)
        B3.grid(row=0, column=2, padx=90, pady=10)

        B4 = Button(btnfrm, text='Update', font=('arial', 15, 'bold'), command=iupdate)
        B4.grid(row=0, column=3, padx=90, pady=10)


def execute():
    win = Tk()
    win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth() - pad,
                                      win.winfo_screenheight() - pad))
    win.iconbitmap(r'icon.ico')
    app = application(win)
    win.mainloop()


if __name__ == '__main__':
    execute()
