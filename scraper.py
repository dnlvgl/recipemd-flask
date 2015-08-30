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
        checkRecipe = soup.find('div', attrs={'id': 'zoneRecipe'}).text
    except Exception:
        return('Error: No recipe found, check URL')
    # title
    title = soup.find('h1', attrs={'id': 'itemTitle'}).text
    # ingredients
    ingreds = soup.find('div', attrs={'class': 'ingred-left'})
    ingreds = [s.getText().strip() for s in ingreds.findAll('li')]
    ingreds = ['- ' + s.replace('\n', ' ') for s in ingreds]  # add dash + remove newlines
    ingreds = [" ".join(s.split()) for s in ingreds]  # remove whitespace
    # instructions
    instruct = soup.find('div', attrs={'class': 'directLeft'})
    instruct = [s.getText().strip() for s in instruct.findAll('li')]
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
    else:
        return 'Error:  Website not supported'
