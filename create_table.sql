CREATE TABLE IF NOT EXISTS User_store (
   id serial PRIMARY KEY ,
   firstname VARCHAR(100) NOT NULL,
   lastname VARCHAR(100) NOT NULL,
   age INTEGER NOT NULL,
   email VARCHAR(100) UNIQUE NOT NULL,
   job VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Application (
   id serial PRIMARY KEY,
   appname VARCHAR(100) NOT NULL,
   username VARCHAR(100) UNIQUE NOT NULL,
   lastconnection DATE,
   userid serial NOT NULL,
    CONSTRAINT fk_user
      FOREIGN KEY(userid)
	  REFERENCES User_store(id)
);
