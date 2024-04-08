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
  
