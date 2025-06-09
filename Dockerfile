# Imagen base oficial de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /usr/src/app

# Copiar archivos necesarios
COPY requirements.txt ./
COPY appsettings.json ./
COPY run.py ./
COPY app ./app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Comando de arranque
CMD ["python", "run.py"]
