#Script for pyspark streaming example
#Assuming we have a kafka topic with name doit
#command to enter pyspark with appropriate kafka packages (kafka version 0.10, scala version 2.12, spark version 3.1.3)

#pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3

#spark will be available for use
from pyspark.sql.functions import explode, split

#read the stream
lines = spark.readStream.format("kafka").option("subscribe", "doit").option("kafka.bootstrap.servers", "localhost:9092").load()
#split the incoming text stream and create a spark sql data frame with a column called word
words = lines.select(explode(split(lines.value, " ")).alias("word"))
#count the words
wordCounts = words.groupBy("word").count()
#create a query.  As we have .start() on the end, when this line is submitted the query will listen for input.  
#Output is set to be 
query = wordCounts.writeStream.outputMode("complete").format("console").start()