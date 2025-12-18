"""
QUESTION:
Write a function named `generate_training_commands` that generates shell commands to train a model with different combinations of learning rates and weight decay values. The function should take four parameters: `learning_rates` (a list of learning rates), `weight_decays` (a list of weight decay values), `config_file` (the path to the configuration file), and `num_epochs` (the total number of epochs). The function should return a list of shell commands, each in the format `./tools/dist_train.sh {config_file} 4 --options optimizer.lr={lr} optimizer.weight_decay={wd} total_epochs={num_epochs} --work-dir work_dirs/fusion_lr_{lr}_{wd}_e{num_epochs}`, where `{lr}` and `{wd}` are the learning rate and weight decay values, respectively, and `{config_file}` and `{num_epochs}` are the configuration file and number of epochs, respectively.
"""

def generate_training_commands(learning_rates, weight_decays, config_file, num_epochs):
    commands = []
    for lr in learning_rates:
        for wd in weight_decays:
            command = f"./tools/dist_train.sh {config_file} 4 " \
                      f"--options optimizer.lr={lr} optimizer.weight_decay={wd} " \
                      f"total_epochs={num_epochs} " \
                      f"--work-dir work_dirs/fusion_lr_{lr}_{wd}_e{num_epochs}"
            commands.append(command)
    return commands