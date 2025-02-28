import os
import logging
import time
from selenium import webdriver

# Crear carpetas si no existen
os.makedirs("capturas", exist_ok=True)
os.makedirs("reportes", exist_ok=True)

# Configuración básica de logging
logging.basicConfig(
    filename="reportes/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def start_driver(context):
    """Inicia WebDriver y maximiza la ventana."""
    logging.info("Iniciando WebDriver...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def quit_driver(context):
    """Cierra WebDriver."""
    if context.driver:
        logging.info("Cerrando WebDriver...")
        context.driver.quit()

def before_all(context):
    """Inicia todas las pruebas."""
    logging.info("Iniciando todas las pruebas...")
    start_driver(context)

def after_all(context):
    """Finaliza todas las pruebas."""
    logging.info("Finalizando todas las pruebas...")
    quit_driver(context)

def before_scenario(context, scenario):
    """Inicia temporizador y cuenta de pasos por escenario."""
    logging.info(f"Iniciando escenario: {scenario.name}")
    context.start_time = time.time()  # Guardamos el tiempo de inicio
    context.step_count = 0

def after_step(context, step):
    """Captura de pantalla después de cada paso y cuenta los pasos."""
    time.sleep(1)  # Pequeña espera para asegurar que la página cargue
    context.step_count += 1  # Incrementa el contador de pasos
    screenshot_name = f"step_{context.step_count}_{step.name}_{time.time()}.png"
    screenshot_path = os.path.join("capturas", screenshot_name)
    context.driver.save_screenshot(screenshot_path)
    logging.info(f"Captura de pantalla del paso {context.step_count}: {screenshot_path}")

def after_scenario(context, scenario):
    """Registra el resultado, duración y cantidad de pasos del escenario."""
    end_time = time.time()
    duration = end_time - context.start_time  # Calculamos la duración de la prueba
    if scenario.status == "passed":
        logging.info(f"Escenario {scenario.name} PASÓ en {duration:.2f} segundos y {context.step_count} pasos.")
    else:
        logging.error(f"Escenario {scenario.name} FALLÓ. Excepción: {str(scenario.exception)}. Duración: {duration:.2f} segundos. Pasos ejecutados: {context.step_count}")
