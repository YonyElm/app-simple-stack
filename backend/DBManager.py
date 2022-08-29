import mysql.connector
import sys


class DBManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user, 
                password=self.password,
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.connection.cursor()
        except:
            print('Connection to DB failed', file=sys.stderr)
    
    ## Resting the DB
    def populate_db(self):
        if (self.cursor):
            self.cursor.execute('DROP TABLE IF EXISTS items')
            self.cursor.execute('CREATE TABLE items (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256))')
            self.cursor.execute("insert into items values(NULL, 'item0')")
            self.connection.commit()

    ## Insert to the DB a new record
    def insert_records(self, id, name):
        if (self.connection):
            data = (id, str(name))
            query = (
                    "INSERT INTO items(id, name)"
                    "VALUES (%s, %s)"
                    )
            try:
                self.cursor.execute(query, data) # Causing exception when id already exists in DB
                self.connection.commit()
            # TBD: Requires better handling of `id` duplication
            except:
                print('Write to DB failed, maybe key exists already', file=sys.stderr)
    
    ## Read all items names from DB
    def query_item_names(self):
        rec = []
        if (self.cursor):
            self.cursor.execute('SELECT name FROM items')
            for c in self.cursor:
                rec.append(c[0])
        return rec
            
    ## Return boolean
    def is_connected(self):
        return self.connection and self.connection.is_connected()