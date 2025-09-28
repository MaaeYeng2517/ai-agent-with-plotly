from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

element_list = []

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use a proper Service object
service = Service(ChromeDriverManager().install())

for page in range(1, 3):
    # Initialize driver properly
    driver = webdriver.Chrome(service=service, options=options)

    # Load the URL
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/tablets"
    driver.get(url)
    time.sleep(2)  # Optional wait to ensure page loads

    # Extract product details
    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    descriptions = driver.find_elements(By.CLASS_NAME, "description")
    ratings = driver.find_elements(By.CLASS_NAME, "ratings")

    # Store results in a list
    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text
        ])

    driver.quit()

# Display extracted data


# importing csv


# Data
data = element_list

# File path for the CSV file
csv_file_path = 'example1.csv'

# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerows(data)

# Print a confirmation message
print(f"CSV file '{csv_file_path}' created successfully.")