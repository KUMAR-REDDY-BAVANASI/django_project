

# Django Project

This repository contains the code for this (deploying-django-applications-to-aws-ec2-with-docker/).

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [Docker](https://www.docker.com/products/docker-desktop)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/KUMAR-REDDY-BAVANASI/django_project.git
```

2. Check into the cloned repository
```
$ cd django_project
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

5. Start the Django API
```
$ python manage.py runserver
```

6. Navigate to `http://localhost:8000`

7. Build the Docker image:
```
$ docker build . -t django_project
```

8. Publish the Docker image to Dockerhub:
```
$ docker tag django_project <DOCKERHUB_USERNAME>/django_project
$ docker push <DOCKERHUB_USERNAME>/django_project
```

9. Deploy on AWS EC2 as outlined in this (deploying-django-applications-to-aws-ec2-with-docker/)

