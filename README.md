# Amazon EC2 Best Instance (amazon-ec2-best-instance)

Amazon EC2 Best Instance (amazon-ec2-best-instance) allows you to choose the most optimal and cheap EC2 instance type for on-demand and spot and with a less reclaimed rate for a spot instance.

# Prerequisites
* python3
* pip3
* boto3  
* AWS Account
* AWS Credentials

# Install
pip install amazon-ec2-best-instance

# Options

* **vcpu** Required. Float. Describes the vCPU configurations for the instance type.
* **memory_gb** Required. Float. Describes the memory for the instance type in GiB.
* **usage_class** Optional. String. Indicates whether the instance type is offered for spot or On-Demand.
* **burstable** Optional. Boolean. Indicates whether the instance type is a burstable performance instance type.
* **architecture** Optional. String. The architectures supported by the instance type.
* **product_descriptions** Optional. List<String>. The operating system that you will use on the virtual machine. Values: Linux/UNIX | Red Hat Enterprise Linux | SUSE Linux | Windows | Linux/UNIX (Amazon VPC) | Red Hat Enterprise Linux (Amazon VPC) | SUSE Linux (Amazon VPC) | Windows (Amazon VPC)
* **is_current_generation** Optional. Boolean. Use the latest generation or not.
* **is_best_price** Optional. Boolean. Indicate if you need to get an instance type with the best price. If this flag is specified, the "get_best_instance_types" method returns a list of instance types sorted by price in ascending order.
* **is_instance_storage_supported** Optional. Boolean. Use instance types with instance store support
* **max_interruption_frequency** Optional. Integer (%). Max spot instance frequency interruption in percent. Note: If you specify >=21, then the '>20%' rate is applied. It is used only if 'usage_class' == 'spot' and 'is_best_price' == True
* **availability_zones** Optional. List<String>. Availability zones
* **final_spot_price_determination_strategy** Optional. String. Default: "min". Valid values: "min"|"max"|"average"

# Usage

## Simple

```
from amazon_ec2_best_instance import Ec2BestInstance

ec2_best_instance = Ec2BestInstance()

# It returns all available instance types, including those with over-provisioning resources (CPU, memory, etc.).
response = ec2_best_instance.get_best_instance_types({
    'vcpu': 1,
    'memory_gb': 2
})

print(response)

'''
[{'instance_type': 'c5n.2xlarge'}, ... , {'instance_type': 'x2iedn.8xlarge'}]
'''
```

## Advanced

```
import boto3
from botocore.config import Config
import logging
from amazon_ec2_best_instance import Ec2BestInstance

ec2_client_config = Config(
    retries={
        'max_attempts': 20,
        'mode': 'adaptive'
    }
)

pricing_client_config = Config(
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

ec2_client = boto3.Session().client('ec2', config=ec2_client_config)
pricing_client = boto3.Session().client('pricing', config=pricing_client_config)

# Optional.
options = {
    # Optional. Default: us-east-1
    'region': 'us-east-1',
    # Optional. Default: 10
    'describe_spot_price_history_concurrency': 20,
    # Optional. Default: 10
    'describe_on_demand_price_concurrency': 20,
    'clients': {
        'ec2': ec2_client,
        'pricing': pricing_client
    },
    # Optional. Integer. Default: 120. It limits the lifetime of cache data.
    'cache_ttl_in_minutes': 60
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
    # Optional. Default: ['Linux/UNIX'].
    # Values: Linux/UNIX | Red Hat Enterprise Linux | SUSE Linux | Windows | Linux/UNIX (Amazon VPC) | 
        # Red Hat Enterprise Linux (Amazon VPC) | SUSE Linux (Amazon VPC) | Windows (Amazon VPC)
    'product_descriptions': ['Linux/UNIX'],
    # Optional.
    'is_current_generation': True,
    # Optional. If this parameter is set to True, the method will return the instance type with the best price.
    'is_best_price': True,
    # Optional. If this parameter is set to True, the method will return the instance type with the instance storage.
    'is_instance_storage_supported': True,
    # Optional. Integer. Max spot instance frequency interruption in percent.
    'max_interruption_frequency': 10,
    # Optional. List<String>. The availability zones.
    'availability_zones': ['us-east-1a', 'us-east-1b']
})

print(response)
'''
[{'instance_type': 'c5d.large', 'price': '0.032700', 'interruption_frequency': {'min': 0, 'max': 5, 'rate': '<5%'}}, ...]
'''

```

## Spot

If you need to get a spot instance with minimal price and minimal frequency of interruption you can use 'is_best_price' and/or 'max_interruption_frequency' input parameter

```
from amazon_ec2_best_instance import Ec2BestInstance

ec2_best_instance = Ec2BestInstance()

response = ec2_best_instance.get_best_instance_types({
    # Required. Float
    'vcpu': 31.2,
    # Required. Float
    'memory_gb': 100.5,
    # Optional. String. Default: 'on-demand'. Values: 'spot'|'on-demand'
    'usage_class': 'spot',
    # Optional. Boolean.
    # If this parameter is set to True, the method will return the instance type with the best price.
    'is_best_price': True,
    # Optional. Integer. Max spot instance frequency interruption in percent.
    # Note: If you specify >=21, then the '>20%' rate is applied
    # It is used only if 'usage_class' == 'spot' and 'is_best_price' == True
    'max_interruption_frequency': 10
})

print(response)
'''
[{'instance_type': 'm6id.8xlarge', 'price': '0.642600', 'interruption_frequency': {'min': 6, 'max': 10, 'rate': '5-10%'}}, ...]
'''
```

```
from amazon_ec2_best_instance import Ec2BestInstance

ec2_best_instance = Ec2BestInstance()

response = ec2_best_instance.get_best_instance_types({
    # Required. Float
    'vcpu': 31.2,
    # Required. Float
    'memory_gb': 100.5,
    # Optional. String. Default: 'on-demand'. Values: 'spot'|'on-demand'
    'usage_class': 'spot',
    # Optional. Boolean.
    # If this parameter is set to True, the method will return the instance type with the best price.
    'is_best_price': True
})

print(response)
'''
[{'instance_type': 'r5a.8xlarge', 'price': '0.578100'}, ...]
'''
```