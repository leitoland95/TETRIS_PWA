FROM python:3.9-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Ejecuta el comando
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]