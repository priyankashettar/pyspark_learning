from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType

tableSchema= StructType([
    StructField('studentName',StringType(),True),
    StructField('studentDep',StringType(),True),
    StructField('studentMarks',IntegerType(),True),
])

tableData=[
    ('Priyanka','ECE',9),
    ('Somashekhar','EEE',10),
    ('Amar','ECE',8),
]

if __name__=='__main__':
    spark=SparkSession.builder.appName('pysparkdemo').getOrCreate()
    df=spark.createDataFrame(data=tableData, schema=tableSchema)
    df.printSchema()
    df.show()