from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()

    driver.get("https://www.um.edu.ar/biblio/")
    boton=driver.find_element(By.PARTIAL_LINK_TEXT, "Ir al Catálogo")
    
    boton.click()
    # driver.quit()
main()