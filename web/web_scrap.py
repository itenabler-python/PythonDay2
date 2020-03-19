#https://www.fortytwo.sg/dining/dining-tables/ross-dining-table-walnut.html

import bs4
import requests

requestObj = requests.get("https://www.fortytwo.sg/dining/dining-tables/ryder-round-table-black.html")
requestObj.raise_for_status()
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')

html_link = soup.select("a href")
elements = soup.select("#product-price-25087")  # html id - element #
print(elements[0].text)

elements = soup.select(".warranty-information")  # html class -element .
print(elements[0].text)


