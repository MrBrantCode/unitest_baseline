"""
QUESTION:
Implement a function `parseCommandLineArgs` that takes a list of command-line arguments as input and returns a dictionary containing the extracted information. The dictionary should have the following keys: `preemptible`, `num_nodes`, and `disk_size`, representing whether the virtual machine is preemptible, the number of nodes for the virtual machine, and the disk size for the virtual machine, respectively. The command-line arguments include `--preemptible`, `--num-nodes <value>`, and `--disk-size <value>`. The function should parse these arguments and update the corresponding dictionary values accordingly.
"""

def parseCommandLineArgs(args):
    parsed_args = {
        'preemptible': False,
        'num_nodes': 0,
        'disk_size': '10GB'
    }
    
    i = 0
    while i < len(args):
        if args[i] == '--preemptible':
            parsed_args['preemptible'] = True
        elif args[i] == '--num-nodes' and i + 1 < len(args):
            parsed_args['num_nodes'] = int(args[i + 1])
            i += 1
        elif args[i] == '--disk-size' and i + 1 < len(args):
            parsed_args['disk_size'] = args[i + 1]
            i += 1
        i += 1
    
    return parsed_args