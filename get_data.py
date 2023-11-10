from selenium import webdriver
from selenium.webdriver.common.by import By
from unidecode import unidecode
driver = webdriver.Chrome()
query = "Novalgina Infantil".lower().replace(" ", "_")

def get_data (query):
    url = f"https://www.bulario.com/{query}"

    driver.get(url)

    data = driver.find_elements(By.CSS_SELECTOR, 'a[name="composicao"] ~ p > strong')

    vehicles = driver.find_elements(By.CSS_SELECTOR, 'a[name="composicao"] ~ p')

    filtered_veh = []
    for p in vehicles:
        if ("(Excipientes: " in p.text) or ("(Veículos: " in p.text):
            formatted = p.text.replace("(", "")
            formatted = formatted.replace(")", "")
            formatted = unidecode(formatted)
            filtered_veh.append(formatted)

    data_array = []
    for item in data:
        index = data.index(item)
        current_object = {}
        if index != len(data)-1:
            current_object = {
            "presentation": item.text,
            "vehicles": filtered_veh[index]
            }

        else:
            current_object = {"lab": item.text}
        data_array.append(current_object)

    return data_array