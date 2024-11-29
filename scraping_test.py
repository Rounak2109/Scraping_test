import requests 
from bs4 import BeautifulSoup 
import statistics 
import pprint
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
import time
from tests import *

# Function to get the size of the HTML in KB  
def median_calculation(prices_list):
    prices_list.sort()
    if len(prices_list)%2==0:
        mid1 = prices_list[len(prices_list) // 2 - 1] 
        mid2 = prices_list[len(prices_list) // 2] 
        median = (mid1 + mid2) / 2
    else:
        median = prices_list[len(prices_list) // 2]
    return median

def products_creation(product_link):
    
    driver_2 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver_2.get(product_link)

    time.sleep(2)
    html_content = driver_2.page_source 
    soup_2 = BeautifulSoup(html_content, 'html.parser')
    # oct-listers__pagination oct-listers__pagination-top oct-listers__pagination-top__no-chanel
    parent_div = soup_2.find('div',{'class':'templateMainContentArea'})
    # pprint.pprint(parent_div)
    child_div = parent_div.find_all('div',{'class':'oct-teaser__contents-panel--main-content'})
    # print(child_div , "--child div")
    print(len(child_div))
    
    products = []
    price_list = []
    for item in child_div:
        h3_tags = item.find_all('h3')
        review_tags = item.find('div',{'class':'oct-reviews'})
        
        # If There are no ratings then by default ratings will be "Not Mentioned"
        try:
            a_tags_within_review = review_tags.find('a')
            ratings = a_tags_within_review.get('aria-label')
        except Exception as e:
            ratings = "Not Mentioned"

        ''' Need to be created '''                
        short_description = item.find('div',{'class':'oct-button__content'})
        
        json_content = {}
        price = item.find('p')
        json_content = {'Price': float(price.text[1:]),'Ratings':ratings,'Title':h3_tags[1].text,'Price Unit': "\u00A3",'Page_Size':str(len(item)/1024)+"KB",'Short_description':""}

        products.append(json_content)
        price_list.append(float(price.text[1:])) 
        
    print(products)
    final_json = {}
    final_json["Product"] = products
    
    try:
        # Median Calculation
        median = median_calculation(price_list)
    except Exception as e:
        raise f"{e} as Exception"
    
    try:
        runner = unittest.TextTestRunner() 
        runner.run(suite(price_list,median))
        # medianTest.test_median()
    except Exception as  e:
        raise f"{e} as Exception"
    
    final_json["Median"] = median
    return final_json

def sleep_items_function(parent_div): 
    
    # swiper-wrapper swiper-wrapper--nudge
    child_divs = parent_div.find_all('div',{'class':'swiper-slide oct-carousel-horizontalnav-swiper-slide'})
    
    # Checking for the length of child divs
    print(len(child_divs))
    
    # swiper-slide oct-carousel-horizontalnav-swiper-slide swiper-slide-active
    links = []
    
    # Find all the a tags
    for item in child_divs:
        a_tags = item.find_all('a')
        for a in a_tags: 
            href = a.get('href') 
            if href: 
                links.append(href)

    print(links)
    total_items = []
    for product_link in links:
        final_json = products_creation(product_link)
        total_items.append(final_json)
    return total_items

def scrape_products(url):
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url) # URL of the website to scrape
    
    # Wait for a few seconds to let the page load completely 
    time.sleep(2) 

    # Get the page source 
    html_content = driver.page_source

    # Parsing with Beautiful Soup 
    soup = BeautifulSoup(html_content, 'html.parser') 
    
    try:
        parent_div = soup.find('div',{'class':'templateMainContentArea'})  

        # Function to find all the sleep items
        total_items = sleep_items_function(parent_div) 
    except Exception as e:
        raise f"{e} as Exception"  
    
    return total_items

def main(): 
    url = 'https://www.boots.com/health-pharmacy/medicines-treatments/sleep?paging.index=0&paging.size=24&sortBy=mostRelevant&criteria.category=wellness---sleep&criteriabb.brand=Bach+Rescue+Remedy---Boots'
    while True: 

        print("Press 1 to Run:")
        print("Press 2 to Exit from the Console:")
        console_input = int(input())
        if console_input==1:
            results = scrape_products(url) 
            print(results)
        elif console_input==2:
            break
        else:
            print("Please enter either 1 or 2:\n")
            continue

if __name__ == "__main__": 
    main()
    
