# recipe.md

recipe.md is a webapp to convert recipes from different websites to Markdwown. Written in in python
using the micro framework [Flask](http://flask.pocoo.org/).

It's configured to run on [Openshift](https://www.openshift.com/).

## Try it

You can find it at [http://recipemd-dnlvgl.rhcloud.com/](http://recipemd-dnlvgl.rhcloud.com/)

Because it is running on the free plan the application idles after 24 hours. If you get a Server Error just load the page again.

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
