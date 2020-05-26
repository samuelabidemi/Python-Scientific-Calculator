import tkinter as tk
import math as m
import numpy as np
import sympy as sym
import statistics as st
from functools import reduce
import scipy
'''
This is a scientific calculator built using python -n-built libraries- Tkinter, math and statistics- and external libraries
viz: numpy and sympy. The various buttons are the functionalities of the calculator. 




'''
btn_paremeters = {
    'padx': 1,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': 'grey',
    'font': ('arial', 10),
    'width': 6,
    'height': 2,
    'relief': 'ridge',
    'activebackground': "#666666"
}

btn_paremeters_2 = {
    'padx': 1,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': 'powder blue',
    'font': ('arial', 10),
    'width': 6,
    'height': 2,
    'relief': 'ridge',
    'activebackground': "#666666"
}
btn_paremeters_3 = {
    'padx': 1,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': 'pink',
    'font': ('arial', 10),
    'width': 6,
    'height': 2,
    'relief': 'ridge',
    'activebackground': "#666666"
}
global const
const = 180
pi = 22/7
def Sin(x):
        return m.sin(x * (const/180))
def Cos(x):
        return m.cos(x*const)
def Tan(x):
        return m.tan(x)
def Floor(x):
        return m.floor(x)
def Ceil(x):
        return m.ceil(x)
def ArcSin(x):
        return m.acos(x)
def ArcCos(x):
        return m.acos(x)
def ArcTan(x):
        return m.atan(x)
def GCD(x,y):
        if x> y:
                return m.gcd(x, y)
        else:
                return m.gcd(y,x)
def fmod(x, y):
        return m.fmod(x, y)


def Factorial(x):
        return m.factorial(x)

def Sqrt(x):
        return m.sqrt(x)

def Log(x):
        return m.log(x)  

def perm(x, y):
        if x>=y:
                return Factorial(x)/Factorial(x-y)
        else:
                return 'Incorrect input!'
def comb(x, y):
        if x>=y:
                return Factorial(x)/(Factorial(x-y)*Factorial(y))
        else:
                return 'Wrong input'
def angle_conversion(x):
        pass
        


class Sci_Calculator:
    def __init__(self, master):
   
        self.master = master
        master.title('Scientific Calculator')        #name of Calculator
                                                     #self-equation to store values
        self.expression = ""

        self.result = ""
        self.input_txt = tk.StringVar()
        self.recall = ''
        self.sum_up = ''
        

        #Mainframe
        MainFrame = tk.Frame(self.master, bg = 'gray')
        MainFrame.place(relx=0.1, rely=0.1, relwidth = 0.8, relheight=0.8)

        #frame for the display   
        top_frame = tk.Frame(MainFrame, height = 50, width = 100, bg = 'yellow', relief = 'groove', bd = 4 )
        top_frame.pack(side = tk.TOP)

        #the frame for the buttons
        bottom_frame = tk.Frame(MainFrame,height = 700, width = 100, bg= 'grey')
        bottom_frame.pack(side=tk.TOP)
       

        #display on screen
        self.screen = tk.Entry(top_frame, width = 60, background = "grey", foreground = "white", textvariable=self.input_txt, bd = 5, justify ='right' , cursor = 'tcross')
        self.screen.pack()
       
        
#Row 3
        #factorial button
        self.mod = tk.Button(bottom_frame, text = 'n!',  **btn_paremeters, command = lambda:self.btn_click('Factorial('))
        self.mod.grid(row=3, column = 0)

        #cube root button
        self.cube_root = tk.Button(bottom_frame, text = '₃√',  **btn_paremeters, command = lambda:self.btn_click('**(1/3)'))
        self.cube_root.grid(row=3, column = 1)

        #cube button
        self.cube = tk.Button(bottom_frame, text = 'x^3',  **btn_paremeters,command = lambda: self.btn_click('**3'))
        self.cube.grid(row=3, column = 2)

        #Author button
        self.ntn = tk.Button(bottom_frame, text = 'Author',  **btn_paremeters, command = lambda:self.btn_click('Osikoya Samuel'))
        self.ntn.grid(row=3, column = 3)

        #antilog button
        self.pwr10 = tk.Button(bottom_frame, text = '10^x',  **btn_paremeters, command = lambda: self.btn_click('10**') )
        self.pwr10.grid(row=3, column = 4)

        #exponential button
        self.exp = tk.Button(bottom_frame, text = 'e^x',  **btn_paremeters, command = lambda:self.btn_click('m.exp('))
        self.exp.grid(row=3, column = 5)

#Row  4
        #fraction button
        self.frac = tk.Button(bottom_frame, **btn_paremeters, text = 'x/y', command ='', )
        self.frac.grid(row = 4, column = 0)

        #square root button
        self.rootx = tk.Button(bottom_frame, **btn_paremeters, text = '√x', command =lambda : self.btn_click('Sqrt(') )
        self.rootx.grid(row = 4, column = 1)
        
        #square button
        self.xsquared = tk.Button(bottom_frame, **btn_paremeters, text = 'x^2', command =lambda : self.btn_click('**2'),  )
        self.xsquared.grid(row = 4, column = 2)

        #power button
        self.xpwr = tk.Button(bottom_frame, **btn_paremeters, text = 'x^n', command =lambda : self.btn_click('**') )
        self.xpwr.grid(row = 4, column = 3)
        #base 10 log button
        self.log = tk.Button(bottom_frame, **btn_paremeters, text = 'log', command =lambda : self.btn_click('Log('),  )
        self.log.grid(row = 4, column = 4)

        #natural log button
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text = 'ln', command =lambda : self.btn_click('ln('))
        self.btn_ln.grid(row = 4, column = 5)
        
#Row 5
        #x button
        self.alpah_a = tk.Button(bottom_frame, text = 'x',**btn_paremeters, command = lambda: self.btn_click('x'))
        self.alpah_a.grid(row=5, column = 0)

        #y button
        self.fact_b = tk.Button(bottom_frame, text = 'y', **btn_paremeters,  command = lambda: self.btn_click('y'))
        self.fact_b.grid(row=5, column = 1)

        #help button
        self.help_btn = tk.Button(bottom_frame, text = 'HELP', **btn_paremeters, command =lambda :self.btn_click('visit www.mathsgem.wordpress.com for help'))
        self.help_btn.grid(row=5, column = 2)

        #sine inverse button
        self.sin_inv_btn = tk.Button(bottom_frame, text = 'Sin^-1', **btn_paremeters,  command = lambda: self.btn_click('Arcsin('))
        self.sin_inv_btn.grid(row=5, column = 3)

        #cosine inverse button
        self.cos_inv_btn = tk.Button(bottom_frame, text = 'Cos^-1', **btn_paremeters,  command = lambda: self.btn_click('Arcos('))
        self.cos_inv_btn.grid(row=5, column = 4)

        # tan inverse button
        self.tan_inv_btn = tk.Button(bottom_frame, text = 'Tan^-1',**btn_paremeters, command = lambda: self.btn_click('Arctan('))
        self.tan_inv_btn.grid(row=5, column = 5)

#Row  6
        #enclosed minus button
        self.enclosed_minus_btn = tk.Button(bottom_frame, **btn_paremeters, text = '( - )', command = lambda:self.btn_click('(-'), )
        self.enclosed_minus_btn.grid(row = 6, column = 0)

        #degree conversion button
        self.angles_btn = tk.Button(bottom_frame, **btn_paremeters, text = 'o \' \"', command ='' )
        self.angles_btn.grid(row = 6, column = 1)

        #hyperbolic fucntion button
        self.hyp_btn = tk.Button(bottom_frame, **btn_paremeters_3, text = 'hyp', command = self.hyp,  )
        self.hyp_btn.grid(row = 6, column = 2)

        #sine button
        self.Sin_btn= tk.Button(bottom_frame, **btn_paremeters, text = 'Sin', command = lambda: self.btn_click('Sin('))
        self.Sin_btn.grid(row = 6, column = 3)

        #cosine button
        self.cos_btn = tk.Button(bottom_frame, **btn_paremeters, text = 'Cos', command =lambda : self.btn_click('cos(')  )
        self.cos_btn.grid(row = 6, column = 4)

        #tan button
        self.btn_tan = tk.Button(bottom_frame, **btn_paremeters, text = 'Tan', command =lambda : self.btn_click('Tan(') )
        self.btn_tan.grid(row =6, column = 5)



#Row  8
        #equation solver function
        self.eqn = tk.Button(bottom_frame, **btn_paremeters_3, text = 'EQN', command = self.equation_solver, )
        self.eqn.grid(row = 8, column = 0)

        #algebra function button
        self.eng_btn = tk.Button(bottom_frame, **btn_paremeters_3, text = 'Alg', command = self.Alg)
        self.eng_btn.grid(row = 8, column = 1)
        
        #left bracket
        self.left_brac = tk.Button(bottom_frame, **btn_paremeters, text = '(', command = lambda:self.btn_click('(')  )
        self.left_brac.grid(row = 8, column = 2)

        #right bracket
        self.right_brac = tk.Button(bottom_frame, **btn_paremeters, text = ')', command =lambda:self.btn_click(')'))
        self.right_brac.grid(row = 8, column = 3)

        #standard form button
        self.sd = tk.Button(bottom_frame, **btn_paremeters, text = 'sd', command ='',  )
        self.sd.grid(row = 8, column = 4)

        #
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text = 'M+', command ='' )
        self.btn_ln.grid(row = 8, column = 5)

 #Row 9
        #statistics function button
        self.stat = tk.Button(bottom_frame, text = 'STAT', **btn_paremeters_3, command = self.Stat)
        self.stat.grid(row=9, column = 0)

        #Roots function button
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters_3, text = 'Roots', command =self.Roots )
        self.btn_ln.grid(row = 9, column = 1)

        #LCM function button
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters_3, text = 'LCM', command = self.LCM )
        self.btn_ln.grid(row = 9, column = 2)

        #polynomial  button
        self.polyn = tk.Button(bottom_frame, text = 'Pol  ', **btn_paremeters)
        self.polyn.grid(row=9, column = 3)

        #ceiling function button
        self.floor = tk.Button(bottom_frame, text = 'Ceil', **btn_paremeters,  command= lambda: self.btn_click('Ceil('))
        self.floor.grid(row=9, column = 4)

        #floor function button
        self.floor = tk.Button(bottom_frame, text = 'Floor', **btn_paremeters,  command= lambda: self.btn_click('Floor('))
        self.floor.grid(row=9, column = 5)

       
#Row  10
        #matrix function button
        self.matrix_btn = tk.Button(bottom_frame, text = 'MATRIX', **btn_paremeters_3, command = self.matrix)
        self.matrix_btn.grid(row=10, column = 0)

        #vector function button
        self.vec_btn = tk.Button(bottom_frame, text = 'VECTOR', **btn_paremeters_3)
        self.vec_btn.grid(row=10, column = 1)

        #calculus function 
        self.cube = tk.Button(bottom_frame, text = 'Calc', **btn_paremeters_3, command= self.Calc)
        self.cube.grid(row=10, column = 2)

        #permutation button
        self.perm_btn= tk.Button(bottom_frame, text = 'nPr', **btn_paremeters, command = lambda: self.btn_click('perm('))
        self.perm_btn.grid(row=10, column = 3)

        #combination button
        self.comb_btn = tk.Button(bottom_frame, text = 'nCr', **btn_paremeters, command = lambda: self.btn_click('comb('))
        self.comb_btn.grid(row=10, column = 4)

        #exponential button
        self.exp = tk.Button(bottom_frame, text = 'e^x', **btn_paremeters, command = self.btn_click('m.exp('))
        self.exp.grid(row=10, column = 5)

        
 #Row 11
        #seven button
        self.seven_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '7', command = lambda:self.btn_click('7'), )
        self.seven_btn.grid(row = 11, column = 0)

        #eight button
        self.eight_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '8', command = lambda:self.btn_click('8'))
        self.eight_btn.grid(row = 11, column = 1)
        

        #nine button
        self.nine_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '9', command =lambda:self.btn_click('9'),  )
        self.nine_btn.grid(row = 11, column = 2)

        #delete function button
        self.Del_btn = tk.Button(bottom_frame, **btn_paremeters, text = 'DEL', command =self.btn_clear )
        self.Del_btn.grid(row = 11, column = 3)

        #clear all button
        self.Ac_btn = tk.Button(bottom_frame, **btn_paremeters, text = 'AC', command = self.btn_clearAll,  )
        self.Ac_btn.grid(row = 11, column = 4)

        #GCD function button
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text = 'GCD', command = lambda: self.btn_click('GCD(') )
        self.btn_ln.grid(row = 11, column = 5)

       
#Row  12
        #four button
        self.four_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '4', command =lambda:self.btn_click('4'), )
        self.four_btn.grid(row = 12, column = 0)

        #five button
        self.five_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '5', command =lambda:self.btn_click('5') )
        self.five_btn.grid(row = 12, column = 1)
        
        #six button
        self.six_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '6', command =lambda:self.btn_click('6'),  )
        self.six_btn.grid(row = 12, column = 2)

        #multiplication button
        self.times_btn = tk.Button(bottom_frame, **btn_paremeters, text = 'x', command =lambda:self.btn_click('*') )
        self.times_btn.grid(row = 12, column = 3)

        #division button
        self.div_btn = tk.Button(bottom_frame, **btn_paremeters, text = '/', command =lambda:self.btn_click('/'),  )
        self.div_btn.grid(row = 12, column = 4)

        #complex function button
        self.complx = tk. Button(bottom_frame, text = 'CMPLX',**btn_paremeters, command = '')
        self.complx.grid(row=12, column = 5)
 #Row 13
       

#Row  14
        #one button
        self.one_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '1', command =lambda:self.btn_click('1'), )
        self.one_btn.grid(row = 14, column = 0)

        #two button
        self.two_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '2', command =lambda:self.btn_click('2') )
        self.two_btn.grid(row = 14, column = 1)
        
        #three button
        self.three_btn = tk.Button(bottom_frame, **btn_paremeters_2, text = '3', command =lambda:self.btn_click('3'),  )
        self.three_btn.grid(row = 14, column = 2)

        #plus button
        self.plus_btn = tk.Button(bottom_frame, **btn_paremeters, text = '+', command =lambda:self.btn_click('+') )
        self.plus_btn.grid(row = 14, column = 3)

        #minus button
        self.minus_btn = tk.Button(bottom_frame, **btn_paremeters, text = '-', command =lambda:self.btn_click('-'),  )
        self.minus_btn.grid(row = 14, column = 4)

        #Distribution button
        self.distr = tk.Button(bottom_frame, text = 'DISTR', **btn_paremeters)
        self.distr.grid(row=14, column = 5)
        
#Row  16
        #zero button
        self.zero_btn = tk.Button(bottom_frame, **btn_paremeters, text = '0', command =lambda:self.btn_click('0'), )
        self.zero_btn.grid(row = 15, column = 0)

        #dot button
        self.dot_btn = tk.Button(bottom_frame, **btn_paremeters, text = '.', command =lambda:self.btn_click('.') )
        self.dot_btn.grid(row = 15, column = 1)
        

        #comma button
        self.exp_btn = tk.Button(bottom_frame, **btn_paremeters, text = ',',command=lambda:self.btn_click(','),  )
        self.exp_btn.grid(row = 15, column = 2)

        #Ans button
        self.ans_btn = tk.Button(bottom_frame, **btn_paremeters, text = 'Ans', command =self.Answer )
        self.ans_btn.grid(row = 15, column = 3)

        #equal button
        self.equal_btn = tk.Button(bottom_frame, **btn_paremeters, text = '=', command =self.btn_equal,  )
        self.equal_btn.grid(row = 15, column = 4)
        
        #mod n button
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text = 'mod n', command =lambda :self.btn_click('fmod('))
        self.btn_ln.grid(row = 15, column = 5)

        #function for statisticsq
    def Stat(self): 
        print('Choose task to perform:\n1. Mean \n2. Mode\n3. Median\n4. Standard Deviation\n5. Variance')
        choice = float(input('Enter the appropriate number:'))
        if choice ==1:  #calculates mean
                list_1 = []
                list_2 = []
                x = input('Enter data points separated by a space: ')
                list_1 = x.split()
                for i in list_1:
                        list_2.append(float(i))
                print('The mean is ', sum(list_2)/len(list_2))        
                
        elif choice ==2: #calculates mode
                list_1 = []
                list_2 = []
                x = input('Enter data points separated by a space: ')
                list_1 = x.split()
                for i in list_1:
                        list_2.append(float(i))
                print('The mode is/are', st.mode(list_2))
        elif  choice ==3:
                list_1 = []
                list_2 = []
                x = input('Enter data points separated by a space: ')
                list_1 = x.split()
                for i in list_1:
                        list_2.append(float(i))
                print('The median is', st.median_grouped(list_2))
        elif choice ==4:#calculates standard deviation
                list_1 = []
                list_2 = []
                list_3=  []
                list_4 = []
                a = input('Is the frequecy? y/n: ')
                if a == 'y' or a == 'Y':
                        x = input('Enter data points separated by a space: ')
                        list_1 = x.split()
                        for i in list_1: # to convert the string to floats
                                list_2.append(int(i)) # list of data points
                        y = input('Enter the frequncy of each data point accordinnly separated by space:')
                        list_3 = y.split()
                        for j in list_3: # to convert the string to floats
                                list_4.append(int(j)) # list of frequency
                        c = [(x*y) for x,y in zip(list_2, list_4)]
                        d = sum(c)/ sum(list_4) # the mean
                        e = [(k - d)**2 for k in list_2 ] # list of the square of the devation
                        f = [(m*n) for m,n in zip(list_4, e)] #list of the product of the frequency and the deviation
                        print('The standard deviation is', m.sqrt(sum(f)/sum(list_4)))

                elif a =='N' or a =='n':
                        list_1 = []
                        list_2 = []
                        x = input('Enter data points separated by a space: ')
                        list_1 = x.split()
                        for i in list_1:
                                list_2.append(int(i))
                        d = sum(list_2)/len(list_2)
                        list_3 = [(k - d)**2 for k in list_2]
                        print('The standard deviation is ', m.sqrt(sum(list_3)/len(list_2)))
        elif choice ==5:  #calculates variance
                list_1 = []
                list_2 = []
                list_3= []
                list_4 = []
                a = input('Is the frequecy? y/n: ')
                if a == 'y' or a == 'Y':
                        x = input('Enter data points separated by a space: ')
                        list_1 = x.split()
                        for i in list_1: # to convert the string to floats
                                list_2.append(int(i)) # list of data points
                        y = input('Enter the frequncy of each data point accordinnly separated by space:')
                        list_3 = y.split()
                        for j in list_3: # to convert the string to floats
                                list_4.append(int(j)) # list of frequency
                        c = [(x*y) for x,y in zip(list_2, list_4)]
                        d = sum(c)/ sum(list_4) # the mean
                        e = [(k - d)**2 for k in list_2 ] # list of the square of the devation
                        f = [(m*n) for m,n in zip(list_4, e)] #list of the product of the frequency and the deviation
                        print('The variance is', sum(f)/sum(list_4))
                elif a =='N' or a =='n':
                        list_1 = []
                        list_2 = []
                        x = input('Enter data points separated by a space: ')
                        list_1 = x.split()
                        for i in list_1:
                                list_2.append(int(i))
                        d = sum(list_2)/len(list_2)
                        list_3 = [(k - d)**2 for k in list_2]
                        print('The variance is ', sum(list_3)/len(list_2))
        else:
                print('Wrong input!')

        #function to expand and simplify algebraic expressions
    def Alg(self):
        #declared variables
        a, b, c ,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = sym.symbols('a, b, c ,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
        print('Choose task to perform:\n1. Expand \n2. Simplify')
        self.choice = float(input('Entter the task to perform enclosed in even parentheses:'))
        #expands algebraic expressions e.g (x + y)**5
        if self.choice ==1:
                expression = input('Enter the expression to expand: ')
                print(sym.expand(expression))
        #simplifes algebraic expressions
        elif self.choice ==2:
                expression = input('Enter the expression to expand: ')
                print(sym.simplify(expression))
        else:
                print('Wrong Input!')



        #function to find the limits, derivative,  and integral of single variable functions
    def Calc(self):
        #declaration of all possible variables
        a, b, c ,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = sym.symbols('a, b, c ,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
        print('Choose the task to perform:\n1.Derivative \n2. Limits \n3. Improper Integral \n4. Definite Integral')
        self.choice = float(input('Enter the nnumber here: ')) #user's task to perform
        
        #derivate of function
        if self.choice ==1:
                expression = input('Enter the function to differentiate: ')
                var_of_func = input('Enter the variable e.g x, y or z: ')
                order_of_dydx = input('Enter the order of the derivative eig 1, 2, or 3:')
                print(sym.diff(sym.simplify(expression), var_of_func, order_of_dydx))

        #limit of fucnction
        elif self.choice == 2:
                
                expression = input('Enter the expression of limit: ')
                var_of_func = input('Enter the variable e.g x, y or z: ')
                pt_of_limit = input('Enter the point of limit. If point of limit is infinity please enter d: ')
                
                print(sym.limit(sym.simplify(expression), var_of_func, pt_of_limit))

        #integral of function
        elif self.choice ==3:
               expression = input('Enter the expression to inegrate beginning special functions with sym. e.g sin(x) as sym.sin(x):  ')
               var_of_func = input('Enter the variable e.g x, y or z: ')
               print(sym.integrate(sym.simplify(expression)))

        #definite integral
        elif self.choice == 4:
                expression = input('Enter the expression to inegrate beginning special functions with sym. e.g sin(x) as sym.sin(x)')
                var_of_func = input('Enter the variable e.g x, y or z: ')
                lower_limit = input('Enter the value of the lower limit:')
                upper_limit = input('Enter the value of the upper limit:')
                print(sym.integrate(sym.simplify(expression), (var_of_func, lower_limit, upper_limit)))
        else:
                print('Wrong Input')

        #fucntion to find the roots of polynomial equations
    def Roots(self):
            a = []
            b = []
            c = input('Enter the coeeficients of the polynomial in ascending powers of the variable separated by space: ')
            a = c.split()
            for i in a:
                    b.append(float(i))
            v = np.polynomial.Polynomial(b)
            print(v.roots())


        #function to find the lcm of denominator
    def LCM(self):
            
            a = []
            b = []
            c = input('Enter the the numbers (max of 7 numbers) separated by a space: ') #accepts the denominators
            a =  c.split()
            for i in a:
                b.append(int(i)) 
            arr = np.array(b)
            print(np.lcm.reduce(arr)) #prints the lcm

        #Matrix function
    def matrix(self):
            ''' This fucntion evaluates the product, inverse and determinant of matrices
             '''

            print('Choose task to perform:\n1. Matrix Multiplication\n2. Determinant of Matrix\n3. Inverse of Matrix')
            self.choice = int(input('Enter the task to pperfom eg 1,2 3'))
            if self.choice ==1:
                    print('How manny matrices for multip[l;ication(min of 2 and max 0f 4)?')
                    choice = int(input('Enter the number of matrices here: '))
                    if choice ==2:
                        R_1 = int(input('Enter the number of rows for the first matrix: '))#function for statistics#function for statistics
                        C_1 = int(input('Enter the number of columns for the first matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_1 = list(map(float, input().split())) #accepts all the elements in matrix on a single line

                        R_2 = int(input('Enter the number of rows for the 2nd matrix: '))
                        C_2 = int(input('Enter the number of columns for the 2nd matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_2 = list(map(float, input().split()))


                        matrix_1 = np.array(entries_1).reshape(R_1, C_1)
                        matrix_2 = np.array(entries_2).reshape(R_2, C_2)
                        print(sym.Matrix(matrix_1)*sym.Matrix(matrix_2))

                    elif choice==3:
                        R_1 = int(input('Enter the number of rows for the first matrix: '))
                        C_1 = int(input('Enter the number of columns for the first matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_1 = list(map(float, input().split()))

                        R_2 = int(input('Enter the number of rows for the 2nd matrix: '))
                        C_2 = int(input('Enter the number of columns for the 2nd matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_2 = list(map(float, input().split()))

                        R_3 = int(input('Enter the number of rows for the 3RD matrix: '))
                        C_3 = int(input('Enter the number of columns for the 3RD matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_3 = list(map(float, input().split()))

                        matrix_1 = np.array(entries_1).reshape(R_1, C_1)
                        matrix_2 = np.array(entries_2).reshape(R_2, C_2)
                        matrix_3 = np.array(entries_3).reshape(R_3, C_3)
                        print(sym.Matrix(matrix_1)*sym.Matrix(matrix_2)*sym.Matrix(matrix_3))

                    elif choice ==4:
                        R_1 = int(input('Enter the number of rows for the first matrix: '))
                        C_1 = int(input('Enter the number of columns for the first matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_1 = list(map(float, input().split()))

                        R_2 = int(input('Enter the number of rows for the 2nd matrix: '))
                        C_2 = int(input('Enter the number of columns for the 2nd matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_2 = list(map(float, input().split()))

                        R_3 = int(input('Enter the number of rows for the 3RD matrix: '))
                        C_3 = int(input('Enter the number of columns for the 3RD matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_3 = list(map(float, input().split()))

                        R_4 = int(input('Enter the number of rows for the 3RD matrix: '))
                        C_4 = int(input('Enter the number of columns for the 3RD matrix: '))
                        print('Enter all entries(row-wise) in a single line separated by space: ')
                        entries_4 = list(map(float, input().split()))

                        matrix_1 = np.array(entries_1).reshape(R_1, C_1)
                        matrix_2 = np.array(entries_2).reshape(R_2, C_2)
                        matrix_3 = np.array(entries_3).reshape(R_3, C_3)
                        matrix_4 = np.array(entries_4).reshape(R_4, C_4)

                        print(sym.Matrix(matrix_1)*sym.Matrix(matrix_2)*sym.Matrix(matrix_3)*sym.Matrix(matrix_4))
                        
            elif self.choice==2:
                R_1 = int(input('Enter the number of rows for the first matrix: '))
                C_1 = int(input('Enter the number of columns for the first matrix: '))
                print('Enter all entries(row-wise) in a single line separated by space: ')
                entries = list(map(float, input().split()))
                matrix_1 = np.array(entries).reshape(R_1, C_1)
                print(round(np.linalg.det(matrix_1), 2))
                
            elif self.choice ==3:
                R_1 = int(input('Enter the number of rows for the first matrix: '))
                C_1 = int(input('Enter the number of columns for the first matrix: '))
                print('Enter all entries(row-wise) in a single line separated by space: ')
                entries = list(map(float, input().split()))
                matrix_1 = np.array(entries).reshape(R_1, C_1)
                print(np.linalg.inv(matrix_1))

    def equation_solver(self):
        '''This function solves linear system of equations  '''


        R_1 = int(input('Enter the number of equations: '))
        C_1 = int(input('Enter the number of unknowns: '))
        print('Enter all coefficients(row-wise) in a single line separated by space: ')
        entries_1 = list(map(float, input().split())) #gets matrix input from user
        R_2 = R_1
        C_2 = int(input('Enter 1: '))
        print('Enter all the constants of the equations accordingly: ')
        entries_2 = list(map(float, input().split()))
        matrix_1 = np.array(entries_1).reshape(R_1, C_1)
        matrix_2 = np.array(entries_2).reshape(R_2, C_2)
        print(np.linalg.inv(matrix_1)*sym.Matrix(matrix_2))

        #to display items on screen
    def btn_click(self, x):
        if len(self.expression)>=100:
            self.expression = self.expression
            self.input_txt.set(self.expression)
        else:
            self.expression = self.expression + str(x)
            self.input_txt.set(self.expression)
    
        
        #for backspace
    def btn_clear(self):
        self.expression = self.expression[:-1]
        self.input_txt.set(self.expression)

        #evaluate expressions on screen 
    def btn_equal(self):
        self.result = str(eval(self.expression))
        self.expression = self.result
        self.input_txt.set(self.expression)

        #clears all expressions screen
    def btn_clearAll(self):
        self.expression =""
        self.input_txt.set(self.expression)
    def hyp(self):
        choice = int(input('1.sinh\n2.cosh\n3.tanh'))
        if choice==1:
                user_entry= float(input('Enter number: '))
                print(m.sinh(user_entry))
        elif choice==2:
                user_entry= float(input('Enter number: '))
                print(m.cosh(user_entry))
        elif choice==3:
                user_entry= float(input('Enter number: '))
                print(m.sinh(user_entry))
        else:
                print('Wrong input!')

    def Answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.input_txt.set(self.expression)

    # uses whatever is stored in memory_recall

    def memory_recall(self):
        if self.expression == "":
            self.input_txt.set('0' + self.expression + self.recall)
        else:
            self.input_txt.set(self.expression + self.recall)


    

root = tk.Tk()
first_gui = Sci_Calculator(root)
root.geometry('')
root.mainloop()