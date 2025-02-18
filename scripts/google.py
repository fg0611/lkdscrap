from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import urllib.parse

# from webdriver_manager.chrome import ChromeDriverManager
def gsearch(query):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Simulación de usuario real
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # service = Service(ChromeDriverManager(driver_version="133.0.6943.60").install())
    service = Service("C:\\Users\\Francisco\\Desktop\\DEV_STUFF\\EMPLOYMENT\\scrap\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    query = 'web developer'
    sub_search = '"remote" English -"Argentina" -"Brazil" -"Mexico" -"Colombia" -"Chile" -"Peru" -"Spanish" -"Portuguese"'
    base_url = "https://www.google.com/search"
    params = {
        "q": f"site:linkedin.com/jobs {query} {sub_search}"
    }

    search_url = base_url + "?" + urllib.parse.urlencode(params)
    print(search_url)

    # sub_search = '"remote" -Argentina -Brazil -Mexico -Colombia -Chile -Peru -Spanish -Portuguese' 
    # search_query = f"site:linkedin.com/jobs/{query} {sub_search}"
    # search_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query)}"

    driver.get(search_url)
    
    # Simulación de interacción humana con tiempos de espera aleatorios
    time.sleep(random.uniform(1, 3))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1, 3))
    
    try:
        # Esperar a que los resultados de búsqueda aparezcan
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        
        # Obtener todos los enlaces de los resultados de Google
        results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc a")
        job_links = [result.get_attribute("href") for result in results if "linkedin.com/jobs/" in result.get_attribute("href")]
        
        if not job_links:
            print("No se encontraron ofertas de trabajo en LinkedIn desde Google.")
        
    except Exception as e:
        print(f"Error al buscar en Google: {e}")
        job_links = []
    print(f'en google se encontraron {len(job_links)} urls')
    driver.quit()
    return job_links