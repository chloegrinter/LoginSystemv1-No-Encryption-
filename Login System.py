
import sys
user = ' '
passw = ' '
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
            
    else:
        print('Incorrect Username or Password.')
        print('|--------------------------------|')
       
for i in range(0,5):
    if passw == 'supersecurepassword': 
        sys.exit()
    else:
        user = usernameinput()
        passw = passwordinput()
        adminverify(user, passw)


