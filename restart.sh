#!/bin/bash

sudo docker stop push-server
sudo docker rm push-server
sudo docker rmi push-server
sudo docker image build -t push-server .
sudo docker run --name=push-server --network=host -d push-server