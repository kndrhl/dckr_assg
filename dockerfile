FROM python:alpine
WORKDIR /home/data
COPY ./ ./
CMD ["python" ,"assg_script.py"]
