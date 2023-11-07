from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    
    profile = db.relationship("Profile", backref="user", uselist=False) # [<Profile 1>] => <Profile 1>
    
    posts = db.relationship("Post", backref="user")
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active, 
            "name": self.profile.name,
            "lastname": self.profile.lastname,
            "posts": len(self.posts)
        }
        
    def datos_con_publicaciones(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active, 
            "name": self.profile.name,
            "lastname": self.profile.lastname,
            "posts": list(map(lambda post: post.serialize(), self.posts))
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), default="")    
    lastname = db.Column(db.String(120), default="") 
    twitter = db.Column(db.String(120), default="")    
    instagram = db.Column(db.String(120), default="")    
    facebook = db.Column(db.String(120), default="")    
    github = db.Column(db.String(120), default="")
    
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "users_id": self.users_id,
            "user": self.user.username
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
       
        
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "users_id": self.users_id
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    
    
    
    
    
    
    