from bs4 import BeautifulSoup
import requests

class Webscraper:
    
    """ A class establishing the url and the soup method we'll be using"""
    
    def __init__(self):
        
    """ Initlizaies the names url and soup
    
    Args:
        self, a parameter that indivudally intalizaites an object 
        
    """
    
        self.url = None

        self.soup = None

    def get_url(self):
        
    """ Requests the url for the URL to be webscraped
    
    Args:
        self, a parameter that indivudally intalizaites an object   
    """

        self.url = input("Input a URL to webscrape here: ")

    def beautifulsouping_url(self):
        
    """ A function that uses beautiful soup to extract the URLs data
    
    Args:
        self, a parameter that indivudally intalizaites an object
    """

        response = requests.get(self.url)

        self.soup = BeautifulSoup(response.text, "html.parser")

    def course_season(self):
        
    """ A function that finds the season of the courses displayed 

    Args:
        self, a parameter that indivudally intalizaites an object

    Returns:
        Returns the courses season if it's found
    """

        course_season_tag = self.soup.find('div', id="page-desc")

        return course_season_tag.text.strip() if course_season_tag else "N/A"
    
    def extract_courses(self):
        
    """ A function that extracts the information of the courses, such as Course ID, Credits, and Subject

    Args:
        self, a parameter that indivudally intalizaites an object

    Returns:
        A dictionary of courses
    """

        course_tags = self.soup.find_all('div', class_="course")

        courses = []

        for tags in course_tags:

            course_id_tag = tags.find('div', class_="course-id")

            course_id = course_id_tag.text.strip() if course_id_tag else "N/A"

            course_subject_tag = tags.find('span', class_="course-title")

            course_subject = course_subject_tag.text.strip() if course_subject_tag else "N/A"

            credits_label_tag = tags.find('span', class_="course-info-label")

            credits_value_tag = tags.find('span', class_="course-min-credits")

            credits_label = credits_label_tag.text.strip() if credits_label_tag else "N/A"

            credits_value = credits_value_tag.text.strip() if credits_value_tag else "N/A"

            course = {
                "course_id": course_id,

                "subject": course_subject,

                "credits": credits_value
            }
            courses.append(course)

        return courses
    
        
    def print_course(self, courses):
        
    """ A function that prints out the information of the courses for the user to see

    Args:
        self: a parameter that indivudally intalizaites an object
        
        courses: the courses extarcted from the extract_courses method

    Side Effects:
        print(): Prints out courses
    """

        for course in courses:

            print("Course ID:", course["course_id"])

            print("Subject:", course["subject"])

            print("Credits:", course["credits"])

            print()

    def calculate_cost(self):
        
    """ A function that calculates the cost of a course chosen by the user
    Args:
        self: a parameter that indivudally intalizaites an object

    Side Effects:
        print(): Prints out a prompt asking the expected cost of tution. If cost is 0, a print of "This Course is FREE!" is printed, if not, the cost is printed

    Returns:
        Returns a tuple of the course_id and cost
        
        Returns nothing if nothing was found
    
    """
        
        course_id = input("What course are you interested in? Enter a course ID: ")

        for course in self.extract_courses():

            if course["course_id"] == course_id:

                credits = int(course["credits"])

                tuition_rate = float(input("What's the tuition rate for this semester? "))

                cost = credits * tuition_rate

                print(f"Expected cost for course {course_id}: ${cost}")

                if cost == 0:
                    
                    print("This course is FREE!")

                return course_id, cost
            
        print("Course not found.")

        return None, None

    def scrape(self):
        
    """A function that calls the meothods to be executed
    
    Args:
        self: a parameter that indivudally intalizaites an object
    
    """

        self.get_url()

        self.beautifulsouping_url()

        course_season = self.course_season()

        print(course_season)

        courses = self.extract_courses()

        self.print_course(courses)

        self.calculate_cost()

if __name__ == "__main__":

    scraper = Webscraper()

    scraper.scrape()
