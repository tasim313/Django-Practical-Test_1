# HealthOS-Django-Practical-Test


First of all install Docker in your local machine. 
Open your terminal 
windows : docker-compose up --build
linux : sudo docker-compose up --build
open another terminal 
windows:  docker-compose run web python manage.py  makemigrations
linux : sudo  docker-compose run web python manage.py  makemigrations
windows :  docker-compose run web python manage.py migrate
linux: sudo  docker-compose run web python manage.py migrate
create superuser for admin 
windows: docker-compose run web python manage.py  createsuperuser
linux: sudo  docker-compose run web python manage.py createsuperuser

all requirement will be automatically install when command docker-compose up --build


Here Login, registration and email verification and reset password api use third party api package. I use djoser for user authentication

when run this project go this url : http://127.0.0.1:8000/docs/
all api can see in swagger. User must be register otherwise can not see  api
