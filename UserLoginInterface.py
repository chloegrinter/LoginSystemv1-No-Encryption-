import login
login.usernamestartup()
username = login.usernameinput()
password = login.passwordinput()
login.adminverify(username, password)
