from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
     # Accedemos a pagina ppal
    libro="Ingenieria del software de Pressman"
    
    try: 
        try:
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 5)
            driver.get("https://www.um.edu.ar/biblio/")
            driver.maximize_window()
        except:
            print("La web de la facultad no responde")

    # Accedemos a web de la biblio
        try:
            element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Ir al Catálogo")))
            driver.execute_script("arguments[0].click();", element)
        except:
            print("La web de la biblioteca no responde")

    # Switcheamos la pestana y buscamos el libro
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

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
            
main()