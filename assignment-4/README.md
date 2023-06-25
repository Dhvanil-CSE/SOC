# Running the cloud server:<br>
### First you need to create the required volume.<br>
``` 
docker volume create factors-db 
```
### Then to create an image of the server use:<br>
```
docker docker build -t gs .
```
### Finally run the cloud server by running the docker container with following command:<br>
```
docker run -p 127.0.0.1:3000:3000 --mount type=volume,src=factors-db,target=/fdata/ --mount type=bind,src=/tmp/data,target=/app/qdata gs
```

# For data server, use the following command:<br>
```
python3 data_server.py
```

# For client server, use the following command:<br>
```
python3 echo_client.py
```
