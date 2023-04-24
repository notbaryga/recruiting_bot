import sqlite3

class Base():
    def __init__(self, way):
        self.way = way
        self.connection = sqlite3.connect(self.way, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_user(self, id: int):
        self.cursor.execute(f'SELECT id FROM users WHERE id = (?)', (id, ))
        return self.cursor.fetchone()

    def add_user(self, id: int):
        self.cursor.execute(f'INSERT INTO users (id) VALUES (?)', (id,))
        self.connection.commit()

    def add_role(self, id: int, role: str):
        self.cursor.execute(f'UPDATE users SET role= (?) WHERE id= (?)', (role, id,))
        self.connection.commit()

    def get_role(self, id: int):
        self.cursor.execute(f'SELECT role FROM users WHERE id = (?)', (id,))
        return self.cursor.fetchone()

base = Base('models/database.db')
#print(base.get_user(789))