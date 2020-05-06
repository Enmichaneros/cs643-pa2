# cs643-pa2

(Note: docker container is not fully functional by itself yet.)

Steps:
- obtain EC2 keypair
- install flintrock `sudo apt-get install flintrock`
- execute `./run.sh` to copy files and set up EC2 cluster
- login to cluster with `flintrock login pa2`
- execute `./spark/bin/spark-submit --master [MASTER_URL] ./train.py` using the url given. This trains the model and evaluates it on the validation dataset 
- Note: you can replace the existing validation set with the new one using `flintrock copy-file pa2 [path_to_new_dataset] /home/ec2-user`
- execute `./spark/bin/spark-submit --master [MASTER_URL] ./pa2.jar` (Would use the code in /scala to load the best model and run it on the validation dataset)
