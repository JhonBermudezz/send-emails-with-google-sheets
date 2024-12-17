import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

logging.basicConfig(level=logging.INFO)

# Cargar las variables de entorno desde el archivo .env
load_dotenv('credenciales.env')  

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_file = os.getenv('GOOGLE_SHEETS_CREDS')
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

# Acceder a la hoja de cálculo
spreadsheet = client.open_by_url(os.getenv('SPREADSHEET_URL'))
worksheet = spreadsheet.sheet1 

# Obtener los datos de la hoja
datos = worksheet.get_all_records()

# Configuración del correo electrónico
email_origen = os.getenv('EMAIL_ORIGEN')
password = os.getenv('EMAIL_PASSWORD')

# Conectar al servidor SMTP de Gmail
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()  
    try:
        server.login(email_origen, password)
    except smtplib.SMTPAuthenticationError:
        logging.error("No se pudo autenticar con el servidor SMTP. Verifica tus credenciales.")
        exit(1)

    # Verificar y agregar columna de estado
    header_row = worksheet.row_values(1)
    if 'Estado' not in header_row:
        worksheet.update_cell(1, len(header_row) + 1, 'Estado') 
        header_row.append('Estado')

    estado_col_idx = header_row.index('Estado') + 1  

    # Enviar correos electrónicos
    for i, fila in enumerate(datos, start=2): 
        estado = fila.get('Estado', '')
        
        if estado != 'Enviado':
            email_destino = fila.get('Email')
            
            # Validar campos
            if not email_destino:
                logging.warning(f"Fila {i}: Falta información necesaria. Correo no enviado.")
                continue
    
            asunto = "Asunto"
            cuerpo = f"Cuerpo del correo"
            
            mensaje = MIMEMultipart()
            mensaje['From'] = email_origen
            mensaje['To'] = email_destino
            mensaje['Subject'] = asunto
            
            mensaje.attach(MIMEText(cuerpo, 'plain'))
            
            server.send_message(mensaje)
            
            logging.info(f"Correo enviado a {email_destino}")
            
            worksheet.update_cell(i, estado_col_idx, 'Enviado')

print('Todos los correos fueron enviados con éxito, y los estados actualizados.')
