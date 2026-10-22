# Graph Database Modelling using AWS Neptune and Gremlin

Graph Database Modelling using AWS Neptune and Gremlin — AWS Data Engineering project.

## Overview
Instead of utilizing rows and columns in tables, graph data modeling allows users to define an arbitrary domain as a linked graph of nodes and relationships with properties and labels. Graph representation of data has several advantages over relational databases. A graph database may be searched by edge type or by traversing the complete graph. Because the associations between nodes are not computed at query time but are stored in the database, traversing the joins or relationships in graph databases is relatively fast. Graph databases are useful for use cases like social networking, recommendation engines, and fraud detection when you need to construct linkages between data and query these associations with minimum processing time. In this project, the requirement from our customer (simulated), an Airport Operator, is to have an analytics platform using Graph Modelling to answer questions like:

## Data
The Bureau of Transportation Statistics of the United States Department of Transportation monitors the on-time performance of domestic flights operated by big airlines. The databases include daily airline data such as flight details, origin and destination, carrier company, delay time, and generic delay explanation.

_Data is not included in this repository._

## Tech stack
➔ Languages-
- SQL, Python3, Gremlin ➔ Services -
- AWS S3, AWS Glue, AWS Athena, AWS IAM, Amazon Neptune, AWS Cloud9, AWS EC2, Apache Spark

Amazon S3 Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance. Users may save and retrieve any quantity of data using Amazon S3 at any time and from any location.

## How to run
Notebooks: [`video16 - Jupyter Notebook 1 - Data Engineering Lab 1.ipynb`](Code/Code/video16%20-%20Jupyter%20Notebook%201%20-%20Data%20Engineering%20Lab%201.ipynb), [`video31 - Jupyter Notebook - Neptune Data Querying and Visualization Lab 1.ipynb`](Code/Code/video31%20-%20Jupyter%20Notebook%20-%20Neptune%20Data%20Querying%20and%20Visualization%20Lab%201.ipynb)

## Project structure
```
.gitignore
Code/
  Code/
    Fixed Spark Glue Job.py
    video13.sh
    video16 - Jupyter Notebook 1 - Data Engineering Lab 1.ipynb
    video21 - Glue Job - us-bts-flight-stats-spark-job-extract-edges-nodes-for-neptune.py
    video24 - Python connection test and Libs installation.py
    video25 - Install Neptune Python Utils steps.sh
    video25 - Python connection test, using new Utils.py
    video27 - Count Script gremlin-count-nodes-edges-lab.py
    video27 - gremlin-load-bulk.py
    video27 - print top 10 vertices gremlin-random-queries.py
    video30 - Count Script gremlin-count-nodes-edges-lab.py
    video30 - gremlin-delete-all-data.py
    video31 - Jupyter Notebook - Neptune Data Querying and Visualization Lab 1.ipynb
  Terraform/
    Instructions.md
README.md
```

## Credits
Based on a ProjectPro guided project.
