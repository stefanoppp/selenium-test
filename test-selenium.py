from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

def main():
     # Accedemos a pagina ppal
    libro="Ingenieria del software"
    autor="Pressman"
    try: 
        try:
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 20)
            driver.get("https://www.um.edu.ar/biblio/")
        except:
            print("La web de la facultad no responde")

    # Pagina biblioteca
        try:
            element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Ir al Catálogo")))
            driver.execute_script("arguments[0].click();", element)
        except:
            print("La web de la biblioteca no responde")

        try:
            new_window=driver.window_handles[1]
            driver.switch_to.window(new_window)
            search_bar=driver.find_element(By.ID,"translControl1")
            search_bar.send_keys(libro)
      
            go = driver.find_element(By.ID,"searchsubmit")
            go.click()
            
            confirm=driver.find_element(By.ID,"numresults")
            confirm = confirm.text
            print(confirm)
            
            book=driver.find_element(By.PARTIAL_LINK_TEXT, libro)
            book = book.text
            print(book)
            # search_bar.send_keys(Keys.RETURN)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
            
main()