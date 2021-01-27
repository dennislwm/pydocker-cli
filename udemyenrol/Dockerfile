FROM selenium/standalone-chrome
USER root
RUN \ 
  apt-get update && \
  apt-get --assume-yes install python3-pip python3-requests wget
#--------------------------------------------------
# GitHub Action ignores WORKDIR, ENTRYPOINT and CMD
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "python3" ]
CMD ["app.py"]
