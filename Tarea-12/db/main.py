import sqlite3

def main2():
    buscarAlumno(1)

def main():
    crearAlumno(2,"Patrick2","Luis")
    crearAlumno(3,"Patrick3","Luis")
    crearAlumno(4,"Patrick4","Luis")
    crearAlumno(5,"Patrick5","Luis")
    crearAlumno(6,"Patrick6","Luis")
    crearAlumno(7,"Patrick7","Luis")
    crearAlumno(8,"Patrick8","Luis")

def crearAlumno(id,nombre,apellido):
    conn = sqlite3.connect('Tarea-12/db/alumnos.db')
    cursor = conn.cursor()
    
    query = f"INSERT INTO alumnos(id,nombre,apellido) VALUES ({id},'{nombre}','{apellido}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def buscarAlumno(id):
    conn = sqlite3.connect('Tarea-12/db/alumnos.db')
    cursor = conn.cursor()
     
    query = f"SELECT * FROM alumnos WHERE id={id}"
    data = cursor.execute(query)
    print(data.fetchone())
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main2()