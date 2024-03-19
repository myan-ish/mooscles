# Mooscles

Mmmm my mooscles are getting bigger and bigger.

[![Alternate Text](http://img.youtube.com/vi/S6UqgjaBt4w/0.jpg)](http://www.youtube.com/watch?v=S6UqgjaBt4w "Link Title")


# Run the project

# Setps to build the project

1. Make sure you have docker installed
2. Run `docker-compose -f docker-compose.prod.yml up -d --build`

After that it should be accessible in localhost:8000, port

# First time command

1. Run `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput` to make inital migration
2. Run `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear` for collecting static files

# Other commands

- To spin down docker `docker-compose down -v`
- Create super user `docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser`
- Build after update `docker-compose up -d --build`


