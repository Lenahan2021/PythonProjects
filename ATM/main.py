from Customer import Customer
import sys
card = None
pin = None
loginTries = 2
transactions = 3
transferChoice = None
transferAmount = None

customers=[]
customer = None
loggedIn = False

def load():
    global customers
    with open('db.csv', 'r') as f:
        file = f.readlines()
        for i in range(len(file)):
            file[i] = file[i].rstrip()
            name, savings, checking, card, pin = file[i].split(',')
            if float(savings) > 10: 
                customers.append(Customer(name, checking, savings, card, pin))
    print('LoadingComplete')



def write():
    file = []
    global customers
    for i in customers:
        file.append(f'{i.name},{i.saving},{i.checking},{i.card},{i.pin}\n')
    print(file)
    with open('db.csv', 'w') as f:
        f.writelines(file)
    print('file was written')
    customers = []

def deposit(depositAmount):
    global customer
    global transactions
    if transactions > 0:
        customer.checking += depositAmount
        return 'ok'
    else:
        return 'transactions'
def changePin(pin):
    global customer
    if len(str(pin)) == 4:
        customer.pin = pin
        return 'ok'
    else:
        return 'invalid'

def withdrawal(amount):
    global customer
    global transactions
    if transactions > 0:
        if (not (amount > 500)) and (customer.checking - amount > 0):
            if amount % 5 != 0:
                return "%5"
            else:
                transactions -=1
                customer.checking -= amount
                return 'good'
        else:
            return 'bad'
    else:
        return 'transactions'

def transferBalance(choice, balance):
    global customer
    global transactions
    if transactions > 0:
        if choice == 'Saving':
            if customer.saving - balance >= 10:
                customer.saving -= balance
                customer.checking += balance
                transactions -=1
                return 'ok'
            else:
                return 'no funds'
        elif choice == 'Checking':
            if customer.checking - balance > 0:
                customer.checking -= balance
                customer.saving += balance
                transactions -=1
                return 'ok'
            else:
                return 'no funds'
    else:
        return 'transactions'

def login(card, pin):
    global loginTries
    global loggedIn
    global customer
    global transactions
    if not loggedIn and loginTries > 0:
        for i in customers:
            if str(i.card) == card and str(i.pin) == pin:
                loggedIn = True
                transactions = 3
                loginTries = 3
                customer = i
                print('Welcome, ', customer.name)
                return loggedIn, customer
        if not loggedIn:
            loginTries -= 1
            return False, None
    else:
        print(loggedIn)
        sys.exit(0)

def logOut():
    global card
    global pin
    global customer
    global customers
    global loggedIn
    loggedIn = False
    customer = None
    pin= None
    card = None
    customers = []
load()