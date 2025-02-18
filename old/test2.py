from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# from webdriver_manager.chrome import ChromeDriverManager
def search_google_for_linkedin_jobs(query):
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
    
    search_url = f"https://www.google.com/search?q=site:linkedin.com/jobs/ {query}"
    # search_url = f"https://www.google.com/search?q=site:linkedin.com/jobs/web developer remote"
    print(search_url)
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
    
    driver.quit()
    return job_links

if __name__ == "__main__":
    query = "Web developer remote mexico"
    # query = "Data Analyst"
    linkedin_job_links = search_google_for_linkedin_jobs(query)
    
    for link in linkedin_job_links:
        print(link)