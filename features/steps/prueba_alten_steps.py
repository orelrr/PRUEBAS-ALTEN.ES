from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from pages.alten_home.prueba_alten_page import PruebaAltenPage


# Paso para navegar a la URL
@given('que el usuario está en la tabla de búsqueda de empleo localizada en la url "{url}"')
def step_ir_a_url(context, url):
    print("Accediendo a la URL:", url)
    context.driver.get(url)
    # Creamos una instancia
    alten_page = PruebaAltenPage(context.driver)
    # Espera a que el elemento principal se haga visible
    main_element = context.driver.find_element(By.ID, "jobboard-filter-0-body")
    alten_page.helpers.wait_for_element(main_element)
    # Hacemos scroll hasta la ubicacion del elemento seleccionado
    actions = ActionChains(context.driver)
    actions.move_to_element(main_element).perform()

@when('ingresa la palabra clave en el campo de búsqueda y presiona Buscar Ofertas')
def step_ingresar_palabra(context):
    # Creamos una instancia
    alten_page = PruebaAltenPage(context.driver)
    # Ingresamos y buscamos uan palabra clave en el campo de búsqueda
    alten_page.auto_search_first_job()
    
@then('se muestran los resultados de las ofertas relacionadas')
def step_ver_resultados(context):    
    # Creamos una instancia
    alten_page = PruebaAltenPage(context.driver)
    # Valida que existan empleos relacionados a la búsqueda realizada.
    alten_page.should_have_matching_jobs()
