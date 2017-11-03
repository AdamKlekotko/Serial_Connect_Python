from tkinter import *
from tkinter import ttk, filedialog
from tkinter.ttk import Style
from serial.tools import list_ports


class Window(Frame):

    def __init__(self,parent):

        self.parent=parent


        self.parent.title("Connetction To Serial Port")
        self.style = Style()
        self.style.theme_use()


        self.parent.baud_text = StringVar();
        self.parent.baud_text.set("Baud Rate:")
        self.parent.baud_label =Label(self.parent,textvariable = self.parent.baud_text )
        self.parent.baud_label.grid(row=0, column=0,sticky='WENS')

        self.parent.data_text = StringVar();
        self.parent.data_text.set("Data Bits:")
        self.parent.data_label = Label(self.parent, textvariable=self.parent.data_text)
        self.parent.data_label.grid(row=1, column=0,sticky='WENS')

        self.parent.stopB_text = StringVar();
        self.parent.stopB_text.set("Stop Bits:")
        self.parent.stopB_label = Label(self.parent, textvariable=self.parent.stopB_text)
        self.parent.stopB_label.grid(row=2, column=0,sticky='WENS')

        self.parent.parity_text = StringVar();
        self.parent.parity_text.set("Parity:")
        self.parent.parity_label = Label(self.parent, textvariable=self.parent.parity_text)
        self.parent.parity_label.grid(row=3, column=0,sticky='WENS')

        self.parent.to_connect_text =StringVar();
        self.parent.to_connect_text.set("Serial Port to connect:")
        self.parent.to_connect_label = Label(self.parent, textvariable=self.parent.to_connect_text)
        self.parent.to_connect_label.grid(row=4, column=0,sticky='WENS')

        self.parent.baud_select_combo = ttk.Combobox(self.parent, state="readonly");
        self.parent.baud_select_combo['values'] = ('9600','19200','38400', '57600','115200');
        self.parent.baud_select_combo.current(0)
        self.parent.baud_select_combo.grid(row=0, column=1,sticky='WENS')

        self.parent.data_select_combo = ttk.Combobox(self.parent, state="readonly");
        self.parent.data_select_combo['values'] = ('7', '8');
        self.parent.data_select_combo.current(1)
        self.parent.data_select_combo.grid(row=1, column=1,sticky='WENS')

        self.parent.stopB_select_combo = ttk.Combobox(self.parent, state="readonly");
        self.parent.stopB_select_combo['values'] = ('1', '2');
        self.parent.stopB_select_combo.current(0)
        self.parent.stopB_select_combo.grid(row=2, column=1,sticky='WENS')

        self.parent.parity_select_combo = ttk.Combobox(self.parent, state="readonly");
        self.parent.parity_select_combo['values'] = ('None', 'Odd','Even','Mark','Space');
        self.parent.parity_select_combo.current(0)
        self.parent.parity_select_combo.grid(row=3, column=1,sticky='WENS')

        list = list_ports.comports();
        self.parent.to_connect_select_combo = ttk.Combobox(self.parent, state="readonly");
        self.parent.to_connect_select_combo['values'] = (list);
        self.parent.to_connect_select_combo.current(0)
        self.parent.to_connect_select_combo.grid(row=4, column=1,sticky='WENS')

        self.parent.info_label = Label(self.parent, text="File:")
        self.parent.info_label.grid(row=5, column=0,sticky='WENS')

        FileText="Not Selected"

        self.parent.file_label = Label(self.parent, text=FileText)
        self.parent.file_label.grid(row=5, column=1,sticky='WENS')

        self.parent.button_file = Button(self.parent, text="Sellect File to save data", command=self.GetFile);
        self.parent.button_file.grid(row=6, columnspan=2,sticky='WENS')

        self.parent.button = Button(self.parent,text="Connect",command = self.GetConnectionParameters());
        self.parent.button.grid(row=7,columnspan=2,sticky='WENS')


    def ButtonClick(self):
        myString=str(self.to_connect_select_combo.get())
        print( myString.split(" - ", 1)[0])
    def GetFile(self):
        self.filename = filedialog.asksaveasfilename(parent=self.parent, title='Select file',filetypes=[('Text files','.csv')])
        self.parent.file_label["text"] = str(self.filename) if self.filename else 'Select file'

    def GetConnectionParameters(self):
        return ()





