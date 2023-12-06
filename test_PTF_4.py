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
    driver.get("https://nahual.github.io/qc-provinciano-evolution/provinciano.html?v=2")
    #return driver
    yield driver
    driver.quit()

def test_visualizar_btn(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Beta")
    try:
        btn_exportar = driver.find_element(By.XPATH,'//*[@id="export"]/a')
        print(f'Se visualiza correctamente el boton Exportar : {btn_exportar}')
        assert True,f'No se visualiza el boton Expotar en la pantalla principal'
    except:
        assert False, F'No se visualiza el boton Expotar en la pantalla principal'

def test_btn_exportar_con_datos(driver):
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
    mensage = 'No hay provincias que coincidan con lo buscado'
    if data_prov[0] != mensage:
        export = driver.find_element(By.XPATH,'//*[@id="export"]/a')
        export.click()
        dialog = driver.find_element(By.XPATH,'/html/body/div[3]')
        print(dialog)
        dialog = dialog.get_attribute("role")
        assert dialog == 'dialog', f"Se abre correctamente la ventana para Exportar los datos."
    else:
        assert data_prov[0] != mensage, f'No hay provincias que coincidan con lo buscado' 
        
def test_exportar_sin_datos(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Beta")
    export = driver.find_element(By.XPATH,'//*[@id="export"]/a')
    export.click()
    notification = driver.switch_to.alert
    texto_alerta = notification.text
    print(f'Se abre correctamente la notificacion: {texto_alerta}')
    driver.switch_to.alert.accept()
    expected_text = 'No hay datos para exportar, ¿Desea exportar los nombres de las columnas?'
    assert texto_alerta == expected_text, f'La notificacion no es la esperada'
    
def test_aceptar_notificacion(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Beta")
    export = driver.find_element(By.XPATH,'//*[@id="export"]/a')
    export.click()
    driver.switch_to.alert.accept()
    dialog = driver.find_element(By.XPATH,'/html/body/div[3]')
    print(f"Se abre correctamente la ventana Expotar: Attribute {dialog}")
    dialog = dialog.get_attribute("role")
    assert dialog == 'dialog', f"No se abre la ventana Exportar."
    
def test_cancelar_notificacion(driver):
    filtro = driver.find_element(By.XPATH, '//*[@id="input"]')
    filtro.click()
    filtro.send_keys("Beta")
    export = driver.find_element(By.XPATH,'//*[@id="export"]/a')
    export.click()
    driver.switch_to.alert.dismiss()
    try:
        dialog = driver.find_element(By.XPATH,'/html/body/div[3]')
        dialog = dialog.get_attribute("role")
        assert False, f"Se cancela notificacion,Pero se visualiza la ventana Exportar y no la pantalla principal : {dialog}"
    except:
        print("Se muestra correctamente la pantalla principal")
        assert True
        
    
#x = driver()
#test_cancelar_notificacion(x)
#x.close()
