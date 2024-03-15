FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD [ "python3", "main.py"]