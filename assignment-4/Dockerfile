FROM ubuntu
WORKDIR .
COPY . .
RUN mkdir qdata
RUN mkdir fdata
RUN apt update
RUN apt install python3 -y
CMD ["python3","cloud_server.py"]
EXPOSE 3000
