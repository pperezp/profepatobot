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
        self.cur = self.db.cursor()

    def desconectar(self):
        self.db.commit()
        self.db.close()

    def get_alumno(self, id):
        self.conectar()

        self.cur.execute("SELECT * FROM alumno WHERE id = "+str(id))

        alumno = None

        for row in self.cur.fetchall():
            alumno = Alumno(row[0], row[1])

        self.desconectar()

        return alumno

    def crear_alumno(self, alumno):
        self.conectar()

        insert = "INSERT INTO alumno VALUES('"+str(alumno.id)+"','"+str(alumno.nombre)+"', NOW())"
        self.cur.execute(insert)
        print(insert)

        self.desconectar()

    def reg_mensaje(self, mensaje):
        self.conectar()

        insert = "INSERT INTO mensaje VALUES(NULL, '"+str(mensaje.id_alumno)+"', '"+str(mensaje.mensaje)+"', NOW())";
        self.cur.execute(insert)

        self.desconectar()

    def get_links(self, tag):
        self.conectar()

        select = "SELECT l.id AS 'ID link', l.valor AS 'Link',t.id AS 'ID tag', t.valor AS 'Tag' FROM link_tag lt INNER JOIN link l ON l.id = lt.link INNER JOIN tag t ON t.id = lt.tag WHERE t.valor LIKE '%"+tag+"%' GROUP BY l.id;"

        self.cur.execute(select)

        links = list()

        for row in self.cur.fetchall():
            links.append(row[1])

        self.desconectar()

        return links


    def get_tags(self):
        self.conectar()

        select = "SELECT * FROM tag"
        self.cur.execute(select)

        tags = list()
        for row in self.cur.fetchall():
            tags.append(row[1])

        self.desconectar()

        return tags