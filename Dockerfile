
FROM bitnami/spark:3.5

USER root

RUN apt-get update && apt-get install -y wget curl unzip && rm -rf /var/lib/apt/lists/*

ENV HADOOP_VERSION=3.3.6
RUN mkdir -p /opt/bitnami/spark/jars && \
    wget -P /opt/bitnami/spark/jars/ \
      https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar && \
    wget -P /opt/bitnami/spark/jars/ \
      https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

ENV SPARK_EXTRA_CLASSPATH="/opt/bitnami/spark/jars/*"

WORKDIR /opt/bitnami/spark

