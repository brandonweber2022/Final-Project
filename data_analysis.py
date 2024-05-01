#data analysis file 
def filter_clases_by_subject(class_list, subject):
  """
Filters a list of class dictionaries to find those with a specified subject
Parameters:
  class_list (list of dict): List of cleases, each as a dictionary containing detials reguarding the class
  subjects (str): Selected subject to filter classes by

  Returns: 
  A filtered list of classes that include the specified subject

  """
  filtered_classes = [cl for cl in class_list if subject.lower() in cl['description'}.lower()]
  return filtered_classes
  


def extract_course_credits(course_data):
    """
    Extracts the number of credits for each course from the course data.

    Parameters:
    - tbd

    Returns:
    - credits_list (list): List of credit values for each course.
    """
    list_credits = [ course["credits"] for course in course_data]
    return list_credits
  #create opportunity extract non int course creidt like a certificiation

def extract_course_season(course_data):
    """
    Extracts the season (e.g., Fall, Spring, Summer) for each course from the course data.

    Parameters:
    - tbd

    Returns:
    - season_list (list): List of seasons for each course.
    """
   
fall_semester_classes = re.search(r"Fall (.+)", class_list)
spring_semester_classes = re.search(r"Spring (.+)", class_list)
summer_semester_classes = re.search(r"Summer (.+)", class_list)
season_list = []

#possibly add function to extract course delivery method, online, asyc, in person

def identify_gen_ed_courses(course_data):
    """
    Identifies if each course is a General Education (GenEd) course or not.

    Parameters:
    - tbd

    Returns:
    - gen_ed_list (list): List indicating whether each course is GenEd or not.
    """
  #same thing as semester but for gen eds instead
gen_ed_course = ["GenEd" in course["tags"] for course in course_data]
return gen_ed_course
