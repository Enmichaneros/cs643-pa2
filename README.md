# cs643-pa2

(Note: docker container is not fully functional by itself yet.)

Steps:
- obtain EC2 keypair
- install flintrock `sudo apt-get install flintrock`
- execute `./run.sh` to copy files and set up EC2 cluster
- login to cluster with `flintrock login pa2`
- execute `./spark/bin/spark-submit --master [MASTER_URL] ./train.py` using the url given. this trains the model and validates it
- execute `./spark/bin/spark-submit --master [MASTER_URL] ./pa2.jar`
