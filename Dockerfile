FROM python:3.11.14-slim-bookworm

WORKDIR /home/webserver

COPY index.html python_webserver.py .
 
EXPOSE 8000

CMD ["python3", "python_webserver.py"]
