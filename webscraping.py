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

def parse_html(self, html_content):

    """ Takes html content as input and uses bueatifulsoup to extract class data"""
    soup = BeautifulSoup(html_content,'html.parser')
    classes_compiled = []
    for course_tag in soup.find_all("div", class_="course"):
        name = course_tag.find("span",class_="name").text
        description = course_tag.find("p", class_="description").text
        classes.append({"name": name, "description": description})
    return classes_compiled
                                
def extract_data():

    """a standalone function that extracts the data using regular expressiosns to indentify free courses"""
    pass

def permission():

    """A function that checks to see if we can get permission from the website to extract data"""
    pass

def error_handling():

    """ A funcion that handles errors"""
    pass
