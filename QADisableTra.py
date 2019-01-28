import boto3  
import botocore  
#import datetime  
#import re  
#import logging
#import time
import argparse

REGION = 'us-east-1'
source = boto3.client('opsworks', region_name=REGION)
source1 = boto3.client('ec2', region_name=REGION)
source2 = boto3.client('rds', region_name=REGION)
Group=['sg-02f3d40e9527b4cb0']
#Instance='i-07d2a2d912bffe3e3'

  

def DisableZK():
      print ('disabled ZK')
      stack_parsed = source.describe_stacks()
      stack = stack_parsed['Stacks']
      i=0
      while(i<len(stack)):

      	   if (stack_parsed['Stacks'][i]['Name']== 'QAZookeeper'):
               stackID = stack_parsed['Stacks'][i]['StackId']
               print (stackID)
               i = len(stack)     
      i = i+1


      EC2instance_parsed = source.describe_instances(StackId=stackID)
      EC2instances = EC2instance_parsed['Instances']
      print (len(EC2instances))
      j=0
      Instances=[]
      
      while(j<len(EC2instances)):
      	   
      	   Instance = EC2instance_parsed['Instances'][j]['Ec2InstanceId']
      	   print (Instance)
      	   response = source1.modify_instance_attribute(InstanceId=Instance, Groups=Group)
           print(response)
      	   j=j+1
           



def DisableRDS():       
        print ('disabled RDS')
      RDS_parsed = source2.describe_db_instances()
      RDSinstances = RDS_parsed['DBInstances']
      #print (RDSinstances)
      print (len(RDSinstances))
      x=0
      rdsInstances=[]
      
      while(x<len(RDSinstances)):
      	   
      	   rdsInstance = (RDS_parsed['DBInstances'][x]['DBInstanceIdentifier'])
      	   if (rdsInstance == 'lpi-data' or rdsInstance == 'lpi-encrypted' or rdsInstance== 'dd1a2q8s6mpoe0w'):
      	   	   print ((RDS_parsed['DBInstances'][x]['VpcSecurityGroups']))
      	   	   #response = source2.modify_db_instance(DBInstanceIdentifier=rdsInstance, VpcSecurityGroupIds=Group)
      	   x=x+1
       
           
      print (len(rdsInstances))



def parser():
    
    parser = argparse.ArgumentParser(description='Get Parameter')
    #commands = parser.add_subparsers(help="commands")
    parser.add_argument('--zk', default=False, action='store_true')
    parser.add_argument ('--rds', default=False, action='store_true')
    
    args = parser.parse_args()
    #subparser = commands.add_parser("zk", description="Disable ZK Traffic")
    #subparser.set_defaults(func= DisbaleZK)
    if args.zk :
       DisableZK()
    else :
       print ("Please select zk true , if you want to diable zk. Otherwise, zk won't be disbaled") 

    if args.rds:
       DisableRDS()
    else: 
       print ("Please select rds true , if you want to diable rds. Otherwise, rds won't be disbaled") 

     
if __name__ == '__main__':
       parser()
       
   
