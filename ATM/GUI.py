from tkinter import *
from main import *

#https://www.codegrepper.com/code-examples/python/tkinter+call+function+in+mainloop

root = Tk()
root.wm_geometry('800x800')
root.title('ATM')
root.wm_resizable(False, False)
expression = ''

currentWindow = 'Login'

menuText = """WELCOME

What would you like to do?
L1 - Deposit
L2 - withdrawal
L3 - Change Pin
L4 - Transfer
R2 - Balance Inquiry
R3 - End Session

Press R1 to return to Menu at any time
"""

loginText="""Please Enter Card Number\n"""
def buttonClick(item):
    global expression
    global currentWindow
    global card
    global pin
    global customer
    global transferChoice
    if ('l' in item) or ('r' in item):
        if currentWindow == 'Menu':
            print(currentWindow)
            if item == 'l1':
                currentWindow = 'Deposit'
                print(currentWindow)
            elif item == 'l2':
                currentWindow = 'Withdrawal'
            elif item == 'l3':
                currentWindow = 'Pin'
            elif item =='l4':
                currentWindow ='Transfer'
            elif item == 'r2':
                currentWindow = 'Balance'
                balanceLbl.config(text=f'Current checking ${customer.checking}\n Current Saving ${customer.saving}')
            elif item == 'r3':
                currentWindow = 'End'
                card = None
                pin = None
                customer = None
        if currentWindow == 'Transfer' and transferChoice == None:
            if item == 'l1':
                transferChoice = 'Saving'
                transferLbl.config(text='How much would you like to transfer?')
            elif item == 'l2':
                transferChoice = 'Checking'
                transferLbl.config(text='How much would you like to transfer?')
    else:
        if not currentWindow =='Balance':
            expression+= item
        if currentWindow == 'Login':
            loginInput.config(text=expression)
        elif currentWindow == 'Deposit':
            depositInput.config(text=expression)
        elif currentWindow == 'Withdrawal':
            withdrawalInput.config(text=expression)
        elif currentWindow == 'Pin':
            pinInput.config(text=expression)
        elif currentWindow == 'Transfer':
            transferInput.config(text=expression)
        print(expression)

#https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter#:~:text=One%20way%20to%20switch%20frames,use%20any%20generic%20Frame%20class.
def raise_frame(frame):
    frame.tkraise()

def updateFrames():
    global currentWindow
    global expression
    if currentWindow == 'Login':
        raise_frame(loginFrame)
    elif currentWindow == 'Balance':
        raise_frame(balanceFrame)
    elif currentWindow == 'Deposit':
        raise_frame(depositFrame)
    elif currentWindow == 'Transfer':
        raise_frame(transferFrame)
    elif currentWindow == 'Withdrawal':
        raise_frame(withDrawalFrame)
    elif currentWindow =='Pin':
        raise_frame(pinFrame)
    elif currentWindow == 'Menu':
        raise_frame(menuFrame)
        resetAllLbls()
    elif currentWindow=='End':
        resetAllLbls()
        write()
        logOut()
        load()
        currentWindow ='Login'
    root.after(500,updateFrames)

def clearButton():
    global expression
    global currentWindow
    expression=''
    if currentWindow == 'Login':
        loginInput.config(text=expression)
    elif currentWindow == 'Deposit':
        depositInput.config(text=expression)
    elif currentWindow == 'Transfer':
        transferInput.config(text=expression)
    elif currentWindow == 'Withdrawal':
        withdrawalInput.config(text=expression)
    elif currentWindow =='Pin':
        pinInput.config(text=expression)

def back():
    global loggedIn
    global expression
    global currentWindow
    expression = ''
    if loggedIn:
        currentWindow='Menu'

def resetAllLbls():
    global expression
    depositLbl.config(text='Please input amount you would like to deposit')
    withdrawalLbl.config(text='Please input amount you would like to withdrawal')
    transferLbl.config(text='Where would you like to transfer from? \n Savings - L1 \n Checking - L2')
    pinLbl.config(text='What would you like your new pin to be?')
    loginLbl.config(text='Please enter card number')
    expression =''
    loginInput.config(text=expression)
    depositInput.config(text=expression)
    withdrawalInput.config(text=expression)
    transferInput.config(text=expression)
    pinInput.config(text=expression)

def confirmButton():
    global currentWindow
    global expression
    global card
    global pin
    global loggedIn
    global customer
    global transferChoice
    if currentWindow =='Login':
        if card == None:
            card = expression
            expression = ''
            loginInput.config(text=expression)
            loginLbl.config(text='Please enter Pin')
        elif pin == None:
            pin = expression
            expression = ''
            loggedIn, customer = login(card, pin)
            print(loggedIn)
            if loggedIn:
                currentWindow='Menu'
            else:
                loginLbl.config(text='Please enter Card')
                card = None
                pin = None
                expression =''
    elif currentWindow == 'Deposit':
        status = deposit(int(expression))
        if status == 'ok':
            depositLbl.config(text=f'Your new balance is: {customer.checking}')
        elif status == 'transactions':
            currentWindow = 'End'
    elif currentWindow == 'Transfer':
        if not transferChoice == None:
            status = transferBalance(transferChoice, int(expression))
            if status == 'ok':
                transferLbl.config(text='Successfully Transferred Funds')
                transferChoice = None
            elif status =='no funds':
                transferLbl.config(text='Not enough funds avaiable to transfer')
                transferChoice = None
            else:
                currentWindow = 'End'
    elif currentWindow == 'Withdrawal':
        status = withdrawal(int(expression))
        if status == 'good':
            withdrawalLbl.config(text=f'Your new balance is: {customer.checking}')
        elif status == '%5':
            withdrawalLbl.config(text='ATM can only withdrawal in $5 incremements')
        elif status =='bad':
            withdrawalLbl.config(text='Withdrawl Amount is too high, or insuffiect funds')
        elif status == 'transactions':
            currentWindow = 'End'
    elif currentWindow =='Pin':
        status = changePin(int(expression))
        if status =='ok':
            pinLbl.config(text=f'Your new pin is: {customer.pin}')
        else:
            pinLbl.config(text='Invalid pin')

def deleteButton():
    global expression
    expression = expression[0:len(expression)-1]
    if currentWindow == 'Login':
        loginInput.config(text=expression)
    elif currentWindow == 'Deposit':
        depositInput.config(text=expression)
    elif currentWindow == 'Transfer':
        transferInput.config(text=expression)
    elif currentWindow == 'Withdrawal':
        withdrawalInput.config(text=expression)
    elif currentWindow =='Pin':
        pinInput.config(text=expression)


loginFrame  = Frame(root,width=500,height=500,bd=0,highlightbackground='black',bg='black', highlightcolor='black',highlightthickness=1)
menuFrame = Frame(root,width=500,height=500,bd=0,highlightbackground='black', bg='black',highlightcolor='black',highlightthickness=1)
balanceFrame  = Frame(root,width=500,height=500,bd=0,highlightbackground='black', bg='black',highlightcolor='black',highlightthickness=1)
depositFrame = Frame(root,width=500,height=500,bd=0,highlightbackground='black', bg='black',highlightcolor='black',highlightthickness=1)
transferFrame  = Frame(root,width=500,height=500,bd=0,highlightbackground='black', bg='black',highlightcolor='black',highlightthickness=1)
withDrawalFrame = Frame(root,width=500,height=500,bd=0,highlightbackground='black', bg='black',highlightcolor='black',highlightthickness=1)
pinFrame = Frame(root,width=500,height=500,bd=0,highlightbackground='black', bg='black',highlightcolor='black',highlightthickness=1)

for frame in (loginFrame, menuFrame, balanceFrame, depositFrame,transferFrame, withDrawalFrame, pinFrame):
    frame.grid(row=0, column=0, sticky='news',padx=125)


loginLbl = Label(loginFrame,text=loginText, fg='#FFFFFF',width = 70, height=5, bg='#000000')
loginLbl.pack()
loginInput = Label(loginFrame, fg='#FFFFFF',width = 70, height=5, bg='#000000')
loginInput.pack()

menuLbl = Label(menuFrame,text=menuText, fg='#FFFFFF',width = 70, height=30, bg='#000000')
menuLbl.pack()

balanceLbl = Label(balanceFrame,text=f'Current checking\n CurrentSaving', fg='#FFFFFF',width = 70, height=5, bg='#000000')
balanceLbl.pack()

depositLbl = Label(depositFrame,text='Please input amount you would like to deposit', fg='#FFFFFF',width = 70, height=5, bg='#000000')
depositLbl.pack()
depositInput = Label(depositFrame,text=expression, fg='#FFFFFF',width = 70, height=5, bg='#000000')
depositInput.pack()

withdrawalLbl = Label(withDrawalFrame,text='Please input amount you would like to withdrawal', fg='#FFFFFF',width = 70, height=5, bg='#000000')
withdrawalLbl.pack()
withdrawalInput = Label(withDrawalFrame,text=expression, fg='#FFFFFF',width = 70, height=5, bg='#000000')
withdrawalInput.pack()

transferLbl = Label(transferFrame,text=f'Where would you like to transfer from? \n Savings - L1 \n Checking - L2',fg='#FFFFFF',width = 70, height=5, bg='#000000')
transferLbl.pack()
transferInput = Label(transferFrame,text=expression,fg='#FFFFFF',width = 70, height=5, bg='#000000')
transferInput.pack()

pinLbl = Label(pinFrame,text=f'What would you like your new pin to be?',fg='#FFFFFF',width = 70, height=5, bg='#000000')
pinLbl.pack()
pinInput = Label(pinFrame,text=expression,fg='#FFFFFF',width = 70, height=5, bg='#000000')
pinInput.pack()


leftFrame = Frame(root,width=100,height=300,bd=0,highlightbackground='black', highlightcolor='black')
leftFrame.place(x=20, y=60)
rightFrame = Frame(root,width=100,height=300,bd=0,highlightbackground='black', highlightcolor='black')
rightFrame.place(x=680, y=60)


buttonFrame = Frame(root,width=312, height=272.5)
buttonFrame.grid(row=1,column=0)

one = Button(buttonFrame,text='1', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('1')).grid(row=1, column=0, padx=1, pady=1)
two= Button(buttonFrame,text='2', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('2')).grid(row=1, column=1, padx=1, pady=1)
three= Button(buttonFrame,text='3', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('3')).grid(row=1, column=2, padx=1, pady=1)

four = Button(buttonFrame,text='4', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda:buttonClick('4')).grid(row=2, column=0, padx=1, pady=1)
five= Button(buttonFrame,text='5', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda:buttonClick('5')).grid(row=2, column=1, padx=1, pady=1)
six= Button(buttonFrame,text='6', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda:buttonClick('6')).grid(row=2, column=2, padx=1, pady=1)

seven = Button(buttonFrame, text='7', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('7')).grid(row=3, column=0, padx=1, pady=4)
eight = Button(buttonFrame, text='8', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('8')).grid(row=3, column=1, padx=1, pady=4)
nine = Button(buttonFrame, text='9', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('9')).grid(row=3, column=2, padx=1, pady=4)
zero = Button(buttonFrame, text='0', fg='black', width=10, height=3, bd=0, bg='#fff',command=lambda:buttonClick('0')).grid(row=4, column=1, padx=1, pady=4)

clear = Button(buttonFrame, text='CLEAR', fg='black',width=10, height=3, bd=0, bg='#FFFF00',command=clearButton)
clear.grid(row=2, column=3, padx=20)

enter = Button(buttonFrame, text='ENTER', fg='black',width=10, height=3, bd=0, bg='#00FF00',command=confirmButton)
enter.grid(row=3,column=3,padx=20)

delete = Button(buttonFrame, text='DELETE', fg='black',width=10, height=3, bd=0, bg='#FF0000',command=deleteButton)
delete.grid(row=1,column=3,padx=20)

r1 = Button(rightFrame, fg='black',command=back,text='R1', width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)
r2 = Button(rightFrame, fg='black',command=lambda:buttonClick('r2'),text='R2', width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)
r3 = Button(rightFrame, fg='black',command=lambda:buttonClick('r3'),text='R3', width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)
r4 = Button(rightFrame, fg='black', command=lambda:buttonClick('r4'),text='R4',width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)

l1 = Button(leftFrame, fg='black', command=lambda:buttonClick('l1'),text='L1',width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)
l2 = Button(leftFrame, fg='black', command=lambda:buttonClick('l2'),text='L2',width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)
l3 = Button(leftFrame, fg='black', command=lambda:buttonClick('l3'),text='L3',width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)
l4 = Button(leftFrame, fg='black', command=lambda:buttonClick('l4'),text='L4',width=10, height=3, bd=0, bg='#5a5a5a').pack(pady=10)


root.after(100,updateFrames)
root.mainloop()