FROM python:3.10-slim

WORKDIR /app

# Crear usuario no-root
RUN useradd -m appuser

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Asignar permisos al usuario no-root
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/ || exit 1

CMD ["python", "app.py"]
