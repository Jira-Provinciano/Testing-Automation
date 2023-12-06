import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture()

def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://nahual.github.io/qc-provinciano-evolution/provinciano.html?v=2")
    #return driver
    yield driver
    driver.quit()

def test_title(driver):
    heading1 = driver.find_element(By.XPATH, '/html/body/h1').text
    print(heading1)
    expected_title = "Provinciano Evolution"
    assert heading1 == expected_title, f"El título actual '{heading1}' no coincide con el esperado '{expected_title}'"

def test_subtitle(driver):
    subheading1 = driver.find_element(By.XPATH, '/html/body/p').text
    print(subheading1)
    expected_subtitle = "Buscador de datos sobre Provincias de la República Argentina"
    assert subheading1 == expected_subtitle, f"El título actual '{subheading1}' no coincide con el esperado '{expected_subtitle}'"

def test_region(driver):
    element = driver.find_element(By.XPATH,'//*[@id="region"]')
    list = element.find_elements(By.TAG_NAME, 'option')
    opciones = []
    for option in list:
        opciones.append(option.get_attribute("value"))
    expected_element = [
        'Todas',
        'Ninguna',
        'Centro',
        'Norte Grande Argentino',
        'Nuevo Cuyo',
        'Patagónica'      
    ]
    dif = True
    for indice in range(0,len(expected_element)):
        if opciones[indice] != expected_element[indice]:
            dif = False
    print(opciones)
    assert dif == True, f"La lista de opciones '{element}'. No coincide con el orden esperado'"
        
def test_nombre(driver):
    input = driver.find_element(By.XPATH,"//body/div/form/input[@id='input']")    
    input_now = input.get_attribute("value")
    expected_input = ""
    print('Filtro Nombre: None')
    assert input_now == expected_input, f"El filtro nombre no se encuentra vacio por defecto"

#x = driver()
#test_region(x)
#x.close()
#print("closed")