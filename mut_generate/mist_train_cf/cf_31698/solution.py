"""
QUESTION:
Implement the function `check_molecular_equivalence(record, mutation_record, mutator)` to check the equivalence of two molecular records. The function should take three parameters: `record` (the original molecular record), `mutation_record` (the mutated molecular record), and `mutator` (an object with a `mutate` method that performs the mutation on a molecular record). The function should return `True` if the mutator name of the mutated record matches the mutator name of the `mutation_record` and the molecules in both records are equivalent; otherwise, it should return `False`.
"""

def entrance(record, mutation_record, mutator):
    result = mutator.mutate(record)
    if result.get_mutator_name() == mutation_record.get_mutator_name():
        return result.get_molecule_record().get_molecule() == mutation_record.get_molecule_record().get_molecule()
    else:
        return False