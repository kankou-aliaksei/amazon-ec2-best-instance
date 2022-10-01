# Amazon EC2 Best Instance (amazon-ec2-best-instance)

Amazon EC2 Best Instance (amazon-ec2-best-instance) allows you to choose the most optimal and cheap EC2 instance type for your use.

# Prerequisites
* python3
* pip3
* boto3  
* AWS Account
* AWS Credentials

# Install
pip install amazon-ec2-best-instance

# Options

* **vcpu** Required. Describes the vCPU configurations for the instance type.
* **memory_gb** Required. Describes the memory for the instance type in GiB.
* **usage_class** Optional. Indicates whether the instance type is offered for spot or On-Demand.
* **burstable** Optional. Indicates whether the instance type is a burstable performance instance type.
* **architecture** Optional. The architectures supported by the instance type.
* **operation_systems** Optional. The operating system that you will use on the virtual machine.
* **is_current_generation** Optional. Use the latest generation or not.
* **is_best_price** Optional. Indicate if you need to get an instance type with the best price.
* **is_instance_storage_supported** Optional. Use instance types with instance store support

# Usage

## Simple

```
from amazon_ec2_best_instance import Ec2BestInstance

ec2_best_instance = Ec2BestInstance()

response = ec2_best_instance.get_best_instance_types({
    'vcpu': 1,
    'memory_gb': 2
})

print(response) # ['m5a.16xlarge', ... ,'r5n.metal']
```

## Advanced

```
import logging
from amazon_ec2_best_instance import Ec2BestInstance

# Optional.
options = {
    # Optional. Default: us-east-1
    'region': 'us-east-1',
    # Optional. Default: 10
    'describe_spot_price_history_concurrency': 20,
    # Optional. Default: 10
    'describe_on_demand_price_concurrency': 20
}

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
# Optional.
logger = logging.getLogger()

ec2_best_instance = Ec2BestInstance(options, logger)

response = ec2_best_instance.get_best_instance_types({
    # Required.
    'vcpu': 1,
    # Required.
    'memory_gb': 2,
    # Optional. Default: 'on-demand'. Values: 'spot'|'on-demand'
    'usage_class': 'spot',
    # Optional.
    'burstable': False,
    # Optional. Default: 'x86_64'. Values: 'i386'|'x86_64'|'arm64'|'x86_64_mac'
    'architecture': 'x86_64',
    # Optional. Default: ['Linux/UNIX']. Values: 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)'
    'operation_systems': ['Linux/UNIX'],
    # Optional.
    'is_current_generation': True,
    # Optional. If this parameter is set to True, the method will return the instance type with the best price.
    'is_best_price': True,
    # Optional. If this parameter is set to True, the method will return the instance type with the instance storage.
    'is_instance_storage_supported': True
})

print(response)

```
