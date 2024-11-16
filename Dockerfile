FROM python:3.9-slim

RUN mkdir /home/ubuntu/app

WORKDIR /home/ubuntu/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "task_api.py"]