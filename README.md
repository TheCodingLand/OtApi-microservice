# OtApi-microservice 

This project aims to provide a microservice style RestFul api to an enterprise product called omnitracker, from the company
Omninet.

The goal is to spawn several web service APIs behind a load balancer, and a message queue.

## CONFIG :

Edit Docker-compose.yml to add your omnitracker server host name.
Adapt ot_models.py file to your environment.

## RUNNING :
`docker-compose up -d`
 
 Web services should be available on port 5001.
 Swagger api doc ui on port 5100.
 
 
