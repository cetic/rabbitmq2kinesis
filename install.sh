#/bin/bash

yum install -y git
yum install -y python-pip
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --enable docker-ce-edge
yum makecache fast
yum install -y docker
pip install docker-compose