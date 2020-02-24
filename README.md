# todo_microservice_crud
Simple todo-list microservice app, which has:
1) Service to add/delete/query users
2) Service to create/edit/delete/query TODO lists for users

Crud  rest api operations using flask ,sqlAlchemy ,Flask-Marshmallow , Postman Client 

With docker run:
Files in project folder 

 1.app.py													
 2. requirements.txt 	
 3. Dockerfile 	
 4.db.sqlite 	

Docker build :
 docker build . -t todo_crud:newv1
Docker run :
 docker run -p 5000:5000 740d9dbe4474

use postman client to send requests:
 set contenttype = application/josn in header.
 
 1.Add users:POST methos
 http://127.0.0.1:5000/user
 raw message
    {
	"userid": "Test3",
	"username": "Test user 3"
	}
 2.Read all users  :GET method
  http://127.0.0.1:5000/user

 3.Update User: GET method
  http://127.0.0.1:5000/user/1
  raw message
    {
	"userid": "user1",
	"username": "test1 test1"
	}
 4.Delete User: PUT method
 http://127.0.0.1:5000/user/1

Repeat similar postman steps for todo as well 
 Endpoint: http://127.0.0.1:5000/todo
  For todo post example :
         {
	"userid": "test1",
	"todovalue": "Go for Run  "
	  }

Without docker run 

1.Set environment:
  Python3 –version
  pip3 install pipenv
  pipenv shell
  pipenv install flask flask-sqlalchemy flask-marshmallow 
  marshmallow-sqlalchemy

2.create db :python shell 
  from app import db
  db.create_all()

3.Run the app :
 Python3 app.py 

4.Repeat above postman steps for app microservice 

