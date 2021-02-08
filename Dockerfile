FROM python:3.7-slim

EXPOSE 8000

ADD . /django_project

WORKDIR /django_project

RUN pip3 install -r requirements.txt

RUN python ImagesAndFilesUpload_Project/manage.py makemigrations

RUN python ImagesAndFilesUpload_Project/manage.py migrate

CMD [ "python", "ImagesAndFilesUpload_Project/manage.py", "runserver", "0.0.0.0:8000" ]

