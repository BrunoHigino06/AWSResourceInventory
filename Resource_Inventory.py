import os
import re

def Resource_Inventory():

    os.system('aws configservice select-aggregate-resource-config --expression "SELECT resourceId WHERE resourceType="AWS::EC2::Instance"" --configuration-aggregator-name test_agregator')

    return