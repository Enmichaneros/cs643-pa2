FROM ubuntu:18.04
WORKDIR /
COPY . .
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN pip install flintrock
ENTRYPOINT /bin/bash
