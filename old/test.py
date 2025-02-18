from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_mt4_texts(url):
    options = Options()
    # options.add_argument("--headless")  # Descomenta para ejecutar sin interfaz gráfica
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # service = Service(ChromeDriverManager(driver_version="133.0.6943.60").install())
    service = Service("C:\\Users\\Francisco\\Desktop\\DEV_STUFF\\EMPLOYMENT\\scrap\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    try:
        # Esperar hasta que al menos un elemento con la clase 'mt4' esté presente
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mt4")))
        
        elements = driver.find_elements(By.CLASS_NAME, "mt4")
        extracted_texts = []
        
        for element in elements:
            for sub_element in element.find_elements(By.XPATH, ".//*"):
                text = sub_element.text.strip()
                if len(text) > 3:
                    extracted_texts.append(text)
        
        if not extracted_texts:
            print("No se encontró texto con más de 3 caracteres dentro de los elementos 'mt4'.")
        
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        extracted_texts = []
    
    driver.quit()
    return extracted_texts

if __name__ == "__main__":
    url = "https://www.linkedin.com/jobs/search/?currentJobId=3784464379"
    texts = extract_mt4_texts(url)
    for text in texts:
        print(text)
