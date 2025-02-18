import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def linkedin_search(url):
    options = Options()
    options.add_argument("--disable-webrtc")  # Deshabilita WebRTC
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Simulación de usuario real
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # service = Service(ChromeDriverManager(driver_version="133.0.6943.60").install())
    service = Service("C:\\Users\\Francisco\\Desktop\\DEV_STUFF\\EMPLOYMENT\\scrap\\drivers\\chromedriver.exe")
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.linkedin.com/jobs/search/?keywords=data%20analyst")

        # Evita que el navegador se cierre automáticamente
    # input("Presiona Enter para cerrar el navegador...")
    # driver.quit()
    time.sleep(5)  # Espera a que cargue la página

    try:
        # Buscar el modal
        modal = driver.find_element(By.XPATH, "//*[@id='base-contextual-sign-in-modal']")        
        # Hacer scroll hacia el modal para asegurarse de que sea interactuable
        ActionChains(driver).move_to_element(modal).perform()        
        # Eliminar el modal del DOM
        driver.execute_script("arguments[0].remove();", modal)        
        print("Modal eliminado correctamente.")
    except:
        print("No se encontró el modal, continuando ejecución...")

    try:
        # Buscar el segundo modal
        modal = driver.find_element(By.CSS_SELECTOR, "div.blurred-overlay")        
        # Hacer scroll hacia el modal para asegurarse de que sea interactuable
        ActionChains(driver).move_to_element(modal).perform()        
        # Eliminar el modal del DOM
        driver.execute_script("arguments[0].remove();", modal)        
        print("Modal eliminado correctamente.")
        time.sleep(random.uniform(3, 6))  # Espera a que cargue la página
    except:
        print("No se encontró el modal, continuando ejecución...")
        
        
    job_list = []

    try:
        job_elements = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search__results-list li")
        
        for job_element in job_elements:
            try:
                # Locate the <a> element containing both the title and URL
                job_link = job_element.find_element(By.CSS_SELECTOR, "a.base-card__full-link")
                job_url = job_link.get_attribute("href")
                # Extract job title from within the <a> element
                try:
                    job_title = job_link.find_element(By.CLASS_NAME, "sr-only").text.strip()
                except:
                    job_title = "No title found"           
            except:
                job_url = "No URL found"
            try:
                company = job_element.find_element(By.CLASS_NAME, "hidden-nested-link").text.strip()
            except:
                company = "No company name found"
            try:
                location = job_element.find_element(By.CLASS_NAME, "job-search-card__location").text.strip()
            except:
                location = "No location found"
            try:
                time_posted = job_element.find_element(By.CLASS_NAME, "job-search-card__listdate").text.strip()
            except:
                time_posted = "No time posted"

            job_list.append({
                "title": job_title, 
                "company": company, 
                "location": location, 
                "published": time_posted, 
                "url": job_url
            })

    except Exception as e:
        print(f"Error: {e}")



    print(job_list)   
    driver.quit()
    return job_list

linkedin_search("")