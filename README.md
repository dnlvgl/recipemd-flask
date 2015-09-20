# recipe.md

recipe.md is a webapp to convert recipes from different websites to Markdwown. Written in in python
using the micro framework [Flask](http://flask.pocoo.org/).

It's configured to run on [Openshift](https://www.openshift.com/).


## Installation

Local / hosted Installation:

* Create a virtualenv
* Install the dependencies
    * `pip install -r requirements.txt`
* Run the web app
    * `python recipemd.py`

OpenShift Installation:

* Create a python cartridge on [Openshift](https://developers.openshift.com/en/python-overview.html)
* Entry Point is configured in `wsgi.py`
* Deploy to OpenShift


## License

BSD License
