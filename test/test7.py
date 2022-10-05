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
    # Required. Float
    'vcpu': 32,
    # Required. Float
    'memory_gb': 7.5,
    # Optional. String. Default: 'on-demand'. Values: 'spot'|'on-demand'
    'usage_class': 'spot',
    # Optional.
    'burstable': False,
    # Optional. Boolean. Default: 'x86_64'. Values: 'i386'|'x86_64'|'arm64'|'x86_64_mac'
    'architecture': 'x86_64',
    # Optional. Array(String). Default: ['Linux/UNIX']. Values: 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)'
    'operation_systems': ['Linux/UNIX'],
    # Optional. Boolean
    'is_current_generation': True,
    # Optional. Boolean. If this parameter is set to True, the method will return the instance type with the best price.
    'is_best_price': True,
    # Optional. Boolean. If this parameter is set to True, the method will return the instance type with the instance storage.
    'is_instance_storage_supported': True,
    # Optional. Integer. Max spot instance frequency interruption in percent. Note: If you specify >=21, then the '>20%' rate is applied
    # It is used only if 'usage_class' == 'spot' and 'is_best_price' == True
    #'max_interruption_frequency': 10
})

print(response)
