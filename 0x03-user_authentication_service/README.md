## User authentication service
In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.    

### Resources
* [Requests module](https://requests.kennethreitz.org/en/master/user/quickstart/)  
* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)  
* [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)  
* [SQLAlchemy declare a mapping](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping)
* [More on sqlalchemy.create_engine](https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.create_engine) 
* [SQLAlchemy column description](https://docs.sqlalchemy.org/en/13/core/metadata.html#sqlalchemy.schema.Column) 

### Learning objectives
The following learning objectives will be met in this project
* How to declare API routes in a Flask app
* How to get and set cookies
* How to retrieve request form data
* How to return various HTTP status codes


