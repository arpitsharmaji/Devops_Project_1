FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

Workdir /app

Copy . /app

RUN pip3 install flask 

EXPOSE 5000

CMD ["python3","app.py"]
