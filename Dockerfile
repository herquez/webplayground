# pull the official base image
FROM python:3.10.12

# set work directory
WORKDIR /root

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /root
RUN pip install -r requirements.txt

# copy project
COPY . /root

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]