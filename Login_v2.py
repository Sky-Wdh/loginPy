import time,sys,random

DataSaveNotfi = [
    'Verifying Id...',
    'Verifying Password...',
    'Further verification in progress...',
    'Almost done...',
]
# hello
Menus = [
    'Sign up',
    'Log in',
    'Change Id',
    'Change Password',
]

UserData = {} # Id : Password

def SignUp_ID():
    Id = input('Make your Id : ')
    for check in UserData.keys():
        if check == Id:
            return print(("\033[1;31m%s\033[0m")%'This ID already exists.'),SignUp_ID()
    SignUP_Password(Id)
    
def SignUP_Password(Id):
    Password = input('Make your Password : ')
    RePassword = input('Enter password again : ')
    if Password != RePassword:
        return print(("\033[1;31m%s\033[0m")%'The password is incorrect!'), SignUP_Password(Id)
    for msg in DataSaveNotfi:
        print(msg)
        time.sleep(random.randint(1,3))
    for per in range(0,101):
        time.sleep((random.randint(1,5))/(30+(per//2)))
        print(f'Progress: {per}%', end = '\r')
    UserData[Id] = Password
    print(("\033[1;32m%s\033[0m")%'Data saved Successfully!')
    Lobby()

def Log_in_Id():
    Id = input('Enter your Id : ')
    Ids = UserData.keys()
    if not Id in Ids:
        return print("\033[1;31mCan't find Id : %s\033[0m"%Id), Log_in_Id()
    Log_in_Password(Id)

def Log_in_Password(Id):
    Password = input('Enter your Password : ')
    if UserData[Id] != Password:
        return print("\033[1;31m%s\033[0m"%"Password is incorrect."), Log_in_Password(Id)
    print(("\033[1;32mWelcome, %s\033[0m")%Id)
    Lobby()

def Lobby():
    print('<Menu list>')
    for i in Menus:
        print(f'- {i}')
    Choose = input('Enter the menu: \n').lower()
    Choose.replace(' ', '')
    if Choose == 'signup':
        SignUp_ID()
    elif Choose == 'login':
        Log_in_Id()
    else:
        print("\033[1;31m%s\033[0m"%'This Menu is currently not support!')
        Lobby()
Lobby()