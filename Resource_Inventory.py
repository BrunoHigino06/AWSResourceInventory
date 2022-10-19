import os
import re

def Resource_Inventory():

    os.system('aws configservice select-resource-config --expression "SELECT resourceId WHERE resourceType="AWS::EC2::Instance"" --configuration-aggregator-name ')

    return