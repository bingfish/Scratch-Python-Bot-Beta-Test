import scratchclient
# imports os to get environment vars
import os
# gets scratchsession
from scratchclient import ScratchSession
print ("Loading... Current state: Connecting to scratch")
print ("Loading... Current state: Connecting to project")
project = 641985963 # insert project id here
session = ScratchSession(os.environ['USERNAME'], os.environ['PASSWORD'])
cloud = session.create_cloud_connection(641985963)
# do code
connection = session.create_cloud_connection(641985963) #To create a cloud connection (must be done first)
print ("Current state: Successfully connected!")
connection.set_cloud_variable("c", "1") #To set a cloud variable
cloudvar = connection.get_cloud_variable("c") 
print ("Current variable state: " , (cloudvar))
