
from aws_cdk import (
    Stack
)
from constructs import Construct

from aws_cdk import aws_eks_v2_alpha as eks
from aws_cdk import aws_ec2 as ec2

class EksStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC with 1 NAT Gateway
        vpc = ec2.Vpc(self, "EksVpc",
            nat_gateways=1,  # This will create only 1 NAT Gateway
            max_azs=2  # Using 2 AZs for cost optimization while maintaining availability
        )
               
        cluster = eks.Cluster(self, 'hello-eks',
            version=eks.KubernetesVersion.V1_32,
            vpc=vpc
        )
