# hapi-tabletop

## Getting started

To run create a virtual env and run:
```
pip install -r
```

Migrate database
```
python3 manage.py migrate
```

Create super user to access admin interface
```
python3 manage.py createsuperuser
```

Launch local server
```
python3 manage.py runserver
```

Visit [/update](http://127.0.0.1:8000/update/) and click the link to load the indicators into the database

## Example API Calls

Query inidicator
http://127.0.0.1:8000/api/indicators/population

Query by country
http://127.0.0.1:8000/api/indicators/population?iso3=AFG

Change format
http://127.0.0.1:8000/api/indicators/population?iso3=AFG&format=csv

Change table to wide shape
http://127.0.0.1:8000/api/indicators/population?iso3=AFG&format=csv&shape=wide

## Useful files

### Indicator configuration files
[/definition_files](definition_files)

### Transformation Scripts
[/scripts](/scripts)
