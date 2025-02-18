import os
import pandas as pd
import csv

def list_to_csv(list, filename):
    """
    Guarda una lista de URLs en un archivo CSV en una columna llamada 'urls'.
    :param list: Lista de strings con las URLs a guardar.
    :param filename: Nombre del archivo CSV donde se guardarán los datos.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["urls"])  # Escribir encabezado

        for url in list:
            writer.writerow([url])
    print(f"Se guardaron {len(list)} URLs en '{filename}'.")

def get_csv_content(ruta_csv):
    with open(ruta_csv, mode="r", encoding="utf-8") as file:
        return csv.reader(file)

def read_csv(ruta_csv):
    with open(ruta_csv, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for fila in reader:
            print(fila)  # Imprime cada fila como una lista

def count_rows(ruta_csv):
    with open(ruta_csv, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Omitir la primera fila (encabezado)
        rows = sum(1 for _ in reader)  # Contar filas restantes
    print(f"El CSV tiene {rows} registros (sin contar el encabezado).")
    return rows

def manage_csv(urls_list, file_name):
    # Verifica si el archivo existe
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
    else:
        df = pd.DataFrame(columns=['urls'])
    
    # Agrega nuevas URLs al DataFrame
    new_data = pd.DataFrame({'urls': urls_list})
    df = pd.concat([df, new_data], ignore_index=True)
    df = df.drop_duplicates(subset=["urls"])
    
    # Guarda el archivo
    df.to_csv(file_name, index=False)
    print(f"Se han guardado {len(urls_list)} URLs en {file_name}.")

def manage_job_csv(data, file_name):
    # Verifica si el archivo existe
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
    else:
        df = pd.DataFrame(columns=['title', 'company', 'location', 'published', 'applicants', 'url', 'description'])
    
    # Insertar la lista como una nueva fila en el DataFrame
    df.loc[len(df)] = data
    df = df.drop_duplicates(subset=["url"])
    
    # Guarda el archivo
    df.to_csv(file_name, index=False)
    print(f"Se han guardado el dato URLs en {file_name}.")

import os
import pandas as pd

def csv_to_df(filepath):
    # Verifica si el archivo existe y es accesible
    if os.path.exists(filepath):
        try:
            # Intenta leer el archivo CSV
            df = pd.read_csv(filepath)
            return df
        except pd.errors.ParserError:
            print(f"El archivo '{filepath}' no es un CSV válido.")
            return None
        except Exception as e:
            print(f"No se pudo leer el archivo CSV: {e}")
            return None
    else:
        print(f"El archivo '{filepath}' no existe.")
        return None


# Uso del script
# file_name = "urls_storage.csv"
# urls_to_add = ["https://example1.com", "https://example2.com", "https://example3.com"]
# manage_csv(file_name, urls_to_add)