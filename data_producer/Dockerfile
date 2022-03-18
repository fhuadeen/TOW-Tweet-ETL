FROM python:3.9-alpine

# make directory in the container
# RUN chmod 0777 /usr
# RUN mkdir /src

# set working directory
WORKDIR /src

RUN pip install --upgrade pip
# RUN pip install apache-airflow==2.1.4 \
#     --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.1.4/constraints-3.7.txt"
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

# Copy source code into the container
COPY ./src/ /src/

CMD ["python", "app.py"]

