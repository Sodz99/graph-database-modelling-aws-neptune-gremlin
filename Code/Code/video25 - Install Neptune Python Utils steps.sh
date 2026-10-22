######################################################################################################
# Section 1:
######################################################################################################

mkdir neptune-utils-source
cd neptune-utils-source

# *) Clone the Neptune Utils, by AWS

 	 git clone https://github.com/awslabs/amazon-neptune-tools.git

#    Instructions:
 	 cd amazon-neptune-tools/neptune-python-utils

# 	 - edit the build.sh file, if necessary. For example, this script calls python executable 3.8.
# 		 -> in this case, I replaced 3.8 by 3.7, in the following strings:
# 			
# 				virtualenv temp --python=python3.7
# 				cd lib/python3.7/site-packages
# 	
# 	- run the build.sh, as in the instructions at https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils
 	  sh build.sh 
# 		This will compile and create a new directory called "neptune-python-utils"
# 	- cd neptune-app and copy the newly "neptune-python-utils" directory here.
# 		(this directory will have the gremlin_python binaries, including the tornado packages)


######################################################################################################
# Section 2:
######################################################################################################

mkdir gremlin-lab-1
cd gremlin-lab-1
pip3 install boto3 -t .
pip3 install gremlinpython -t .
# Copy the new directory neptune_python_utils (generated above) here:
cp -r ~/environment/neptune-utils-source/amazon-neptune-tools/neptune-python-utils/neptune_python_utils .
