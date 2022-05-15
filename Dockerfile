FROM python:latest

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 3000

CMD ["python3", "exporter.py"]