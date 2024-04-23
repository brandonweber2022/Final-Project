import requests 
from bs4 import BeautifulSoup
class Webscraper:
    """ A Class that uses uninversal regualr expression to seperate free course from unpaid courses
    
    Will include methods such as: 
    
    fetch_html: fetches the html content from a URL
    parse_html: parses the html using BeautifulSoup
    extract_data: extracts the specified data from the pasrse function
    save_data: saves the data we extracted to a file
    
    """
    pass

def get_html (self, url):

    "A function that sends a request to recieve a specified URL and returns the HTML webpages
    parameters: 
        url: url of the desired website
    "
    try: 
        response = requests.get(url)
        response.raise_for_status() #error handling condtion
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error occured: {e}"

def parse_html():

    """ Takes html content as input and uses bueatifulsoup to parse it"""
    pass

def extract_data():

    """a standalone function that extracts the data using regular expressiosns to indentify free courses"""
    pass

def permission():

    """A function that checks to see if we can get permission from the website to extract data"""
    pass

def error_handling():

    """ A funcion that handles errors"""
    pass
