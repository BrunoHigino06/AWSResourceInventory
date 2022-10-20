import os

def Resource_Inventory():
    ec2 = True
    rds = False

    if ec2 == True and rds == False:
        os.system("aws configservice select-aggregate-resource-config --expression \"SELECT resourceId,resourceName,configuration.privateIpAddress,resourceType,configuration.instanceType,tags,availabilityZone,configuration.state.name,accountId WHERE resourceType='AWS::EC2::Instance' --configuration-aggregator-name test_agregator --output json > report_json.json\"")

    if ec2 == False and rds == True:
        os.system("aws configservice select-aggregate-resource-config --expression \"SELECT resourceId,resourceName,configuration.privateIpAddress,resourceType,configuration.instanceType,tags,availabilityZone,configuration.state.name,accountId WHERE resourceType='AWS::RDS::DBInstance' --configuration-aggregator-name test_agregator --output json > report_json.json\"")
    
    if ec2 == True and rds == True:
        os.system("aws configservice select-aggregate-resource-config --expression \"SELECT resourceId,resourceName,configuration.privateIpAddress,resourceType,configuration.instanceType,tags,availabilityZone,configuration.state.name,accountId WHERE resourceType='AWS::RDS::DBInstance' OR resourceType='AWS::EC2::Instance' --configuration-aggregator-name test_agregator --output json > report_json.json\"")


Resource_Inventory()