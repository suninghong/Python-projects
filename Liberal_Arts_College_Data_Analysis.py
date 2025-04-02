import requests
from bs4 import BeautifulSoup
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
from selenium import webdriver

def get_colgate_subjects(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_buttons = soup.select("button") #Because on colgate's website each area of study is a button
   
    subjects = {' '.join(button.text.strip().split()) for button in all_buttons if button.text.strip()} #strip is an efficient method in getting of /n from the list
    # strip gets of spaces and /n which would otherwise appear in the list
    return subjects

def num_colgate_houses(url_c_housing):
    response = requests.get(url_c_housing)
    soup = BeautifulSoup(response.text, "html.parser")
    all_buttons = soup.select("button")
   
    total = 0
    for i in all_buttons[1:]: #This is because "In this section" is a button
        total += 1
    return total

def get_williams_subjects(url):
    driver = webdriver.Chrome()  # Ensure ChromeDriver is correctly set up
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
   
    table = soup.find('table', id='areas-of-study')
    if not table:
        print("Table not found for Williams College")
        return set()

    rows = table.find('tbody').find_all('tr')[1:]  # Skip the header row. We want to find tr because tr indicates the line and 'tbody' is the tag that surrounds the entire table of area of study values
    subjects = {row.find('td').text.strip() for row in rows if row.find('td')} #Here we are looping through each row of the table of area of study values
    #and so we don't use findall to find 'td' because each row contains one 'td' tag.
    return subjects

def num_williams_houses(url_w_housing):
    response = requests.get(url_w_housing)
    soup = BeautifulSoup(response.text, "html.parser")
    all_buttons = soup.find_all("button")

    total = 0
    for i in all_buttons: #This is because "In this section" is a button
        total += 1
    return total

def get_hamilton_subjects(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    majors = soup.find_all("a", class_="study_link")
    #a is the hyperlink tag
    subjects = {' '.join(major.text.strip().split()) for major in majors if major.text.strip()} #we use if just incase we have to skip over empty tags
    return subjects

def num_hamilton_houses(url_h_housing):
    response = requests.get(url_h_housing)
    soup = BeautifulSoup(response.text, "html.parser")
    all_buttons = soup.find_all("span", class_="digest_item_title_link_label")
   
    total = 0
    for i in all_buttons:
        total += 1
    return total

def create_histogram(num_c, num_w, num_h):
    num = [num_c, num_w ,num_h]
    print(num)
    college = ["Colgate", "Williams", "Hamilton"]
    plt.bar(college, num)
    plt.xticks(college)
    plt.yticks(num)
    plt.xlabel("College")
    plt.ylabel("Number of Residence Halls")
    plt.show()

def main():
    colgate_url = "https://www.colgate.edu/academics/majors-minors"
    williams_url = "https://www.williams.edu/academics/areas-of-study/"
    hamilton_url = "https://www.hamilton.edu/academics/areas-of-study"
    url_c_housing = "https://www.colgate.edu/student-life/housing-and-dining/student-housing/residence-halls"
    url_w_housing = "https://campus-life.williams.edu/upperclassresidencehalls/"
    url_h_housing = "https://www.hamilton.edu/campuslife/where-to-live/residence-halls"
    # Retrieve subjects
    colgate_subjects = get_colgate_subjects(colgate_url)
    williams_subjects = get_williams_subjects(williams_url)
    hamilton_subjects = get_hamilton_subjects(hamilton_url)
   


    print("Colgate Academic Subjects:", colgate_subjects)
    print("Williams Academic Subjects:", williams_subjects)
    print("Hamilton Academic Subjects:", hamilton_subjects)
   
    # Create a Venn diagram
    
    plt.figure(figsize=(8, 8))
    venn = venn3(
        [colgate_subjects, williams_subjects, hamilton_subjects],
        ('Colgate', 'Williams', 'Hamilton')
    )
    plt.title("Academic Subjects Overlap Between Universities")
    plt.show()

    num_c= int(num_williams_houses(url_w_housing))
    num_w= int(num_hamilton_houses(url_h_housing))
    num_h= int(num_colgate_houses(url_c_housing))
    create_histogram(num_c, num_w, num_h)
    
    
# Run the program
if __name__ == "__main__":
    main()
