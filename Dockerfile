FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY app.py .
ENV PYTHONUNBUFFERED=1
CMD ["python", "-u", "app.py"]