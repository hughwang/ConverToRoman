This web application was written in a Python/Django web framework. 
The web application have a form to accept a base-10 integer between 1 and 3999, 
and upon submission to the backend, calculate and display that integer represented as Roman numerals.

How to get the source code?
    git clone  https://github.com/hughwang/ConverToRoman.git

How  to run the system?
    suppose the code was downloded to
    d:\CoverToRoman
    Python ( 2.7 above) , Django (1.6.1 above) was installed on the machine
    
    cd d:\ConverToRoman
    python manage.py runserver

    on web browser, open:
    http://127.0.0.1:8000/roman/
    then user can input integer and submit.

How to run Unit Tests for the system?
    python manage.py test

Features implemented in the system:
    .  Input data validation, Only integer between 1 to 3999 is allowed to input
    .  Django form used in the system
    .  use css file to make the web page looks better
    .  system tested on Windows 7
    .  use Django template for rendering web pages



Sample code reference:

http://pythoncentral.io/how-to-use-python-django-forms/

http://www.rapidtables.com/convert/number/how-number-to-roman-numerals.htm

https://github.com/hughwang/practical_django_projects_1.6

Introducing Automated Testing
https://docs.djangoproject.com/en/1.8/intro/tutorial05/

CSS reference
http://www.w3schools.com/cssref/default.asp