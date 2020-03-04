import sqlite3
class Bd:
    def __init__(self):
        self.connect = sqlite3.connect("bd\\players.db", check_same_thread = False) 

    def _select(self, table_name, table_pole, table_if, values):
        cursor = self.connect.cursor()
        cursor.execute("SELECT {1} FROM {0} WHERE {2}".format(table_name, table_pole, table_if), values)
        return cursor

    # дергаёт одну запись!
    def select(self,  table_name, table_pole, table_if, values):
        return self._select(table_name, table_pole, table_if, values).fetchone()

    def insert(self, table_name, table_pole, table_if, values):
        cursor = self.connect.cursor()
        #print("INSERT INTO {0}{1} VALUES {2}".format(table_name, table_pole, table_if))
        cursor.execute("INSERT INTO {0}{1} VALUES {2}".format(table_name, table_pole, table_if), values)
        return cursor.lastrowid
        
    def update(self, table_name, table_pole, table_if, values):
        cursor = self.connect.cursor()
        #print("UPDATE {0} SET {1} WHERE {2}".format(table_name, table_pole, table_if))
        cursor.execute("UPDATE {0} SET {1} WHERE {2}".format(table_name, table_pole, table_if), values)
    
    def del_str(self, table_name, table_if, values):
        cursor = self.connect.cursor()
        cursor.execute(f'DELETE FROM {table_name} WHERE {table_if}', values)
        
    def commit(self):
        self.connect.commit()
    


        