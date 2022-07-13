from builtins import dict, len, zip
import sqlite3


class ProductsDatabase:
   

  # def  __init__(self):

  #   self.execute_hash_query('CREATE TABLE IF NOT EXISTS "Birds" ( "Name"	TEXT NOT NULL, "User"	TEXT NOT NULL, "Bio"	TEXT NOT NULL, "Age"	INTEGER NOT NULL, "PasswordHash"	INTEGER NOT NULL, "BirdId"	INTEGER NOT NULL, PRIMARY KEY("BirdId" AUTOINCREMENT));')  
  #   self.execute_hash_query( 'CREATE TABLE IF NOT EXISTS  "Comment" ( "User" TEXT NOT NULL, "PostId"	INTEGER NOT NULL, "Comments"	TEXT NOT NULL,     PRIMARY KEY("PostId" AUTOINCREMENT));') 
  #   self.execute_hash_query('CREATE TABLE IF NOT EXISTS "Counts" ( "PostId"	INTEGER NOT NULL, "Likescount"	TEXT NOT NULL, "User"	TEXT NOT NULL,      PRIMARY KEY("PostId" AUTOINCREMENT));') 
  #   self.execute_hash_query('CREATE TABLE IF NOT EXISTS "Likes" ( "User"	TEXT NOT NULL, "PostId"	INTEGER NOT NULL );') 
    
    
  def create_user(self,User,Email,Password):
    self.execute_hash_query("""INSERT INTO Users (User,Email,Password) VALUES (?, ?, ?)""",User,Email,Password)
 
 # conn.commit() 


  def get_id_by_user(self, user):
    return self.execute_query("SELECT * FROM Users WHERE User=?",user)
    


  def execute_hash_query(self, query_text, *parameters):
      conn = sqlite3.connect('Products.db')
      cur = conn.cursor()
      cur.execute(query_text, parameters)
      conn.commit()


  def execute_query(self, query_text, *parameters):
      conn = sqlite3.connect('Products.db')
      cur = conn.cursor()
      cur.execute(query_text, parameters)

      column_names = []
      for column in cur.description:
       column_names.append(column[0])

      rows = cur.fetchall()
      dicts = []
      for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)
        conn.close()
      return dicts

  

 
 

         