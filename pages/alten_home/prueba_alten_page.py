from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import random
from pages.pages import Page

class PruebaAltenPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.web = driver
        
        # STATIC lOCATORS
        # ----------------------------------------------------------------
        # ----------------------------------------------------------------
        # Input de texto "ESCRIBE POSICIÓN O TÉRMINO DE BÚSQUEDA"
        self.job_search_input = lambda: self.web.find_element(By.NAME, "job_search")
        
        # Bloque de Categorias en la tabla de empleo
        self.employment_categories = lambda: self.web.find_element(By.ID, "jobboard-filter-0-body")
        
        # Botón "Buscar Ofertas"
        self.find_jobs_button = lambda: self.web.find_element(By.CSS_SELECTOR, "#jobboard-jobboard-0 .btn")
        
        # Tabla de registros de empleos
        self.employee_table = lambda: self.web.find_element(By.CSS_SELECTOR, ".wp-block-jobboard-loop")
        
        # ----------------------------------------------------------------
        # ----------------------------------------------------------------
        
    # ACTIONS
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def get_employee_tabledata(self) -> list[dict]:
        """
        Obtiene los datos de la tabla de empleados y los organiza en una lista de diccionarios.
        
        Retorna:
            list[dict]: Lista donde cada diccionario representa una fila con las claves:
                - 'Titulo': Nombre del empleo.
                - 'Localizcion': Ubicación.
                - 'Fecha': Fecha de publicación.
                - 'Insignia': Estrellita :).
        """

        table_data = self.locators.get_table_data(self.employee_table())
        employee_tabledata = []
        
        for row in table_data:
            employee_row_data = {
                'Titulo': row[0],
                'Localizcion': row[1],
                'Fecha': row[2],
                'Insignia': row[3]
            }
            employee_tabledata.append(employee_row_data)
        
        return employee_tabledata
    # ----------------------------------------------------------------

    def auto_search_first_job(self):
        """
        Extrae el título de un empleo aleatorio en la tabla, lo limpia eliminando caracteres especiales y lo introduce en el buscador.
        
        - Obtiene el título de una fila aleatoria de la tabla de empleos.
        - Filtra el texto para eliminar cualquier símbolo o palabra adicional después de ellos.
        
        Este método automatiza la búsqueda sin necesidad de ingresar manualmente una palabra clave.
        """

        # Obtener la lista de empleos
        lista_empleos = self.get_employee_tabledata()

        if not lista_empleos:
            print("No hay empleos disponibles en la tabla.")
            return

        # Seleccionar un índice aleatorio
        indice_random = random.randint(0, len(lista_empleos) - 1)

        # Extraer y limpiar el título del empleo seleccionado
        titulo_empleo = lista_empleos[indice_random]["Titulo"]
        palabra_limpia = re.sub(r"[^\w\s]+.*", "", titulo_empleo).strip()

        # Ingresar la palabra clave en el campo de búsqueda
        campo_busqueda = WebDriverWait(self.web, 10).until(
            EC.visibility_of_element_located((By.NAME, "job_search"))
        )
        campo_busqueda.send_keys(palabra_limpia)

        # Ejecutar la búsqueda
        boton_buscar = self.web.find_element(By.CSS_SELECTOR, "#jobboard-jobboard-0 .btn")
        boton_buscar.click()


    
    # ----------------------------------------------------------------
        
    # ASSERTIONS
    # ----------------------------------------------------------------
    
    def should_have_matching_jobs(self):
        """
        Valida que existan empleos relacionados a la búsqueda realizada.
        """
        texto_buscado = self.job_search_input().get_attribute("value")
        
        empleos = self.get_employee_tabledata()
        
        assert any(texto_buscado in empleo["Titulo"] for empleo in empleos), "El valor no se encontró en los títulos"
    
    # ----------------------------------------------------------------


    # ----------------------------------------------------------------