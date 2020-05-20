from tkinter import*
from math import sqrt

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title('Py Calculator')
        #create screen widget
        self.screen = Text(master, state = 'disabled', width = 40, height = 4, background = "grey", foreground = "blue")
        #position screen in window
        self.screen.grid(row=0, column=0, columnspan = 4, padx = 5, pady = 5)
        self.screen.configure(state = 'normal')

        #initialize screen as empty
        self.equation = ''

        #create buttons using method createButton
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B", None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=', None, 34)

        #buttons stored in list
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

        #initialize counter
        count = 0 
        #arrange buttons with grid manager
        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count +=1
        #arrangelast button '=' at the bottom
        buttons[16].grid(row=5, column=0, columnspan=4)
    def createButton(self, val, write = True, width = 7):
        #this func creates a button, and takes one compulsory argument, the value that should be on the button
        return Button(self.master, text = val, command = lambda: self.click(val, write), width = width)
    def click(self, text, write):
        if write == 'None':
            if text == '=' and self.equation:
                self.equation=re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline = True)
            elif text == u"\u232B":
                self.clear_screen()
        else:
             self.insert_screen(text)
    def clear_screen(self):
        self.equation= ''
        self.screen.configure(state = 'normal')
        self.screen.delete('1.0', END)
    def insert_screen(self, value, newline = False):
            self.screen.configure(state = 'normal')
            self.screen.insert(END, value)

            self.equation +=str(value)
            self.screen.configure(state = 'disabled')

root = Tk()
my_gui = Calculator(root)
root.mainloop()

'''
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
 
        self.button = Button(frame, text="Quit", fg = "red", bg = 'white', command=frame.quit, padx = 3, pady  = 3)
        self.button.pack(side =LEFT)

        self.hi_there = Button(frame, text = "Our Prayer",image ='', command = self.say_hi, padx = 3, pady  = 3)
        self.hi_there.pack(side = LEFT)
        self.save_us = Button(frame, text = 'QuadRoot', command =self.sam, padx = 3, pady  = 2)
        self.save_us.pack(side=BOTTOM)
       

    def say_hi(self):
        print("Save us Lord from COVID-19")
    def sam(self):
        a = float(input('a= ?'))
        b = float(input('b= ?'))
        c = float(input('c= ?'))
        x, y = (-b + sqrt(a**2 - 4*a*c))/(2*a), ( -b - sqrt(a**2 - 4*a*c))/(2*a)
        print(x, y)
    

root = Tk() 
app = App(root)
root.mainloop()
'''



'''
root = Tk()
w = Label(root, text = 'Hello, Jesus Christ!')
w.pack()
root.mainloop()

'''

