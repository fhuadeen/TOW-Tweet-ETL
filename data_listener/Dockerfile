FROM python:3.9-alpine

# make directory in the container
RUN mkdir /src

# set working directory
WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

# Copy source code into the container
COPY ./src/ /src/

CMD ["python", "app.py"]