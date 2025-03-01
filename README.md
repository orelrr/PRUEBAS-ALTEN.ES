# 📌 README - PRIMERA_PRUEBA

Este proyecto es un ejemplo de automatización de pruebas con **Selenium**, **Python** y **Behave**. A continuación, se describe cómo instalar las dependencias, activar el entorno virtual, ejecutar las pruebas y entender la estructura principal del repositorio.

---

## 📍 1. Resolución de dependencias

### 🔹 Activar entorno virtual
- **Windows**:
  ```cmd
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 🔹 Instalar los requerimientos
```bash/cmd
pip install -r requirements.txt
```

---

## 📁 2. Estructura del proyecto
A continuación, se presenta la estructura principal de carpetas y archivos:

```
📂 PRIMERA_PRUEBA
│── 📂 features                # Contiene los archivos de pruebas
│   ├── 📂 features_files       # Archivos .feature
│   │   ├── 📄 prueba_alten.feature 📝 (Escenario de búsqueda de ofertas)
│   ├── 📂 steps                # Define la lógica BDD y pasos
│   │   ├── 📄 prueba_alten_steps.py
│   └── 📄 environment.py        # Configuraciones globales (Behave, WebDriver, capturas, reportes)
│
│── 📂 capturas                # Almacena las capturas de pantalla generadas tras cada paso
│
│── 📂 reportes                # Contiene el archivo de log de ejecución (test_execution.log)
│
│── 📂 utils                   # Carpeta de utilidades
│   ├── 📄 locators.py          # Lógica para localizar elementos en la página
│   ├── 📄 helpers.py           # Funciones de ayuda (esperas explícitas)
│   ├── 📄 assertions.py        # Validaciones personalizadas
│   └── 📄 actions.py           # Acciones genéricas sobre elementos
│
│── 📂 pages                   # Contiene la clase base y páginas específicas
│   ├── 📄 page.py              # Clase base con locators, helpers, assertions y actions
│   ├── 📂 alten_home
│   │   └── 📄 prueba_alten_page.py  # Página específica para la feature de prueba_alten
│
│── 📄 requirements.txt        # Listado de dependencias del proyecto
│── 📄 .gitignore
│── 📄 README.md               # Archivo de documentación principal
│── 📂 venv                    # Carpeta generada del entorno virtual
│── 📄 settings.json, launch.json  # Configuraciones del editor o IDE
```

---

## 🚀 3. ¿Cómo ejecutar las pruebas?

Asegúrate de activar el entorno virtual antes de ejecutar las pruebas.
Desde la carpeta raíz (`PRIMERA_PRUEBA`), ejecuta en la terminal:

```bash/cmd
behave
```

Esto buscará los archivos `.feature` y ejecutará los pasos definidos en la carpeta `steps`.

---

## 📊 4. Reportes y capturas de pantalla

- **Capturas**: Después de cada paso de la ejecución, se genera una captura de pantalla en la carpeta `capturas`.
- **Logs de reporte**: En la carpeta `reportes` se almacena el archivo `test_execution.log`, con detalles de cada ejecución, indicando si los escenarios pasaron o fallaron.

---

## 🔍 5. Descripción de los módulos de utilidades

- **`locators.py`**: Métodos para localizar elementos en la página.
- **`helpers.py`**: Funciones auxiliares como esperas explícitas.
- **`assertions.py`**: Aserciones personalizadas para validaciones más detalladas.
- **`actions.py`**: Métodos de interacción con elementos (clic, scroll, etc.).

---

## 🏗 6. `page.py` (Archivo principal)

Define la clase base `Page`, que agrupa las funcionalidades de:

✅ **Locators** (Búsqueda de elementos)
✅ **Actions** (Interacciones comunes)
✅ **Assertions** (Validaciones)
✅ **Helpers** (Esperas y utilidades)

Todas las páginas específicas heredan de esta clase base para evitar repetición de código.

---

## 📝 7. `prueba_alten_page.py` (Página específica)

📍 Ubicada en `pages/alten_home/`, extiende la clase base `Page` y contiene métodos específicos para la funcionalidad de filtrado y validación de ofertas en la página de Alten.

### 🔹 Ejemplo de métodos:
- **`auto_search_first_job()`**: Selecciona un empleo aleatorio y usa su título como palabra clave de búsqueda.
- **`should_have_matching_jobs()`**: Verifica que las ofertas resultantes coincidan con la palabra clave ingresada.

---
## 8. Licencia

Este proyecto se distribuye bajo la licencia **MIT License**.  
Puedes usar, modificar y distribuir este código libremente, siempre y cuando se conserve la atribución original.  
Para más detalles, consulta el archivo `LICENSE` incluido en el repositorio.

---

## 9. Autor

👨‍💻 **Orel A. Roman Ramos**  
Desarrollador y QA Engineer apasionado por la automatización de pruebas y la mejora continua en la calidad del software.