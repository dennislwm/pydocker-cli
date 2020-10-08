FROM python:3.7-slim
RUN apt-get update
RUN apt-get --assume-yes install python-requests wkhtmltopdf
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY app.py /app/
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]