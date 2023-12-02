import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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

def test_region_centro(driver):
    select = driver.find_element(By.XPATH, '//*[@id="region"]/option[3]')
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
        'Córdoba',
        'Entre Ríos',
        'Santa Fe'
        ]
    assert data_prov == expected_prov, f"Los datos de la Grilla no son los esperados"

def test_region_norte(driver):
    select = driver.find_element(By.XPATH, '//*[@id="region"]/option[4]')
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
        'Catamarca',
        'Chaco',
        'Corrientes',
        'Formosa',
        'Jujuy',
        'Misiones',
        'Salta',
        'Santiago del Estero',
        'Tucumán'
        ]
    assert data_prov == expected_prov, f"Los datos de la Grilla no son los esperados"
        
def test_region_cuyo(driver):
    select = driver.find_element(By.XPATH, '//*[@id="region"]/option[5]')
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
        'La Rioja',
        'Mendoza',
        'San Juan',
        'San Luis'
        ]
    assert data_prov == expected_prov, f"Los datos de la Grilla no son los esperados"

def test_region_patagonica(driver):
    select = driver.find_element(By.XPATH, '//*[@id="region"]/option[6]')
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
        'Chubut',
        'La Pampa',
        'Neuquén',
        'Río Negro',
        'Santa Cruz',
        'Tierra del Fuego, Antártida e Islas del Atlántico Sur']
    assert data_prov == expected_prov, f"Los datos de la Grilla no son los esperados"
    
def test_nombre_sin_acento(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Catamarca")
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
    expected_prov = ['Catamarca']
    assert data_prov == expected_prov, f"No se en cuentra datos de 'Catamarca' en la grilla. "
    
def test_nombre_sigla_p(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("C.A.B.A")
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
        try:
            data_prov.append(lista[1])
        except:
            data_prov.append(lista[0])
    expected_prov = ['Ciudad Autónoma de Buenos Aires']
    assert data_prov == expected_prov, f"{data_prov[0]}"
    
def test_nombre_ciudad(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("La Plata")
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
        try:
            data_prov.append(lista[1])
        except:
            data_prov.append(lista[0])
    expected_prov = ['Buenos Aires']
    assert data_prov == expected_prov, f"{data_prov[0]}"

def test_nombre_omitiendo_acento(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Cordoba")
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
        try:
            data_prov.append(lista[1])
        except:
            data_prov.append(lista[0])
    expected_prov = ['Córdoba']
    assert data_prov == expected_prov, f"{data_prov[0]}"


#x = driver()
#test_nombre_omitiendo_acento(x)
#x.close()

    
    
    