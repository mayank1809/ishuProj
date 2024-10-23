import requests
from bs4 import BeautifulSoup
import json

def scrape_courses():
    # Replace with the actual URL of Analytics Vidhya's free courses page
    url = "https://www.analyticsvidhya.com/academy/courses/free/"
    
    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Placeholder for the courses
    courses = []
    
    # Find and extract course details (adjust selectors as needed)
    for course in soup.find_all('div', class_='course-card'):
        title = course.find('h3').get_text(strip=True)
        description = course.find('p').get_text(strip=True)
        # Assuming course curriculum may be in a list format, adjust based on actual HTML
        curriculum = [li.get_text(strip=True) for li in course.find_all('li')]
        
        # Append to the list of courses
        courses.append({
            'title': title,
            'description': description,
            'curriculum': curriculum
        })
    
   # Use the absolute path to the courses.json file
    save_path = 'C:/Users/mt166/Ishu_Proj/analytics_vidhya_search/data/courses.json'
    
    # Save to JSON file
    with open(save_path, 'w') as f:
        json.dump(courses, f, indent=4)

if __name__ == "__main__":
    scrape_courses()
