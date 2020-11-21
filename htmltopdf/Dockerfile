FROM python:3.7-slim
RUN apt-get update
RUN apt-get --assume-yes install python-requests wkhtmltopdf
WORKDIR /app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]