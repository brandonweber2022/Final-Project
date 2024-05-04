from bs4 import BeautifulSoup
import requests

class Webscraper:

    def __init__(self):

        self.url = None

        self.soup = None

    def get_url(self):

        self.url = input("Input a URL to webscrape here: ")

    def beautifulsouping_url(self):

        response = requests.get(self.url)

        self.soup = BeautifulSoup(response.text, "html.parser")

    def course_season(self):

        course_season_tag = self.soup.find('div', id="page-desc")

        return course_season_tag.text.strip() if course_season_tag else "N/A"
    
    def extract_courses(self):

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

        for course in courses:

            print("Course ID:", course["course_id"])

            print("Subject:", course["subject"])

            print("Credits:", course["credits"])

            print()

    def calculate_cost(self):

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
