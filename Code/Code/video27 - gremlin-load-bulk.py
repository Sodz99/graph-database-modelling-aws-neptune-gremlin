# Relevant notes:
#
#   - Code example to show how to read files in Amazon S3, to push data to Neptune in bulk.
#   - Functions, reusability, error handling and Logger still needs to be implemented.
#   - Values are hard-coded, since this code is meant to serve as initial code snippets only. 
##################################################################################################################################################################

from neptune_python_utils.bulkload import BulkLoad
from neptune_python_utils.gremlin_utils import GremlinUtils
from neptune_python_utils.endpoints import Endpoints
import time
import traceback

# Connection and Endpoint Definitions:
GremlinUtils.init_statics(globals())

endpoints = Endpoints(neptune_endpoint='YOUR-NEPTUNE-CLUSTER-ENDPOINT-HERE')
gremlin_utils = GremlinUtils(endpoints)

conn = gremlin_utils.remote_connection()
g = gremlin_utils.traversal_source(connection=conn)

# Vertices to load:
s3_graph_data_file = ['s3://ENTER_BUCKET_NAME_HERE/PATH_TO_VERTICES_OR_EDGES_file.csv']


# Bulk-loading
def neptune_loader(endpoint: object, files_to_load: object, iam_role: object) -> object:
    try:
        for file in files_to_load:
            # Bulk-loading
            bulkload = BulkLoad(
                endpoints=endpoints,
                role=iam_role,
                region='eu-west-1',
                source=file,
                update_single_cardinality_properties=True)
            load_status = bulkload.load_async()

            # Checking status:
            status, json = load_status.status(details=True, errors=True)
            print(json)
            load_status.wait()

    except Exception as e:
        print('Error raised: {}'.format(e))
        print(traceback.format_exc())


# Load data:
neptune_loader(
    endpoint=endpoints,
    files_to_load=s3_graph_data_file,
    iam_role='arn:aws:iam::12345678910:role/Neptune-role-with-s3-privileges-iamRole-10Q9LWHL17PPK'
)
