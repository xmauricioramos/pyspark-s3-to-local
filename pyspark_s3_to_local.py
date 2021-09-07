from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder\
	.config("spark.hadoop.fs.s3a.access.key", '<accesskey>')\
	.config("spark.hadoop.fs.s3a.secret.key", '<secretkey>')\
	.config("spark.hadoop.fs.s3a.session.token", '<token>')\
	.config("spark.hadoop.fs.s3a.aws.credentials.provider", 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider')\
	.getOrCreate()

sc = spark.sparkContext

# check Hadoop version
# print(f"Hadoop version = {sc._jvm.org.apache.hadoop.util.VersionInfo.getVersion()}")

df = spark.read.csv("s3a://<path>/", header=True)
df.printSchema()
df.show(truncate=False)
df.repartition(1).write.parquet("C:\\<path>", mode="overwrite")