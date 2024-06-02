import requests
from bs4 import BeautifulSoup
target_url = "https://www.example.com/"  
data_to_extract = ["h1 title"]  
def scrape_data(url):
  try:
    response = requests.get(url)
    response.raise_for_status() 
    soup = BeautifulSoup(response.content, "html.parser")
    extracted_data = []
    for element in data_to_extract:
      data_points = []
      for item in soup.select(element):
        data_points.append(item.text.strip())
      extracted_data.append({"element": element, "data": data_points})
    return extracted_data
  except requests.exceptions.RequestException as e:
    print(f"Error occurred during request: {e}")
    return []
scraped_data = scrape_data(target_url)
print(scraped_data)
