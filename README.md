Code for PyCon NL 2024 talk.


Solving the expression problem in Python

But it can be simpler. Build on the polymorphism and single_dispatch examples from my book. Is there a way to do it that's more Pythonic? How does it work with type hints?


Polymorphism without Classes

The Zen of Polymorphism

"There are no classes"

Outline:
- Explain the MRO mechanism
- UFCS
- What is an object
- Bound methods, method resolution
- Single dispatch


- part 1: what does it do?
    - polymorphism value using objects
    - single dispatch approach with functions
    - when to use objects/polymorphism vs. single dispatch / multi-methods
- part 2: how do objects work?
    - what is a closure
    - what is a bound method
    - simulating objects with closures
    - object oriented features in python are all a way to reduce boiler plate and repetitive code
    - how do you implement isinstance?
- part 3: how do multi-methods work?


