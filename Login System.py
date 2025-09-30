
import sys

def usernamestartup():
    print('Input Your Username and Password')
    print('|--------------------------------|')

def usernameinput():
    username = input('Username: ')
    print('|--------------------------------|')
    return username
    
def passwordinput():
    password = input('Password: ')
    print('|--------------------------------|')
    return password

def adminverify(username, password):
    if username == 'ADMIN1':
        if password == 'supersecurepassword':
            print('Logged In. Welcome')
            print('|--------------------------------|')
        else:
            print('Incorrect Username or Password.')
            print('|--------------------------------|')
            sys.exit()
    else:
        print('Incorrect Username or Password.')
        print('|--------------------------------|')
        sys.exit()
user = usernameinput()
passw = passwordinput()
adminverify(user, passw)
