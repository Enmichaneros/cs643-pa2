import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.classification.LogisticRegressionModel
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator


object pa2{
	def main(args: Array[String]) {

	println("==========================")
	println("Starting Program:")
	println("==========================")
		
	val spark = SparkSession.builder.appName("pa2").getOrCreate()

	println("==========================")
	println("Loading model:")
	println("==========================")


	val model = LogisticRegressionModel.load("./model")


	println("==========================")
	println("Reading Data:")
	println("==========================")

	val validate = spark.read.format("csv")
	  .option("sep", ";")
	  .option("inferSchema", "true")
	  .option("header", "true")
	  .load("ValidationDataset.csv")

	val evaluator = new MulticlassClassificationEvaluator()

	println("==========================")
	println("Running Model:")
	println("==========================")

	val result = evaluator.evaluate(model.transform(validate))

	println("==========================")
	println("Accuracy of model:")
	println(result)
	println("==========================")
	spark.stop()
	}
}