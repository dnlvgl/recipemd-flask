#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import scraper
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():

    url = request.form['url']
    recipe = scraper.getData(url)
    # if recipe is a tuple we got all information
    if isinstance(recipe, tuple):
        return render_template('index.html', recipeTitle=recipe[0], recipeIngreds=recipe[1], recipeInstruct=recipe[2])
    # if it's not a tuple showreturned error
    else:
        return render_template('index.html', Error=recipe)

if __name__ == '__main__':
    app.run(debug=True)
