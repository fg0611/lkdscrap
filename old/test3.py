import re
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

def scrape_linkedin_job_title(url):

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-shm-usage")

    # service = Service(ChromeDriverManager(driver_version="133.0.6943.60").install())
    service = Service("C:\\Users\\Francisco\\Desktop\\DEV_STUFF\\EMPLOYMENT\\scrap\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)


    # si la ruta es https://ar.linkedin.com/jobs/view/front-end-developer-at-viseven-4148153850?position=1&pageNum=0&refId=BP%2F0Qvw1Qo757y885i0tGQ%3D%3D&trackingId=39dYqsSBK9VRgo6cC2x4NQ%3D%3D
    # es decir que no contiene https://www.linkedin.com/
    # extraer el ID dejando solo los numeros que se encuentren antes de "?" y colocarlo dentro de una ruta asi:
    # https://www.linkedin.com/jobs/view/<ID> 
    # esta sera la nueva url

    # URL original
    # url = "https://ar.linkedin.com/jobs/view/front-end-developer-at-viseven-4148153850?position=1&pageNum=0&refId=BP%2F0Qvw1Qo757y885i0tGQ%3D%3D&trackingId=39dYqsSBK9VRgo6cC2x4NQ%3D%3D"

    # Verificar si la URL contiene 'linkedin.com/jobs/view/'
    if "linkedin.com/jobs/view/" not in url:
        # Extraemos la parte de la URL antes del "?"
        url_before_query = url.split('?')[0]
        # Aplicamos una regex para extraer solo los números (ID)
        match = re.search(r'-(\d+)', url_before_query)
        if match:
            job_id = match.group(1)  # El ID es el número encontrado
            print("El ID del trabajo es:", job_id)
        else:
            print("No se encontró el ID en la URL.")
    else:
        print("La URL ya contiene 'linkedin.com/jobs/view/', no es necesario modificarla.")

    driver.get(url)   
    # time.sleep(500)

    time.sleep(random.uniform(3, 5)) # Esperar unos segundos
    
    # remover top-level-modal-container
    try:
        # Intentar encontrar y eliminar el modal si está presente
        modal_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'top-level-modal-container')]")))
        driver.execute_script("arguments[0].remove();", modal_element)
        time.sleep(random.uniform(1, 3))
    except:
        print("No se encontró ningún modal para cerrar.")

    
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(random.uniform(1,2))

    # Suponiendo que la página ya está cargada
    # buscar un boton llamado cuya clase contenga "show-more" y hacer click en el mismo
    try:
        # Esperar hasta que el botón con clase 'show-more' esté presente y sea clickeable
        show_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class*='show-more']"))
        )
        
        # Hacer clic en el botón
        show_more_button.click()
        print("Botón 'show-more' clickeado con éxito.")

    except Exception as e:
        print("Error al encontrar o hacer clic en el botón 'show-more':", e)
    # try:
    #     # Buscar el botón cuya clase contenga "show-more" y hacer clic
    #     show_more_button = driver.find_element(By.CSS_SELECTOR, "[class*='show-more']")
    #     show_more_button.click()
    #     print("Botón 'show-more' clickeado con éxito.")
    # except Exception as e:
    #     print("Error al encontrar o hacer clic en el botón 'show-more':", e)
    # time.sleep(random.uniform(1, 3)) # Esperar unos segundos

    # Declarar las variables como cadenas vacías
    title = ''
    company = ''
    location = ''
    published = ''
    applicants = ''

    # Asignar título
    # el titulo de la busqueda se encuentra en un <h1> cuya clase contiene "top-card-layout__title"
    try:
        title = driver.find_element(By.CSS_SELECTOR, "h1[class*='top-card-layout__title']")
        title = title.text.strip()
    except Exception as e:
        print("Error al obtener el título:", e)

    # Asignar empresa
    # declarar la var company como string vacio, asignar texto de elemento cuya clase contenga "topcard__org-name"  
    try:
        company = driver.find_element(By.CSS_SELECTOR, "[class*='topcard__org-name']").text
    except Exception as e:
        print("Error al obtener la empresa:", e)

    # Asignar ubicación
    # declara var location como string vacio, asignar texto de elemento cuya clase contenga "topcard__flavor topcard__flavor--bullet"
    try:
        location = driver.find_element(By.CSS_SELECTOR, "[class*='topcard__flavor topcard__flavor--bullet']").text
    except Exception as e:
        print("Error al obtener la ubicación:", e)

    # Asignar fecha de publicación
    # declara var published como string vacio, asignar texto de elemento cuya clase contenga "posted-time-ago"
    try:
        published = driver.find_element(By.CSS_SELECTOR, "[class*='posted-time-ago']").text
    except Exception as e:
        print("Error al obtener la fecha de publicación:", e)

    # Asignar número de postulantes
    # declara var applicants como string vacio, asignar texto de elemento cuya clase contenga "num-applicants"
    try:
        applicants = driver.find_element(By.CSS_SELECTOR, "[class*='num-applicants']").text
    except Exception as e:
        print("Error al obtener el número de postulantes:", e)

    # declarar la var description como string vacio
    # buscar todo texto mayor a 4 caracteres que se encuentre dentro de elemento con clase 
    # "show-more-less-html__markup relative overflow-hidden"
    # y concatenarlo a la varible description

    # Declarar la variable description como una cadena vacía
    description = ''

    try:
        # Buscar el elemento con la clase "show-more-less-html__markup relative overflow-hidden"
        elements = driver.find_elements(By.CSS_SELECTOR, ".show-more-less-html__markup.relative.overflow-hidden")

        # Filtrar los textos de los elementos que tengan más de 4 caracteres y concatenarlos a description
        for element in elements:
            text = element.text.strip()  # Extraemos el texto y lo limpiamos de espacios en blanco
            if len(text) > 4:
                description += text + " "  # Concatenar el texto a la variable description
        # Imprimir la variable description
        # print("Description:", description)
        description = description.join(text.split())

    except Exception as e:
        print("Error al obtener el texto:", e)

    # Imprimir los resultados
    # print("Title:", title)
    # print("Company:", company)
    # print("Location:", location)
    # print("Published:", published)
    # print("Applicants:", applicants)
    # print("Description:", description)
    
    driver.quit()

scrape_linkedin_job_title("https://ar.linkedin.com/jobs/view/front-end-developer-at-viseven-4148153850?position=1&pageNum=0&refId=BP%2F0Qvw1Qo757y885i0tGQ%3D%3D&trackingId=39dYqsSBK9VRgo6cC2x4NQ%3D%3D")
