from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init app
app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))

#@app.route('/',methods=['GET'])
#def get():
#	return jsonify({'msg':'Hellow World'})
#Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#init db
db=SQLAlchemy(app)
db.create_all()

#init ma
ma=Marshmallow(app)

#user class mode 
class user(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.String(100),unique=True)
	username=db.Column(db.String(250))

	def __init__(self, userid, username):
		self.userid=userid
		self.username=username

# user schema
class userSchema(ma.Schema):
	class Meta:
		fields=('id','userid','username')

#Init Schema 
user_schema =userSchema()
users_schema=userSchema(many=True)

# create a user 
@app.route('/user',methods=['POST'])
def add_user():
	#id=request.json['id']
	userid=request.json['userid']
	username=request.json['username']
    
	new_user=user(userid, username)
	db.session.add(new_user)
	db.session.commit()
	print(new_user)
	print(new_user.id)
	print(new_user.userid)
	print(new_user.username)

	return user_schema.jsonify(new_user)

# get all users 
@app.route('/user',methods=['GET'])
def get_users():
	all_users=user.query.all()
	result=users_schema.dump(all_users)
	return jsonify(result)

# get single  user
@app.route('/user/<id>',methods=['GET'])
def single_user(id):
	single_user=user.query.get(id)
	return user_schema.jsonify(single_user)

	# update user 
@app.route('/user/<id>',methods=['PUT'])
def update_user(id):
	user1=user.query.get(id)
	userid=request.json['userid']
	username=request.json['username']

	user1.userid=userid
	user1.username=username
	
	db.session.commit()

	return user_schema.jsonify(user1)

# delete user  come back 
@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
	user1=user.query.get(id)
	db.session.delete(user1)
	db.session.commit()
	return user_schema.jsonify(user1)

## todos ######################################
 



#to do  class mode 
class todo(db.Model):
	todoid=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.String(100))
	todovalue=db.Column(db.String(250))

	def __init__(self, userid, todovalue):
		self.userid=userid
		self.todovalue=todovalue

# user schema
class todoSchema(ma.Schema):
	class Meta:
		fields=('todoid','userid','todovalue')

#Init Schema 
todo_schema =todoSchema()
todos_schema=todoSchema(many=True)

# create a todo 
@app.route('/todo',methods=['POST'])
def add_todo():
	#id=request.json['id']
	userid=request.json['userid']
	todovalue=request.json['todovalue']
    
	new_todo=todo(userid, todovalue)

	db.session.add(new_todo)
	db.session.commit()
	print(new_todo.todoid)
	print(new_todo.userid)
	print(new_todo.todovalue)
    
	return todo_schema.jsonify(new_todo)


# get all todo 
@app.route('/todo',methods=['GET'])
def get_todos():
	all_todo=todo.query.all()
	result=todos_schema.dump(all_todo)
	return jsonify(result)

# select single todos 
@app.route('/todo/<todoid>',methods=['GET'])
def single_todo(todoid):
	single_todo=todo.query.get(todoid)
	return todo_schema.jsonify(single_todo)

# update todo 
@app.route('/todo/<todoid>',methods=['PUT'])
def update_todo(todoid):
	user1=todo.query.get(todoid)
	userid=request.json['userid']
	todovalue=request.json['todovalue']

	user1.userid=userid
	user1.todovalue=todovalue
	
	db.session.commit()

	return todo_schema.jsonify(user1)

# delete todo 
@app.route('/todo/<todoid>',methods=['DELETE'])
def delete_todo(todoid):
	user1=todo.query.get(todoid)
	db.session.delete(user1)
	db.session.commit()
	return todo_schema.jsonify(user1)

#Run server 
if __name__=="__main__":
	app.run(host='0.0.0.0',debug=True)  # for docker 
	## app.run(debug=True)  stand alone 
