from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import *

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

# # Create
connection.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
connection.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

#connection de create table
create_table = open("create_table.sql")
escaped_sql = sqlalchemy.text(create_table.read())
connection.execute(escaped_sql)
