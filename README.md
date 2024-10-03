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


----

- set the scene for a calculator
    - parser, ast nodes
- use isinstance to do evaluation, basic functions
- downside: have this god function that does switching
    - it needs to know about the whole class hierarchy
    - brittle, every time you add a new class you also need to update this function to match
- one way to solve this is with polymorphism
    - add a super class with an evaluate method; call that recursively
    - benefit is now you can add more classes that do this without having to update anything else
    - no god function that has to import the whole hiearchy of objects
- later on, say you want to add another ability to this calcalator, like the ability to print out an equation; say if you have something the simplifies or normalizes the notation
    - pretty can be implemented the same way
    - seems good, this is OOP, and it works well for GUIs, business objects, many domains
- but what happens in systems like this is 





