FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /hanger/container

RUN pip3 install --upgrade pip 
COPY requirements.txt .
RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]