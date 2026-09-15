## Inicio del Programa de login

username = input(" LOGIN  \n USERNAME : ")
def greeting():
    print(" HI ", username.upper(), " ! \n WELCOME BACK ! ")
greeting()


## Agregando nueva funcionalidad para el login
password = input(" PASSWORD : ")
if password == "12345":
    print(" ACCESS GRANTED ")   
else:
    print(" ACCESS DENIED ")