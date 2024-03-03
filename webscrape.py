import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import ClothingClassifier
#import ColourClassifier

urls=['https://www.myer.com.au/c/men/mens-clothing/t-shirts/logo?promo_position=Men%27s%20T-Shirts%7C1%7C1%7Ctile-category&promo_id=e711f451-4e0a-4173-9729-60cb9fc75e4b&promo_creative=MENS_Nav%20Tiles_CAT_TILE_C_2.png&promo_name=2023-02-20%7CLogo%7CNon%20promo&promo_position=Men%27s%20T-Shirts%7C1%7C1%7Ctile-category&promo_id=f015ffc8-b444-4d28-b8fd-cc998fc9d562&promo_creative=SS24_WK3-PLP_CAT_TILE_A_2.jpg&promo_name=2024-02-07%7CLogo%7CNon%20promo']

def scrape_products(urls):
    """ Loads link(s) of websites and scrapes clothing information

    Args:
        url (str[]): Array of URL's of websites to scrape

    Returns:
        _type_: dict{}
    """

    data=[]
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
          
        # Find all product items on the page
        product_items = soup.find_all('li',class_='css-1uzpf0u')

        # Loop through each product item and extract relevant information
        for product_item in product_items:
            #product id
            product_id = product_item['id']

            # Extract product price
            #product_price = product_item.select_one("span[data-automation*=product-price]").text

            # Extract product image URL
            product_image_url = product_item.find('img')['src']
            product_type = ClothingClassifier.typeclassify_image_from_url(product_image_url)
            #product_colour = ColourClassifier.colourclassify_image_from_url(product_image_url)

            # Extract product page URL
            # Currently using myer TODO: make product 
            product_page_url = "https://www.myer.com.au"+product_item.find('a')['href']
            
            # Print or store the extracted information

            #print("Price:", product_price)
            
            data.append({"id":product_id,"pageurl":product_page_url,"imageurl":product_image_url,"type":product_type})


    return data




# Call the function to initiate scraping
#Colours are manually coded into the json file (for now)

data = scrape_products(urls=urls)
with open("clothingdata.json","w") as f:
    json.dump(data,f)


#TODO: AI for colour classification (AI may not be needed) and make init file
#TODO: Load data to main program
#TODO: optimize?