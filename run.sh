#!/bin/bash

# request AWS information to launch a cluster on
read -p 'Enter AWS key name: ' aws_key
read -p 'Enter path to AWS pem file: ' aws_file

echo "=================="
echo "Launching cluster...."
echo "=================="

# launch an EC2 cluster using flintrock
flintrock launch pa2 \
    --num-slaves 4 \
    --spark-version 2.4.5 \
    --ec2-key-name $aws_key \
    --ec2-identity-file $aws_file \
    --ec2-ami ami-00b882ac5193044e4 \
    --ec2-user ec2-user

# find the url of the master node and save it
master=$(flintrock describe --master-hostname-only pa2)
sparkmaster="spark://${master}:7077"

echo "=================="
echo "Copying files to cluster..."
echo "=================="

# copy the training dataset and the two scripts throughout the cluster
flintrock copy-file pa2 ./TrainingDataset.csv /home/ec2-user/TrainingDataset.csv
flintrock copy-file pa2 ./ValidationDataset.csv /home/ec2-user/ValidationDataset.csv
flintrock copy-file pa2 ./train.py /home/ec2-user/train.py
flintrock copy-file pa2 ./pa2.jar /home/ec2-user/pa2.jar

echo "=================="
echo "Installing dependencies to cluster..."
echo "=================="

flintrock run-command pa2 'sudo yum install -y python-pip'
flintrock run-command pa2 'pip install --user pyspark'
flintrock run-command pa2 'pip install --user numpy'


# submit python script to Spark to train model
echo "=================="
echo "Setup finished."
echo "To continue, run the following:"
echo "flintrock login pa2"
echo "After logging into cluster: ./spark/bin/spark-submit --master ${sparkmaster} ./train.py"
echo "After training model: ./spark/bin/spark-submit --master ${sparkmaster} ./pa2.jar"
echo "=================="



