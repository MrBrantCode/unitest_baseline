"""
QUESTION:
Implement the `test_argparser` function, which takes in the benchmark name, default number of iterations, default problem sizes list, expert list, and dynamic at compile time list as arguments. The function should parse the command-line arguments and return the parsed arguments as a dictionary.

The function should accept the following arguments:
- `benchmark_name`: the name of the benchmark
- `default_n_iters`: the default number of iterations (integer)
- `default_problem_sizes_list`: a list of lists, where each inner list represents a problem size configuration and contains the following elements: N (batch size), W (input width), C (input channels), KW (kernel width), F (number of filters), st (stride), and dil (dilation)
- `default_expert_list`: a list of experts
- `default_dynamic_at_compile_time_list`: a list of dynamic at compile time

The function should parse the following command-line arguments:
- `--n_iters`: the number of iterations (integer, default: `default_n_iters`)
- `--problem_sizes_list`: the list of problem sizes (list of integers, default: `default_problem_sizes_list`)
- `--expert_list`: the list of experts (list of strings, default: `default_expert_list`)
- `--dynamic_at_compile_time_list`: the list of dynamic at compile time (list of strings, default: `default_dynamic_at_compile_time_list`)
"""

import argparse

def test_argparser(benchmark_name, default_n_iters, default_problem_sizes_list, default_expert_list, default_dynamic_at_compile_time_list):
    parser = argparse.ArgumentParser(description=benchmark_name)
    parser.add_argument('--n_iters', type=int, default=default_n_iters, help='Number of iterations')
    parser.add_argument('--problem_sizes_list', nargs='+', type=int, default=default_problem_sizes_list, help='List of problem sizes')
    parser.add_argument('--expert_list', nargs='+', default=default_expert_list, help='List of experts')
    parser.add_argument('--dynamic_at_compile_time_list', nargs='+', default=default_dynamic_at_compile_time_list, help='List of dynamic at compile time')

    args = parser.parse_args()
    return vars(args)