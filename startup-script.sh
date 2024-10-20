#!/bin/bash

# [START startup_script]

echo "Started executing startup_script"
sudo apt-get update
sudo apt-get install -y python3 python3-pip protobuf-compiler
pip3 install google-cloud-storage grpcio grpcio_tools
pip3 install grpc_tools
python3 -m pip install --user grpcio-tools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
pip3 install flask
pip3 install jsonpickle
pip3 install seaborn

echo "Create directory"

git clone https://github.com/prajaktakini/datacenter-scale-computing-lab6.git
cd datacenter-scale-computing-lab6