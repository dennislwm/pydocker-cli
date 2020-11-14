FROM selenium/standalone-chrome
USER root
RUN \ 
  apt-get update && \
  apt-get --assume-yes install python3-pip python-requests wget
# Install app
WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . ./
ENTRYPOINT [ "python3" ]
CMD ["app.py"]
