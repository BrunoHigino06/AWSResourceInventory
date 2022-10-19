import os
import re

def Resource_Inventory():

    os.system('aws configservice select-aggregate-resource-config --expression "SELECT resourceId,configuration.privateIpAddress,resourceType,configuration.instanceType,tags,availabilityZone,configuration.state.name,accountId,Account Name WHERE resourceType="AWS::EC2::Instance"" --configuration-aggregator-name test_agregator')
