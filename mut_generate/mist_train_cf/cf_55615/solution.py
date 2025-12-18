"""
QUESTION:
Write a function named `is_singleton_class_justifiable` that determines whether a singleton class is justified in a given context. The function should consider the context of testability, concurrency, inheritance and polymorphism, code coupling, scalability, single responsibility principle, performance, and modular systems or plugins.
"""

def is_singleton_class_justifiable(testability, concurrency, inheritance_polymorphism, code_coupling, scalability, single_responsibility_principle, performance, modular_systems_plugins):
    """
    This function determines whether a singleton class is justified in a given context.
    
    Parameters:
    testability (bool): Whether the singleton class is testable.
    concurrency (bool): Whether the singleton class is thread-safe.
    inheritance_polymorphism (bool): Whether the singleton class allows inheritance and polymorphism.
    code_coupling (bool): Whether the singleton class is loosely coupled.
    scalability (bool): Whether the singleton class is scalable.
    single_responsibility_principle (bool): Whether the singleton class follows the Single Responsibility Principle.
    performance (bool): Whether the singleton class has good performance.
    modular_systems_plugins (bool): Whether the singleton class is suitable for modular systems or plugins.
    
    Returns:
    bool: Whether the singleton class is justified.
    """
    justification_factors = [
        testability, 
        concurrency, 
        inheritance_polymorphism, 
        not code_coupling,  # tightly coupled systems are not justifiable
        scalability, 
        single_responsibility_principle, 
        performance, 
        not modular_systems_plugins  # avoid in modular systems or plugins
    ]
    
    # If more than half of the factors are False, the singleton class is not justifiable
    return justification_factors.count(False) <= len(justification_factors) / 2