"""
*) In PyCharm, Cloud9 or other IDE environment, install dependencies, via the Project settings or PIP local:
	- boto3
	- gremlinpython
	- requests
	- backoff
	
	e.g.
		1. Create directory, like gremlin-lab-1
		2. Run the following command in the terminal, within the new directory:
		
		   pip3 install boto3 gremlinpython requests backoff -t .

*) Python script below, to test connectivity. 

"""

# IMPORTANT: REMEMBER to CHANGE the cluster endpoint below, in the Python code

from __future__ import print_function  # Python 2/3 compatibility
from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

# Establish a graph traversal object, by calling the graph's traversal method
# - more at: www.kelvinlawrence.net/book/PracticalGremlin.html
graph = Graph()
remoteConn = DriverRemoteConnection(
    'wss://airline-stats-database-1.cluster-czsv9mt1neer.eu-west-1.neptune.amazonaws.com:8182/gremlin', 'g')
g = graph.traversal().withRemote(remoteConn)

# Print some random pre-existing Vertices in the DB.
print(g.V().limit(2).toList())
remoteConn.close()
