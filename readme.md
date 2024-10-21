# Documentación del Proyecto de Envío de Correos con Google Sheets

## Introducción

Este proyecto tiene como objetivo enviar correos electrónicos a partir de datos extraídos de una hoja de cálculo de Google Sheets. Utiliza Python y varias bibliotecas para gestionar la autenticación y el envío de correos.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

-   Python 3.6 o superior
-   pip (el administrador de paquetes de Python)

## Instalación de Bibliotecas

Para instalar las bibliotecas necesarias, ejecuta el siguiente comando en tu terminal:

```bash
pip install gspread oauth2client python-dotenv
```

# Bibliotecas utilizadas:

## gspread:

Para interactuar con Google Sheets.

## oauth2client:

Para la autenticación con Google API.

## python-dotenv:

Para cargar variables de entorno desde un archivo .env.

# Configuración de Google Sheets

Para configurar Google Sheets y permitir que tu script acceda a tus hojas de cálculo, sigue estos pasos:

## Paso 1: Crear un Proyecto en Google Cloud Console

Ve a Google Cloud Console.
Crea un nuevo proyecto.
Una vez creado, haz clic en el menú de navegación (las tres líneas en la esquina superior izquierda) y selecciona "API y servicios" > "Biblioteca".

## Paso 2: Habilitar la API de Google Sheets

Busca "Google Sheets API" en la biblioteca de APIs.
Haz clic en "Habilitar".

## Paso 3: Habilitar la API de Google Drive

Busca "Google Drive API" en la biblioteca de APIs.
Haz clic en "Habilitar".

## Paso 4: Crear Credenciales

Ve a "API y servicios" > "Credenciales".
Haz clic en "Crear credenciales" y selecciona "Cuenta de servicio".
Proporciona un nombre para la cuenta de servicio y haz clic en "Crear".
En el paso siguiente, selecciona "Editor" como rol y haz clic en "Continuar".
Haz clic en "Listo".
Haz clic en el nombre de la cuenta de servicio que acabas de crear y luego en "Agregar clave" > "JSON". Esto descargará un archivo JSON con tus credenciales.

## Paso 5: Compartir la Hoja de Cálculo

Abre tu hoja de cálculo de Google Sheets.
Haz clic en "Compartir" y comparte la hoja con el correo electrónico de tu cuenta de servicio (esto está en el archivo JSON que descargaste, en el campo client_email).

# Crear el Archivo .env

Crea un archivo llamado credenciales.env en el mismo directorio que tu script y agrega las siguientes variables:

plaintext
Copiar código

GOOGLE_SHEETS_CREDS=path/to/your/credentials.json
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit
EMAIL_ORIGEN=your_email@example.com
EMAIL_PASSWORD=your_email_password
Reemplaza path/to/your/credentials.json con la ruta a tu archivo JSON, YOUR_SPREADSHEET_ID con el ID de tu hoja de cálculo, y proporciona tu correo electrónico y contraseña.

Nota: Para una mayor seguridad, considera utilizar una contraseña de aplicación si tu cuenta de Google tiene habilitada la verificación en dos pasos.

# Ejecución del Script

Una vez que hayas configurado todo, puedes ejecutar el script de la siguiente manera:

## bash

Copiar código
python script_main.py

## Descripción del Script

El script se conecta a Google Sheets y recupera datos para enviar correos electrónicos. Aquí hay un desglose de lo que hace:

Carga de Variables de Entorno: Utiliza python-dotenv para cargar credenciales y configuraciones desde el archivo .env.
Autenticación con Google Sheets: Utiliza gspread y oauth2client para autenticarse y acceder a Google Sheets.
Conexión SMTP: Se conecta al servidor SMTP de Gmail para enviar correos electrónicos.
Envío de Correos: Recorre los datos de la hoja de cálculo y envía correos a las direcciones especificadas, actualizando el estado de envío en la hoja.
Manejo de Errores: Implementa manejo de errores para situaciones comunes como la autenticación fallida y datos faltantes.
Contribuciones
Si deseas contribuir al proyecto, siéntete libre de hacer un fork del repositorio, realizar tus cambios y enviar un pull request.
