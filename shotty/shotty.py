import boto3
import click
#import sys
session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    # "List of Bhupendra EC2 Instances"
    for i in ec2.instances.all():
        print(','.join((
		i.id,
		i.instance_type,
		i.placement['AvailabilityZone'],
		i.state['Name'],
		i.public_dns_name)))
    return	

if __name__ == '__main__':
    #print(sys.argv)
    list_instances()
