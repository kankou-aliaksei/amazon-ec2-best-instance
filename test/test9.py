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
[{'instance_type': 'r5a.8xlarge', 'price': '0.578100'}]
'''