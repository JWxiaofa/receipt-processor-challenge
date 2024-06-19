FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]