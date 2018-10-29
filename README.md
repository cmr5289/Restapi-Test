# Restapi-Test

Start environment by running the following command from top level directory

```
. ./env/bin/activate
```

From here run

```
Pip install -r  requirements.txt
```

This will initialize the virtual environment that I used for the project.

```
cd marvel_api
```

Inside of /marvel_api/restapi/management/commands/ is a file called dataimport.py.
This management command can be run like so in order to initialize a MongoDB
```
python manage.py dataimport {CSV file} {name of collection} [--showids](optional tag to show all the ids of the imported data)
```

I ran this command three times with each CSV file provided to make three different collections:
marvel_heroes , marvel_villans, and marvel_stats

I used Postman as a way to test my endpoints. There are two endpoints available, one that will access a collection
/restapi/api/v1/{collection_name}/

The other major endpoint is the accessing of individual data
/restapi/api/v1/{collection_name}/{id}/


EXAMPLES
http://localhost:8000/restapi/api/v1/marvel_heroes/1678/
http://localhost:8000/restapi/api/v1/marvel_heroes/

Using Postman I was able to test the basic functions of the API. These functions consist of GET, POST, PUT, DELETE to the above mentioned endpoints. JSON data must be formatted like so
```
{
"fields":
	[
	{"id": "1678", "name": "Spider-Man (Peter Parker)", "IDENTITY": "Secret Identity", "ALIGN": "Good Characters", "EYE": "Hazel Eyes", "HAIR": "Brown Hair", "SEX": "Male Characters", "ALIVE": "Living Characters", "FIRST APPEARANCE": "Aug-62", "Year": "1962"}
	]
}
```

Using the following CURL command we can test basic functionality:

```
curl --header "Content-Type: application/json" --request POST --data '{"fields":[{"id": "1678", "name": "Spider-Man (Peter Parker)", "IDENTITY": "Secret Identity", "ALIGN": "Good Characters", "EYE": "Hazel Eyes", "HAIR": "Brown Hair", "SEX": "Male Characters", "ALIVE": "Living Characters", "FIRST APPEARANCE": "Aug-62", "Year": "1962"}]}' http://localhost:8000/restapi/api/v1/marvel_heroes/
```

There is a file included in /marvel_api/csvtest.py that does some simple python requests tests to show off functionality as well.
