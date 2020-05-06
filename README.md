# cs643-pa2

(Note: docker container is not fully functional by itself yet.)

Steps:
- obtain EC2 keypair
- install flintrock `sudo apt-get install flintrock`
- obtain TrainingDataset.csv and ValidationDataset.csv and place in current directory. Edit headers to not use extraneous quotes (e.g. "quality" instead of """"quality""""")
- execute `./run.sh` to copy files and set up EC2 cluster
- login to cluster with `flintrock login pa2`
- execute `./spark/bin/spark-submit --master [MASTER_URL] ./train.py` using the url given. This trains the model and evaluates it on the validation dataset 
- execute `./spark/bin/spark-submit --master [MASTER_URL] ./pa2.jar` (Would use the code in /scala to load the best model and run it on the validation dataset)
