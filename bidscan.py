from bs4 import BeautifulSoup
from pathlib import Path
import requests
import agency

#the st. lucie page is dynamically generated using javascript. Need to use a selenium library. Comments for it are here: https://stackoverflow.com/questions/56455255/beautifulsoup-find-all-returns-nothing

agencies = []
city_of_stuart = agency.Agency("City of Stuart", "https://fl-stuart.civicplus.com/bids.aspx", "city_of_stuart.txt", "bid_section = soup.find_all('div', class_='pageStyles')")
city_of_port_st_lucie = agency.Agency("City of Port St. Lucie", "https://www.demandstar.com/app/agencies/florida/city-of-port-st-lucie-procurement-management-department/procurement-opportunities/e3fcaaaf-f326-40ce-876d-5bec54a221ef/", "city_of_port_st_lucie.txt", "bid_section = soup.find_all('body', class_='light_DS')")
agencies.append(city_of_stuart)
agencies.append(city_of_port_st_lucie)

def button_test(agency):
    print(agency.name)

def bidscan(agency):
    html_text = requests.get(agency.site).text
    soup = BeautifulSoup(html_text, "lxml")
    bid_section = []
    exec(agency.search_string)
    current_bid_text = ""
    for element in bid_section:
        current_bid_text += str(element)

    old_bid_text = Path(agency.text_file).read_text()

    true_text = "No changes to bid section."
    false_text = "New bid information available."

    if current_bid_text == old_bid_text:
        return true_text
    else:
        new_bid_text = open(agency.text_file, "w")
        new_text = ""
        for element in bid_section:
            new_text += str(element)
        new_bid_text.write(new_text)
        new_bid_text.close()
        return false_text
