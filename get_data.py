from selenium import webdriver
from selenium.webdriver.common.by import By
from unidecode import unidecode

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

def get_data (query):

    url = f"https://www.bulario.com/{query}"

    driver.get(url)
    data = driver.find_elements(By.CSS_SELECTOR, 'a[name="composicao"] ~ p > strong')

    vehicles = driver.find_elements(By.CSS_SELECTOR, 'a[name="composicao"] ~ p')
    response = {}
    filtered_veh = []
    data_array = []

    for p in vehicles:
        if ("(Excipientes: " in p.text) or ("(Veículos: " in p.text):
            formatted = p.text.replace("(", "")
            formatted = formatted.replace(")", "")
            formatted = unidecode(formatted)
            filtered_veh.append(formatted)

    for item in data:
        index = data.index(item)
        if index != len(data)-1:
            current_object = {
            "presentation": item.text,
            "vehicles": filtered_veh[index]
            }
            data_array.append(current_object)
        else:
            response["lab"] = item.text

    response["content"] = data_array

    return response
