import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


@pytest.fixture()

def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://nahual.github.io/qc-provinciano-evolution/provinciano.html?v=1")
    #return driver
    yield driver
    driver.quit()

def test_region_ninguna(driver):
    select = driver.find_element(By.XPATH, '//*[@id="region"]/option[2]')
    select.click()
    table = driver.find_element(By.XPATH,'//*[@id="data"]/tbody')
    filas = table.find_elements(By.TAG_NAME,'tr')
    lists =[]
    for fila in filas:
        list = []
        celdas = fila.find_elements(By.TAG_NAME,'td')
        for celda in celdas:
            celda = celda.text
            list.append(celda)
        lists.append(list)    
    data_prov = []
    for lista in lists:
        data_prov.append(lista[1])
    expected_prov = [
        'Ciudad Autónoma de Buenos Aires',
        'Buenos Aires'
        ]
    assert data_prov == expected_prov, f"Los datos de la Grilla no son los esperados"
        
    

#x = driver()
#test_region_ninguna(x)
#x.close()

    
    
    