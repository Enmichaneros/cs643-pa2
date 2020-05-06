#!/usr/bin/env python3

from pyspark.ml.feature import RFormula
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)
# Create DataFrame from .csv file
# we could make a training and testing set, but we already have it split
train = spark.read.load("TrainingDataset.csv", format="csv", sep=";", inferSchema="true", header="true")
validate = spark.read.load("ValidationDataset.csv", format="csv", sep=";", inferSchema="true", header="true")

# define the rFormula stage
rform = RFormula(formula="quality ~ .")

# define the LogisticRegression stage
lr = LogisticRegression(family="multinomial").setLabelCol("quality").setFeaturesCol("features")

# define the pipeline and set the stages
stages = [rform, lr]
pipeline = Pipeline().setStages(stages)

# create the ParamGrid in order to choose the best model after trying different hyperparameters
params = ParamGridBuilder()\
		.addGrid(lr.standardization, [True, False])\
		.addGrid(lr.elasticNetParam, [0.1, 0.5, 0.75, 1.0])\
		.addGrid(lr.regParam, [0, 1, 5, 10, 20]).build()

# define the Evaluator (multiclass, since wines are rated between 1-10)
evaluator = MulticlassClassificationEvaluator()

# build a CrossValidator using the above configuration options to select the best performing model
crossval = CrossValidator(estimator=pipeline, estimatorParamMaps=params, evaluator=MulticlassClassificationEvaluator(), numFolds=2)

# fit the model, allowing the CrossValidator to choose the best performing model out of the set
cvModel = crossval.fit(train)

result = evaluator.evaluate(cvModel.transform(validate))

# save the model to a temporary location, to be loaded by the prediction program

bestModel = cvModel.bestModel
bestModel.write().overwrite().save("./model")

print("==========================")
print("==========================")
print("==========================")
print("Finished running, model saved.")
print(result)
print("==========================")
print("==========================")
print("==========================")