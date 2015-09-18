## Translating with babel

create pot file:

`pybabel extract -F babel.cfg -o messages.pot .`

add language and create po file:

`pybabel init -i messages.pot -d translations -l de`

translate file under `translations/de/LC_MESSAGES/messages.po`

compile:

`pybabel compile -d translations`

If strings change, create new pot file and merge changes:

`pybabel update -i messages.pot -d translations`


https://pythonhosted.org/Flask-Babel/
