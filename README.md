OOP Assignment - Classes, Inheritance, Encapsulation & Polymorphism
Overview
This project demonstrates Object-Oriented Programming (OOP) concepts in Python.  
It combines two activities:  
1. Assignment 1: Design Your Own Class 
   - Created a `Smartphone` class that inherits from a `Device` class.  
   - Showcases encapsulation by keeping the device status private.  
   - Includes methods to power on/off, make calls, and take photos.  
2. Activity 2: Polymorphism Challenge 
   - Implemented different `Vehicle` classes (`Car`, `Plane`, `Boat`).  
   - Each class has the same method `move()`, but behaves differently.  
   - Demonstrates polymorphism in Python.  
Features
- Encapsulation→ `__status` attribute in `Device` is private.  
- Inheritance→ `Smartphone` extends the `Device` class.  
- Polymorphism→ `move()` method behaves differently across vehicles.  
 Code Structure
- `Device` → Base class for electronic devices.  
- `Smartphone` → Inherits from `Device`, adds storage, call, and photo features.  
- `Vehicle` → Base class for vehicles.  
- `Car`, `Plane`, `Boat` → Inherit from `Vehicle` and override `move()`.  
 How to Run
1. Save the Python code into a file, e.g. `oop_assignment.py`.  
2. Run the file using:  
python oop_assignment.py
