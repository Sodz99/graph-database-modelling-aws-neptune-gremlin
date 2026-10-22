# IMPORTANT: REMEMBER to CHANGE the cluster endpoint below, in the Python code
from __future__  import print_function  # Python 2/3 compatibility
from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import json
import ast

# Establish a graph traversal object, by calling the graph's traversal method
# - more at: www.kelvinlawrence.net/book/PracticalGremlin.html
graph = Graph()

remoteConn = DriverRemoteConnection('wss://CHANGE_HERE_TO_YOUR_NEPTUNE_CLUSTER_ENDPOINT:8182/gremlin','g')
g = graph.traversal().withRemote(remoteConn)

# Random query:
query_1 = g.V().hasLabel('airport').valueMap().limit(10).toList()
print(json.dumps(query_1, indent=4))

# Close connection:
remoteConn.close()
