import mysql.connector

bd = mysql.connector.connect(
    user='Edgar',password='12345',
    database='mascotas')

cursor = bd.cursor()

while True:
    print('1) Agregar dueño')
    print('2) Mostrar dueños')
    print('0) Salir')
    op=input()

    if op == '1':
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        domicilio = input('domicilio: ')
        telefono = input('telefono: ')
        email = input('email: ')
        foto = input('foto: ')

        consulta = "INSERT INTO dueno (nombre,apellido,domicilio,telefono,email,foto)"\
            "VALUES (%s,%s,%s,%s,%s,%s)"
        
        cursor.execute(consulta, (nombre,apellido,domicilio,telefono,email,foto))
        bd.commit()
        if cursor.rowcount:
            print('Se agrego dueño')
        else:
            print('Error')
    elif op == '2':
        consulta = "SELECT * FROM dueno"
        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('ID: ',row[0])
            print('Nombre: ',row[1])
            print('Apellido: ',row[2])
            print('Domicilio: ',row[3])
            print('Telefono: ',row[4])
            print('Email: ',row[5])
            print('Foto: ',row[6])
    elif op == '0':
        break