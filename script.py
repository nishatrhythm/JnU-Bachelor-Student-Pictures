import requests
from bs4 import BeautifulSoup
import os

# URL of the HTML page containing the image links
url = 'http://139.59.112.45/jnuis/student_pictures/bachelor/2019-20/'

# Send a GET request to fetch the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags that contain links to images
image_links = soup.find_all('a', href=lambda href: (href and href.endswith('.jpg')))

# Create a directory to save the images if it doesn't exist
save_dir = './student_pictures_2019_20'
os.makedirs(save_dir, exist_ok=True)

# Iterate through the image links, download and save each image
for link in image_links:
    image_url = url + link['href']  # Full URL of the image
    image_name = link['href']  # Name of the image file
    image_path = os.path.join(save_dir, image_name)
    
    # Download the image
    with open(image_path, 'wb') as f:
        img_response = requests.get(image_url)
        f.write(img_response.content)
    
    print(f"Downloaded {image_name}")

print("All images downloaded successfully.")