# pyspark-s3-to-local
Connect local Spark to s3 bucket on AWS

First of all, you need to check the Hadoop version installed, so you can install the correct .jars:
```
print(f"Hadoop version = {sc._jvm.org.apache.hadoop.util.VersionInfo.getVersion()}")
```
To access the files directly on AWS S3 it is necessary to add the following .jars in the PySpark installation folder (if PySpark was installed via 'pip install' *%PYTHON_HOME%\Python39\Lib\site-packages\pyspark\jars\\*):
- [**hadoop-aws-*.jar**](https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/) (*version must be the same as Hadoop*)
- [**aws-java-sdk-bundle-*.jar**](https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/) (*the version must be 'hadoop-aws' compatible; the compatible version can be found in the 'Compile Dependencies' section in [Maven Repository](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) for the desired version)*