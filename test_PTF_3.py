import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from unidecode import unidecode



@pytest.fixture()

def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://nahual.github.io/qc-provinciano-evolution/provinciano.html?v=2")
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
        print(list)    
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
        print(list)  
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
        print(list)    
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
        print(list)    
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
        print(list)    
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
    
def test_nombre(driver):
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
        print(list)   
    data_prov = []
    for lista in lists:
        data_prov.append(lista[1])
    expected_prov = ['Catamarca']
    assert data_prov[0] == expected_prov[0], f"No se en cuentra datos de {expected_prov[0]} en la grilla. "
        
def test_nombre_no_contenido(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Gama")
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
        print(list)   
    mensaje = []
    for lista in lists:
        try:
            mensaje.append(lista[1])
        except:
            mensaje.append(lista[0])
    expected_mensaje = ['No hay provincias que coincidan con lo buscado']
    assert mensaje[0] == expected_mensaje[0], f"El mensaje que se visualiza no es el esperado"

def test_color_de_flecha(driver):
    flechas = driver.find_elements(By.CLASS_NAME,'sorter') 
    expected_color = True
    for flecha in flechas:
        flecha.click()
        driver.implicitly_wait(1)
        flecha_clickeada = driver.find_elements(By.CLASS_NAME,'active_sort')
        color_flecha = flecha_clickeada[0].value_of_css_property('color')
        print(color_flecha)
        if color_flecha != 'rgba(255, 0, 0, 1)':
            expected_color = False
    assert expected_color, f'Las flechas de ordenamiento no se ponen de color rojo'
    
def test_orden_de_datos(driver):
    flechas = driver.find_elements(By.CLASS_NAME,'sorter')
    datos_asc = []
    datos_desc = []
    nim = 0
    for x in range(0,len(flechas)):
        flechas[x].click()
        driver.implicitly_wait(1)
        table = driver.find_element(By.XPATH,'//*[@id="data"]/tbody')
        filas = table.find_elements(By.TAG_NAME,'tr')
        lists =[]
        for fila in filas:
            list = []
            celdas = fila.find_elements(By.TAG_NAME,'td')
            for celda in celdas:
                celda = celda.text
                try:
                  celda = unidecode(celda)
                  celda = celda.replace(".","")
                  celda = int(celda)
                except:
                  celda = unidecode(celda)
                  celda = celda.replace(".","")
                list.append(celda)
            lists.append(list)
        if nim == x:
            datos_asc.append(lists)
            nim += 2
        else:
            datos_desc.append(lists)     
    celda = 0
    columnas_asc = []  
    for asc in datos_asc:
        celda_asc=[]
        for prov in asc:
            celda_asc.append(prov[celda])
        columnas_asc.append(celda_asc)
        celda += 1
    idex = 0    
    columnas_desc = []  
    for desc in datos_desc:
        celda_desc =[]
        for prov in desc:
            celda_desc .append(prov[idex])
        columnas_desc.append(celda_desc)
        idex += 1    
    orden = True
    for columna in columnas_asc:
        print(f'Datos ascendentes: {columna}')
        print()
        if all(columna[i] >= columna[i + 1] for i in range(len(columna) - 1)):
            orden = False
    for columna in columnas_desc:
        print(f'Datos descendentes: {columna}')
        print()
        if all(columna[i] <= columna[i + 1] for i in range(len(columna) - 1)):
            orden = False
    assert orden, f'No todos los datos estan ordenados'        

def test_visualizar_columnas(driver):
    select = driver.find_element(By.XPATH, '//*[@id="data"]/thead/tr')
    columnas = select.find_elements(By.TAG_NAME,'th')
    colum_name = []
    for columna in columnas:
        name = columna.find_element(By.TAG_NAME,'span').text
        colum_name.append(name)
    print(colum_name)
    expected_columnas = ['Región', 'Nombre', 'Capital', 'Habitantes', 'Km2']    
    assert colum_name == expected_columnas, f'El el orden de las columnas no es el esperado'

#def test_verificar_info(driver):
#    service = Service(ChromeDriverManager().install())
#    wiki = webdriver.Chrome(service=service)
#    wiki.get("https://es.wikipedia.org/wiki/Provincias_de_Argentina")
#         
#    
#
#x = driver()
#test_verificar_info(x)
#x.close()

    
    
    