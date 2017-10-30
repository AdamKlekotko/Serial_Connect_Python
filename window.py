import tkinter
from tkinter import ttk
from serial.tools import list_ports



class Window():

    def __init__(self):

        self= tkinter.Tk()
        self.frame = tkinter.Frame(self)
        self.frame.pack()

        self.baud_text = tkinter.StringVar();
        self.baud_text.set("Baud Rate:")
        self.baud_label = tkinter.Label(self.frame,textvariable = self.baud_text )
        self.baud_label.grid(row=0, column=0)

        self.data_text = tkinter.StringVar();
        self.data_text.set("Data Bits:")
        self.data_label = tkinter.Label(self.frame, textvariable=self.data_text)
        self.data_label.grid(row=1, column=0)

        self.stopB_text = tkinter.StringVar();
        self.stopB_text.set("Stop Bits:")
        self.stopB_label = tkinter.Label(self.frame, textvariable=self.stopB_text)
        self.stopB_label.grid(row=2, column=0)

        self.parity_text = tkinter.StringVar();
        self.parity_text.set("Parity:")
        self.parity_label = tkinter.Label(self.frame, textvariable=self.parity_text)
        self.parity_label.grid(row=3, column=0)

        self.to_connect_text = tkinter.StringVar();
        self.to_connect_text.set("Serial Port to connect:")
        self.to_connect_label = tkinter.Label(self.frame, textvariable=self.to_connect_text)
        self.to_connect_label.grid(row=4, column=0)

        self.baud_select_combo = ttk.Combobox(self.frame, state="readonly");
        self.baud_select_combo['values'] = ('9600','19200','38400', '57600','115200');
        self.baud_select_combo.current(0)
        self.baud_select_combo.grid(row=0, column=1)

        self.data_select_combo = ttk.Combobox(self.frame, state="readonly");
        self.data_select_combo['values'] = ('7', '8');
        self.data_select_combo.current(1)
        self.data_select_combo.grid(row=1, column=1)

        self.stopB_select_combo = ttk.Combobox(self.frame, state="readonly");
        self.stopB_select_combo['values'] = ('1', '2');
        self.stopB_select_combo.current(0)
        self.stopB_select_combo.grid(row=2, column=1)

        self.parity_select_combo = ttk.Combobox(self.frame, state="readonly");
        self.parity_select_combo['values'] = ('None', 'Odd','Even','Mark','Space');
        self.parity_select_combo.current(0)
        self.parity_select_combo.grid(row=3, column=1)

        list = list_ports.comports();
        self.to_connect_select_combo = ttk.Combobox(self.frame, state="readonly");
        self.to_connect_select_combo['values'] = (list);
        self.to_connect_select_combo.current(0)
        self.to_connect_select_combo.grid(row=4, column=1)

        self.button = tkinter.Button(self.frame,text="Connect",command=connect_callback);
        self.button.grid(row=5,columnspan=2)
        self.mainloop()


def connect_callback():
    print("H")

window = Window()
