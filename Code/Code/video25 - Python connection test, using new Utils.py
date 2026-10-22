from neptune_python_utils.gremlin_utils import GremlinUtils
from neptune_python_utils.endpoints import Endpoints

# Gremlin init
GremlinUtils.init_statics(globals())

# Change to your cluster name
endpoints = Endpoints(neptune_endpoint='airline-stats-database-1.cluster-czsv9mt1neer.eu-west-1.neptune.amazonaws.com')
gremlin_utils = GremlinUtils(endpoints)

# Open connection and graph
conn = gremlin_utils.remote_connection()
g = gremlin_utils.traversal_source(connection=conn)

# Print a random value, to test connectivity
my_list = g.V().limit(1).valueMap().toList()
print(my_list)

# Close connection
conn.close()
