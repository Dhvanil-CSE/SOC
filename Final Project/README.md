## Final Project
### Abstract

In this Project, we propose a new secure k-NN query scheme on encrypted cloud data. Our approach
simultaneously achieves: <br>

(1) data privacy against CS: the encrypted database can resist potential attacks
of CS,<br>
(2) key confidentiality against QUs: to avoid the problems caused by key-sharing, QUs cannot learn
DO’s key,<br>
(3) query privacy against CS and DO: the privacy of query points is preserved as well, (4) query
controllability: QUs cannot launch a feasible k-NN query for any new point without approval of DO.

---
### Our Implementation:
This is a slightly restricted implementation of the [research paper](https://github.com/Dhvanil-CSE/SOC/blob/main/Final%20Project/research%20paper.pdf). It generates a random database consisting of 10000 datapoints each of dimension 50. Each dimension of datapoint has integer values in range [-10,10] . The database is stored in database.txt containing one point per line. The query user can only query 50-dimensional point (No partial dimension is allowed). The query passed by the query-user is first sent to the data-owner for approval. The data-owner can approve or reject the query by entering 1 or 0 respectively. If the data-owner approves, the cloud-server returns a list of k-NN of the query point ,where k=10, else the program exits.

---
### How to use our implementation:
#### Steps:
<pre>
(1) Pull this github folder on your device which has docker installed on it.<br>
(2) Open three tabs in terminal.<br>
(3) Run the files in the specified order and specified manner:<br> 
  (i) data_gen.py in any tab (NOTE : This program stores the database in a text file named database.txt (creates one if not present in folder).<br>
  Tab 1:<br>
    (ii) CS.py<br>
  Tab 2:<br>
    (iii) DO.py<br>
  Tab 3:<br>
    (iv) QU.py<br>
</pre>
Run data_gen.py using :
```
python3 data_gen.py
```

To run CS.py:<br>
<br>
First build the conatiner image from the Dockerfile
```
docker build -t app .
```
Start the docker container and map the port 9998 of device to the container's port 9998
```
docker run -p 0.0.0.0:9998:9998 app
```
Now your cloud-server (CS) is online
![CS](https://github.com/Dhvanil-CSE/SOC/blob/main/Final%20Project/misc/CS.png)

To run DO.py:<br>
```
python3 DO.py
```
![DO](https://github.com/Dhvanil-CSE/SOC/blob/main/Final%20Project/misc/DO.png)

To run QU.py:<br>
```
python3 QU.py
```
Enter your query point with value of each dimension separated by a space.
![QU](https://github.com/Dhvanil-CSE/SOC/blob/main/Final%20Project/misc/QU.png)

