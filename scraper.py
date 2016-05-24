#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import codecs
import sys


def chefkoch(soup):
    try:
        checkRecipe = soup.find('div', attrs={'id': 'recipe-incredients'}).text
    except Exception:
        return('Error: No recipe found, check URL')
    # title
    title = soup.find('h1', attrs={'class': 'page-title'}).text
    # ingredients
    ingreds = []
    table = soup.find('table', attrs={'class': 'incredients'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [s.text.strip() for s in cols]
        ingreds.append([ele for ele in cols if ele])  # get rid of empty values
    ingreds = ['- ' + ' '.join(s) for s in ingreds]
    # instructions
    instruct = soup.find('div', attrs={'id': 'rezept-zubereitung'}).text  # only get text
    instruct = instruct.strip()  # remove leadin and ending whitespace
    instruct = instruct.splitlines() # split into list to remove newlines
    # return tuple
    recipeData = (title, ingreds, instruct)
    return recipeData


def allrecipes(soup):
    try:
        checkRecipe = soup.find('ul', attrs={'class': 'list-ingredients-1'}).text
    except Exception:
        return('Error: No recipe found, check URL')
    # title
    title = soup.find('h1', attrs={'class': 'recipe-summary__h1'}).text
    # ingredients
    def find_ingreds(ingred):
        # TODO sane variable names
        ingreds = soup.find('ul', attrs={'class': 'checklist'})
        ingreds = [s.getText().strip() for s in ingreds.findAll(True, {"class": "recipe-ingred_txt"})]
        ingreds = ['- ' + s.replace('\n', ' ') for s in ingreds]  # add dash + remove newlines
        ingreds = [" ".join(s.split()) for s in ingreds]  # remove whitespace
        ingreds = ingreds[:-1] # delete "Add all ingredients to list"
        return ingreds
    ingreds = find_ingreds('list-ingredients-1') + find_ingreds('list-ingredients-2')
    # instructions
    instruct = soup.find('ol', attrs={'class': 'recipe-directions__list'})
    instruct = [s.getText().strip() for s in instruct.findAll('li')]
    # return tuple
    recipeData = (title, ingreds, instruct)
    return recipeData

def foodnetwork(soup):
    try:
        checkRecipe = soup.find('div', attrs={'itemprop': 'recipeInstructions'}).text
    except Exception:
        return('Error: No recipe found, check URL')
    # title
    title = soup.find('h1', attrs={'itemprop': 'name'}).text
    # ingredients
    ingreds = soup.find('div', attrs={'class': 'ingredients'})
    ingreds = ['- ' + s.getText().strip() for s in ingreds.findAll('li')]
    # instructions
    instruct = soup.find('div', attrs={'itemprop': 'recipeInstructions'})
    instruct = [s.getText().strip() for s in instruct.findAll('p')]
    # return tuple
    recipeData = (title, ingreds, instruct)
    return recipeData


def getData(url):
    try:
        page = requests.get(url)
    except Exception:
        return('Error: Enter a valid URL')
    soup = BeautifulSoup(page.text, "html5lib")

    if url.startswith('http://www.chefkoch.de/'):
        return chefkoch(soup)
    elif url.startswith('http://allrecipes.com/'):
        return allrecipes(soup)
    elif url.startswith('http://www.foodnetwork.com/recipes/'):
        return foodnetwork(soup)
    else:
        return 'Error:  Website not supported'
