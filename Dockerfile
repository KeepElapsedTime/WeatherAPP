FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 3333
COPY app.py .
ENV AUTHORIZATION=your-token-here
CMD ["python", "-u", "app.py"]