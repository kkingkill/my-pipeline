import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_eks as eks
from aws_cdk import aws_ec2 as ec2

class EksStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC
        vpc = ec2.Vpc(self, "EksVpc", max_azs=2)

        # Create EKS Cluster
        cluster = eks.Cluster(self, "EksCluster",
            version=eks.KubernetesVersion.V1_31,
            vpc=vpc,
            default_capacity=1,  # Number of nodes
            default_capacity_instance=ec2.InstanceType.of(
                ec2.InstanceClass.T3,
                ec2.InstanceSize.MEDIUM
            )
        )
