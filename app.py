import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from dotenv import load_dotenv # funcion que me permite cargar las variables de entorno del archivo .env
from models import db, User

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
# configuracion de opciones para la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASEURI')

# vincular el models con app
db.init_app(app)

# gestionar los comandos de base de datos
Migrate(app, db) # db init, db migrate, db upgrade 


@app.route('/')
def main():
    return jsonify({ "status": "Server Up"}), 200


@app.route('/register', methods=['POST'])
def register():
    
    username = request.json.get("username")
    password = request.json.get("password")
    
    if not username:
        return jsonify({ "msg": "Username is required!"}), 400
    
    if not password:
        return jsonify({ "msg": "Password is required!"}), 400
    
    user = User()
    user.username = username
    user.password = password
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({ "msg": "Data completed"}), 200


@app.route('/users', methods=['GET', 'POST'])
def get_or_create_user():
    
    if request.method == 'GET':
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))
        return jsonify(users), 200
        
    if request.method == 'POST':
        username = request.json.get("username")
        password = request.json.get("password")
        
        if not username:
            return jsonify({ "msg": "Username is required!"}), 400
        
        if not password:
            return jsonify({ "msg": "Password is required!"}), 400
        
        user = User()
        user.username = username
        user.password = password
        
        #db.session.add(user)
        #db.session.commit()
        
        user.save()
        
        return jsonify(user.serialize()), 201
    

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_update_or_delete_user(id):
    user = User.query.get(id)
    
    if not user:
        return jsonify({ "result": "User not found!"}), 404
    
    if request.method == 'GET':
        return jsonify(user.serialize()), 200
    
    if request.method == 'PUT':
        
        password = request.json.get("password")
        
        if not password:
            return jsonify({ "msg": "Password is required!"}), 400
        
        user.password = password
        db.session.commit()
        
        return jsonify(user.serialize()), 200
    
    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({ "result": "User deleted!"}), 200

""" @app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    
    password = request.json.get("password")
        
    if not password:
        return jsonify({ "msg": "Password is required!"}), 400
    
    user = User.query.get(id)
    user.password = password
    
    db.session.commit()
    
    print(user)
    
    return jsonify(user.serialize()), 200 """




if __name__ == '__main__':
    app.run()