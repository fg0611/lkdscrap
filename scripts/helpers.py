import re
import urllib.parse


# Función para convertir a días
def to_days(text):
    if not isinstance(text, str):
        return 0
    text = text.lower()  # Convertir a minúsculas para manejar mayúsculas y minúsculas
    # Extraer el número usando una expresión regular
    numero = int(re.search(r"\d+", text).group())

    # Determinar la unidad de tiempo
    if "día" in text or "dia" in text or "day" in text:
        return numero
    elif "semana" in text or "week" in text:
        return numero * 7
    elif "mes" in text or "month" in text:
        return numero * 30
    else:
        return 0  # Si no se reconoce el formato


def fix_url(url):
    # Verificar si la URL contiene 'linkedin.com/jobs/view/'
    urlMatch = "linkedin.com/jobs/view/"
    # Expresión regular para extraer el ID
    match = re.search(r"/view/.*?-(\d+)(\?|$)", url)
    # Verificar si se encontró un match
    if match:
        id = match.group(1)  # Extraer el ID
        return f"{urlMatch}{id}"


def gen_query_url(query):
    if not isinstance(query, str):
        print("La consulta debe ser un string.")
        return None
    sub_search = '"remote" English -"Argentina" -"Brazil" -"Mexico" -"Colombia" -"Chile" -"Peru" -"Spanish" -"Portuguese"'
    base_url = "https://www.google.com/search"
    params = {"q": f"site:linkedin.com/jobs {query} {sub_search}"}
    search_url = base_url + "?" + urllib.parse.urlencode(params)
    print(search_url)
    return search_url
