from models import db, User

""" 
SELECT TO SQLALCHEMY

Sintaxis del SELECT

SELECT * FROM table_name;
SELECT field1, field2 FROM table_name;

SELECT * FROM table_name WHERE condition;
SELECT field1, field2 FROM table_name WHERE condition;


Ejemplo:


SELECT * FROM users;

"""

users = User.query.all() # SELECT * FROM users; [<User 1>, <User 2>, <User 3>, ...]
user = User.query.get(1) # SELECT * FROM users WHERE id = 1;
users = User.query.filter_by(active=True) # SELECT * FROM users WHERE active=true; [<User 1>, <User 2>]
user = User.query.filter_by(username="pperez", active=True).first() # SELECT * FROM users WHERE username='pperez' AND active=true; [<User 1>]


""" 
INSERT TO SQLALCHEMY

Sintaxis

INSERT INTO users (field1, field2) VALUES (value1, value2);

Ejemplo:

INSERT INTO users (username, password) VALUES ('lrodriguez', '123456');

"""
# Definimos los valores a guardar
user = User()
user.username = "lrodriguez"
user.password = "123456"

# Ejecutamos el insert y guardamos los cambios
db.session.add(user) # INSERT INTO users (username, password) VALUES ('lrodriguez', '123456');
db.session.commit()


""" 
UPDATE to SQLALCHEMY

Sintaxis:

UPDATE table_name SET field1=value1, field2=value2 WHERE condition;

Ejemplo:

UPDATE users SET password='Admin123' WHERE id = 1;

"""

# Buscamos primero el usuario

user = User.query.get(1)
user.password = 'Admin123'

# Guardar los cambios
db.session.commit()


""" 
DELETE to SQLALCHEMY

Sintaxis

DELETE FROM table_name WHERE condition;

Ejemplo:

DELETE FROM users WHERE id = 1;

"""

user = User.query.get(1)

# Ejecutamos el delete y guardamos los cambios
db.session.delete(user) # DELETE FROM users WHERE id = 1;
db.session.commit()