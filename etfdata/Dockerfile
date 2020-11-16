FROM python:3.7-slim
RUN apt-get update
RUN apt-get --assume-yes install python-requests
#--------------------------------------------------
# GitHub Action ignores WORKDIR, ENTRYPOINT and CMD
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "etfdata.py" ]