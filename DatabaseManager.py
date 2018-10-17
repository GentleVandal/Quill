from sqlite3 import *

class DatabaseManager:

    def __init__(self):
        self.connect2Database = None
        self.db_cursor = None
        setupDatabase()
        

    def setupDatabase(self):
        self.connect2Database = connect("dquill.db")
        self.db_cursor = self.connect2Database.cursor() 


    def save_changes():
        ''' 
        All changes will be committed to database
        '''
        self.connect2Database.commit()
    
    
    def add(self,name,_type):
        pass
    
    def delete(self,name,_type):
        pass
        
    def query(self,name):
        db_cursor.execute("""SELECT * FROM dquill WHERE name=?""", (name,))
        result = db_cursor.fetchall()
        
