import MySQLdb
from model.bd.Alumno import Alumno

class Data:

    def conectar(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="123456",
            db="profe_pato_bot"
        )

    def desconectar(self):
        self.db.commit()
        self.db.close()

    def get_alumno(self, id):
        self.conectar()

        cur = self.db.cursor()
        cur.execute("SELECT * FROM alumno WHERE id = "+str(id))

        alumno = None

        for row in cur.fetchall():
            alumno = Alumno(row[0], row[1])

        self.desconectar()

        return alumno

    def crear_alumno(self, alumno):
        self.conectar()

        cur = self.db.cursor()
        insert = "INSERT INTO alumno VALUES('"+str(alumno.id)+"','"+str(alumno.nombre)+"', NOW())"
        cur.execute(insert)
        print(insert)

        self.desconectar()