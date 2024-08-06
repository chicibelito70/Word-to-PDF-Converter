```markdown
# Word to PDF Converter

## Descripción

Este proyecto es una herramienta para convertir documentos de Microsoft Word (`.docx`) a formato PDF. La aplicación proporciona una interfaz gráfica simple usando `tkinter` para seleccionar archivos de Word y convertirlos a PDF. También permite arrastrar y soltar archivos directamente en la ventana de la aplicación.

## Funcionalidades

- **Selección de archivos**: Puedes seleccionar archivos `.docx` usando un botón de "Browse" o arrastrándolos y soltándolos en la ventana de la aplicación.
- **Conversión a PDF**: Convierte archivos de Word seleccionados a PDF.
- **Interfaz gráfica**: La interfaz es creada con `tkinter` y permite una experiencia de usuario intuitiva.

## Instalación

1. **Clonar el repositorio** (si está disponible en un repositorio en línea):

   ```sh
   git clone https://github.com/chicibelito70/Word-to-PDF-Converter
   ```

2. **Instalar dependencias**:

   Asegúrate de tener `python-docx` y `reportlab` instalados. Puedes instalar estas bibliotecas usando pip:

   ```sh
   pip install python-docx reportlab tkinterdnd2
   ```

3. **Ejecutar la aplicación**:

   Navega a la carpeta del proyecto y ejecuta el archivo principal:

   ```sh
   python main.py
   ```

## Uso

1. **Abrir la aplicación**: Ejecuta el script `main.py` para abrir la ventana de la aplicación.
2. **Seleccionar archivos**:
   - **Usar botón "Browse"**: Haz clic en el botón "Browse" para seleccionar un archivo `.docx` desde tu sistema.
   - **Arrastrar y soltar**: Arrastra archivos `.docx` desde tu explorador de archivos y suéltalos en la ventana de la aplicación.
3. **Convertir a PDF**:
   - Después de seleccionar uno o más archivos, haz clic en el botón "Convert to PDF".
   - Se abrirá un cuadro de diálogo para elegir la ubicación y el nombre del archivo PDF resultante.
   - La conversión se realizará y se mostrará un mensaje de éxito con el nombre del archivo PDF.

## Requisitos

- Python 3.x
- Bibliotecas Python: `python-docx`, `reportlab`, `tkinterdnd2`

## Problemas Conocidos

- Si `tkinterdnd2` no está instalado correctamente o no funciona, la funcionalidad de arrastrar y soltar puede no estar disponible. En tal caso, usa el botón "Browse" para seleccionar archivos.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias, mejoras o encuentras algún error, por favor crea un issue o un pull request en el repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o soporte, puedes contactar a [tu nombre o dirección de correo electrónico].

```

### Cómo utilizar este `README.md`:

1. **Clona el Repositorio**: Si estás alojando el proyecto en un repositorio, asegúrate de actualizar la URL del repositorio.
2. **Archivos y Nombres**: Ajusta los nombres de los archivos y carpetas si tu proyecto tiene una estructura diferente.
3. **Información de Contacto**: Añade tu información de contacto o la de tu equipo si deseas que los usuarios puedan ponerse en contacto contigo.

Este `README.md` proporciona una descripción clara del proyecto, instrucciones de instalación y uso, y la información necesaria para contribuir.