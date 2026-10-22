# IMPORTANT: REMEMBER to CHANGE the cluster endpoint below, in the Python code

from __future__  import print_function  # Python 2/3 compatibility
from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

# Establish a graph traversal object, by calling the graph's traversal method
# - more at: www.kelvinlawrence.net/book/PracticalGremlin.html
graph = Graph()

remoteConn = DriverRemoteConnection('wss://CHANGE_HERE_TO_YOUR_NEPTUNE_CLUSTER_ENDPOINT:8182/gremlin','g')
g = graph.traversal().withRemote(remoteConn)

# IMPORTANT: this assumes you have already a "~label" column.

# All Vertices:
all_vertices = g.V().count().toList()
print(all_vertices)

# Vertices for some group:
vertices = g.V().groupCount().by('~label').toList()
print(vertices)

# Edges for some group:
edges  = g.E().groupCount().by('~label').toList()    
print(edges)

remoteConn.close()
