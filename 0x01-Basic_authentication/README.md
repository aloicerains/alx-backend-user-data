## Basic_authentication
In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)

## Resources
* [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)  
* [Base64 in Python](https://docs.python.org/3.7/library/base64.html)  
* [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)  
* [Flask](https://palletsprojects.com/p/flask/)  
* [Base64-concept](https://en.wikipedia.org/wiki/Base64)  

## Learning objectives
* What does authentication means
* What is Base64
* How to encode a string in Base64
* What Basic authentication means
* How to send the Authorization header

## Tasks
0. Simple-basic-API: starting project from a simple archive.zip containing an API    
1. Error handler: unauthorized. This is used for new error handling using the endpoint in `api/v1/views/index.py`  
2. Error handler: Forbidden requests. 
3. Auth class: Creating a class to manage the API authentication  
4. Defining which routes don't need authentication   
5. Request validation: Validates all requests to secure the API
6. Conducting basic authentication. 
7. Basic authencation using `Base64 part`
8. Basic-Base64 decode   
9. Basic-User credentials   
10. Basic-user object  
11. Basic-overload current_user-and BOOM!
