import bs4
import requests

# requestObj = requests.get("https://www.fortytwo.sg/dining/dining-tables/ryder-round-table-black.html")
requestObj = requests.get("https://www.fortytwo.sg/dining/dining-tables.html")


requestObj.raise_for_status()
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')
list_url = []  # list of url place holder

# loop through whole document to collect href links in www.fortytwo.sg/dining/dining-tables domain
for a in soup.find_all('a', href=True):
    if(a['href'][:45] == 'https://www.fortytwo.sg/dining/dining-tables/'):
        print("Found the URL:" + a['href'])
        list_url.append(a['href'])
print(len(list_url))
list_url = list(dict.fromkeys(list_url))  # remove duplicates
print("After removing duplicates: {}".format(len(list_url)))
# proof of concept pick the first url for web scrap the product pricing

requestObj = requests.get(list_url[0])
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')

#web scrape for all the product-pricing ids.
product_price=[]
for p in soup.findAll(True,{'id':True}) :
    # print(p['id'])
    if p['id'][:14]=='product-price-':
        print(p['id'])
        product_price.append(p['id'])

print(len(product_price))

for i in product_price:
    # print(i)
    #           <id='product-price-43727'>
    element = soup.select('#'+i)   # html element - id-#,  .-class
    print(element[0].text)
    element = soup.select('.item-title')
    print(element[0].text)
    print(element[1].text)
    print(element[2].text)
    print(element[3].text)

print(list_url[0])


