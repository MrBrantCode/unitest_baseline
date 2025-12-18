"""
QUESTION:
Implement a function `revertTactic` that takes as input a proof state `s`, a list of goals `goals`, and a hypothesis `n` to be reverted. If `n` exists in `s`, create a new substitution by applying a new metavariable to the existing substitution, update the list of goals, and return a new proof state with the reverted hypothesis and updated substitution. If `n` does not exist in `s`, return an error message.

Function Signature: 
```python
def revertTactic(s: ProofState, goals: List[Goal], n: str) -> Union[ProofState, str]
```

Input:
- `s`: The current proof state
- `goals`: A list of goals to be proved
- `n`: The hypothesis to be reverted

Output:
- A new proof state if `n` exists in `s`, otherwise an error message as a string.
"""

from typing import List, Union, Dict

class ProofState:
    def __init__(self, hypotheses: List[str], substitution: Dict):
        self.hypotheses = hypotheses
        self.substitution = substitution

class Goal:
    def __init__(self, statement: str):
        self.statement = statement

def applyNewMeta(value: str) -> str:
    # Apply a new metavariable to the value
    return f"meta({value})"

def revertTactic(s: ProofState, goals: List[Goal], n: str) -> Union[ProofState, str]:
    if n in s.hypotheses:
        new_subst = {}  
        for key, value in s.substitution.items():
            new_subst[key] = applyNewMeta(value)  

        new_goals = goals[1:]  
        new_hypotheses = s.hypotheses.copy()
        new_hypotheses.remove(n)
        new_proof_state = ProofState(new_hypotheses, new_subst)  

        return new_proof_state
    else:
        return f"invalid 'revert' tactic, unknown hypothesis '{n}'"