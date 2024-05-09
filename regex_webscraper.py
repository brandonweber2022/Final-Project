from bs4 import BeautifulSoup

import requests

import re

#https://catalog.upenn.edu/courses/anat/

class other_website:

    def __init__(self):

        self.url = None

        self.soup = None

    def get_url(self):

        self.url = input("Input a URL to webscrape here: ")

    def beautifulsouping_url(self):

        response = requests.get(self.url)

        self.soup = BeautifulSoup(response.text, "html.parser")

    def course_season(self):

        course_season_tag = re.search(r'Fall', self.soup.text)

        course_season_tag = course_season_tag.group() if course_season_tag else "N/A"

        return course_season_tag

    def extract_courses(self):
        course_tags = re.findall(r'(\d+(\.\d+)?) Course Unit.*?([A-Z]+\s\d{4})\s(.+?)\.', self.soup.text, re.DOTALL)

        courses = []

        for tag in course_tags:

            credits_value = tag[0].strip()

            course_id = tag[1].strip()

            course_subject = tag[2].strip()

            course = {

                "course_id": course_id,

                "subject": course_subject,

                "credits": credits_value
            }
            courses.append(course)

        return courses


    def print_course(self, courses):

        for course in courses:

            print("Course ID:", course["subject"])

            print("Subject:", course["subject"])

            print("Credits:", course["credits"])

            print()

    def calculate_cost(self):

        course_id = input("What course are you interested in? Enter a course ID: ")

        for course in self.extract_courses():

            if course["course_id"] == course_id:

                credits = float(course["credits"])

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

    scraper = other_website()

    scraper.scrape()

