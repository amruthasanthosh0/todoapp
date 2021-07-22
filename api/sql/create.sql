drop table if exists login cascade ; 
drop table if exists todolist cascade ;  



CREATE TABLE login (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  pass TEXT NOT NULL
  );
  
CREATE TABLE todolist (
  id SERIAL PRIMARY KEY,
  uid INTEGER ,
  task TEXT  NOT NULL,
  lastdate timestamp NOT NULL,
  status boolean,
  CONSTRAINT uid FOREIGN KEY(uid) REFERENCES login(id) ON DELETE CASCADE
  );




