import json
import sys

import requests
from bs4 import BeautifulSoup

# url = "https://declaration.rostrud.gov.ru/declaration/index"

#-------------------------------loading INN from json file--------------------------------------------
try:
    with open("INN.json") as file:
        INN = file.read()

    url = "https://declaration.rostrud.gov.ru/declaration/index?DeclarationSearch%5Binn%5D=" + INN + "&DeclarationSearch%5Bregion_id%5D=&DeclarationSearch%5Btele%5D=&DeclarationSearch%5Bverify%5D=0"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
#------------------------------------------------------------------------------------------------------

# website page loaded
    req = requests.get(url, headers=headers)
    src = req.text

#=========================saving and loading the html version of the site for offline use===========
    # with open("index.html", "w") as file:
    #     src = file.write(src)

    # with open("index.html") as file:
    #     src = file.read()
#===================================================================================================

    soup = BeautifulSoup(src, "lxml")

#------------------------------------search for html elements on a page-----------------------------------
    table_header = soup.find(class_="table-responsive kv-grid-container").find("thead").find_all("th")
    all_character = soup.find(class_="table-responsive kv-grid-container").find("tbody").find_all("td")
#---------------------------------------------------------------------------------------------------------

#set of variables for further use
    item_num = all_character[0].text
    item_date_in = all_character[1].text
    item_full_name = all_character[2].text
    item_location = all_character[3].text
    item_INN = all_character[4].text
    item_OGRN = all_character[5].text
    item_number_of_the_workplace = all_character[6].text
    item_specialty_of_the_employee = all_character[7].text
    item_number_of_employees = all_character[8].text
    item_name_organization_that_conducted = all_character[9].text
    item_details_of_the_expert = all_character[10].text
    item_validity = all_character[11].text
    item_declaration_termination_date = all_character[12].text

#-------------compiling a dictionary from the target data---------------------
    all_info = {}
    for i in range(0,12):
        headers = table_header[i + 11].text
        item = all_character[i].text
        all_info[headers] = item

    with open("all_info.json", "w") as file:
        json.dump(all_info, file, indent=4, ensure_ascii=False)
#-----------------------------------------------------------------------------
except Exception:
    e = sys.exc_info()
    print(e.args)
