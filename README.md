## Requirements

* MysqlDB
* Django version and libraries required are in requirements.txt file
* Create  library db in mysql
* replace password and username for db in libmanagement/settings.py
* run command : python manage.py makemigrations
* run command python manage.py migrate

## Front end url:
    baseUrl="http://localhost:8000"


## Backend Api End points
 baseUrl='http://localhost:8000/api/v1/'
1. Register User:
    url=baseurl+'user/register/<type>'
    method="POST"
    type= 'student' or 'admin'
    body={
        'name':String,
        'email':Email,
        'password':String
    }
    
    

2. Login User
    url=baseurl+'user/login'
    method="POST"
    
    body={
        'email':Email,
        'password':String
    }

3. Get Book List

    url=baseurl+'book/all'
    method="GET"
    header={
        'Authorization':'JWT '+{token}
    }
   
4. Create Book

    url=baseurl+'book'
    method="POST"
    header={
        'Authorization':'JWT '+{token}
    }
     
    body={
        'name':String,
        'author_name':String,
        'price':Float
    }

5. Update Book

    url=baseurl+'book'
    method="PATCH"
    header={
        'Authorization':'JWT '+{token}
    }
    
    body={
        'id':int,
        'name':String,
        'author_name':String,
        'price':Float
    }<br/>
    Note :id field is compulsory.For rest of fields No need to pass all the fields only the fields required to update
     
6.Delete Book

    url=baseurl+'book/<id>'
    method="DELETE"
    header={
        'Authorization':'JWT '+{token}
    }
    
    
 
    