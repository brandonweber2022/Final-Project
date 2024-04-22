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
  
# Sup Sean, this is what I was thinking for the data_analysis file. lmk what you think

def extract_course_credits(course_data):
    """
    Extracts the number of credits for each course from the course data.

    Parameters:
    - tbd

    Returns:
    - credits_list (list): List of credit values for each course.
    """
  

def extract_course_season(course_data):
    """
    Extracts the season (e.g., Fall, Spring, Summer) for each course from the course data.

    Parameters:
    - tbd

    Returns:
    - season_list (list): List of seasons for each course.
    """

fall_semester = re.search(r"Fall (.+)", "hypothetical course list")
#repeat for summer and spring
season_list = []
retun season_list
#append semester to season list

def identify_gen_ed_courses(course_data):
    """
    Identifies if each course is a General Education (GenEd) course or not.

    Parameters:
    - tbd

    Returns:
    - gen_ed_list (list): List indicating whether each course is GenEd or not.
    """
  #same thing as semester but for gen eds instead

