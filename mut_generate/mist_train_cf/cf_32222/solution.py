"""
QUESTION:
Write a function `generate_nmt_training_command` that takes in 12 parameters: source language `src`, target language `tgt`, vocabulary prefix `vocab_prefix`, training data prefix `train_prefix`, development data prefix `dev_prefix`, test data prefix `test_prefix`, output directory `out_dir`, number of training steps `num_train_steps`, steps per statistics computation `steps_per_stats`, number of layers `num_layers`, number of units `num_units`, dropout rate `dropout`, and evaluation metric `metrics`. The function should return a command string that invokes the `nmt.nmt` module with the provided parameters to train a neural machine translation model.
"""

def generate_nmt_training_command(src, tgt, vocab_prefix, train_prefix, dev_prefix, test_prefix, out_dir, num_train_steps, steps_per_stats, num_layers, num_units, dropout, metrics):
    command = f"python -m nmt.nmt " \
              f"--src={src} --tgt={tgt} " \
              f"--vocab_prefix={vocab_prefix} " \
              f"--train_prefix={train_prefix} " \
              f"--dev_prefix={dev_prefix} " \
              f"--test_prefix={test_prefix} " \
              f"--out_dir={out_dir} " \
              f"--num_train_steps={num_train_steps} " \
              f"--steps_per_stats={steps_per_stats} " \
              f"--num_layers={num_layers} " \
              f"--num_units={num_units} " \
              f"--dropout={dropout} " \
              f"--metrics={metrics}"
    return command