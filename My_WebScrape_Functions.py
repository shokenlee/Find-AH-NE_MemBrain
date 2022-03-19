#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Setup
import numpy as np
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')


# Variables
url_up = 'https://www.uniprot.org/'

# Functions
def searchWord_at_UniprotHome(query_word):
    '''
    Search for a word in the home page of Uniprot
    and returns the browser
    
    ----
    Parameters
        query_word
    
    Returns
        browser
    '''
        
    # Initiate Uniprot Home
    browser = webdriver.Chrome(options=options)
    browser.get(url_up)
    
    # insert the query word
    elem_query = browser.find_element_by_id('query')
    elem_query.clear()
    elem_query.send_keys(query_word)
    
    # search
    elem_search_botton = browser.find_element_by_id('search-button')
    elem_search_botton.click()
   
    # return the opened browser
    return browser


def searchForUniprotID_getProtein_Organism_Name(uniprot_id):
    '''
    To search Uniprot home for an Uniprot ID and get the protein and organism name
    After search, the browser is shut down
    
    -----
    Parameters
        uniprot_id
    
    Returns
        organism_name, protein_name
    '''
    
    # search for the Uniprot ID
    browser = searchWord_at_UniprotHome(uniprot_id)
    
    # 
    
    ## Get the organism name
    elem_organism_name = browser.find_element_by_id('content-organism')
    organism_name = elem_organism_name.text
    
    ## Get the protein name
    elem_protein_name = browser.find_element_by_id('content-protein')
    protein_name = elem_protein_name.text
       
    # quit the browser
    browser.quit()
    
    # return a variable
    return organism_name, protein_name

def summmy(a, b):
    return a + b

def numpytest():
    return np.pi

