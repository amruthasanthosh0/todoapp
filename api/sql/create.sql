drop table if exists login; 
drop table if exists todolist;  



CREATE TABLE login (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  pass TEXT NOT NULL
  );
  
CREATE TABLE todolist (
  id SERIAL PRIMARY KEY, 
  task TEXT  NOT NULL,
  LASTdate timestamp NOT NULL,
  CONSTRAINT uid FOREIGN KEY(id) REFERENCES login(id) ON DELETE CASCADE
  );





