import getpass
import sqlite3

def main2():
    crearUsuario(4,"Rossi","1234")

def main():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("contraseña: ")

    if verifica_credenciales(username,password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect('Clase-11/db/miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}' "
    rows = cursor.execute(query)
    
    data = rows.fetchone()

    

    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        return True

def crearUsuario(identificador,usuario,clave):
    conn = sqlite3.connect('Clase-11/db/miaplicacion.db')
    cursor = conn.cursor()

    query = f"INSERT INTO users(id,username,password) VALUES({identificador},'{usuario}','{clave}')"
    rows = cursor.execute(query)
    
    #data = rows.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    

if __name__ == '__main__':
    main2()

