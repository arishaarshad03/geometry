# Drawing App with OOP in Python 🖌️🧩

This project is a basic drawing simulation built using **Object-Oriented Programming (OOP)** principles in Python. It models simple geometrical drawing components like `Point`, `Line`, `Pen`, `Canvas`, and `Circle`.

---

## 📦 Project Structure

- **`point.py`** – Represents a point on a 2D plane with x and y coordinates.
- **`line.py`** – Represents a line segment between two `Point` objects.
- **`canvas.py`** – Stores and manages all drawn lines on a virtual canvas.
- **`pen.py`** – Inherits from `Point` and acts like a movable drawing pen, used to draw lines between points on the canvas.
- **`circle.py`** – Represents a circle with a center (`Point`) and a radius. Can compute area, circumference, and display details.

---

## 💡 Features

- ✅ Move pen to any point  
- ✅ Draw lines using two `Point` instances  
- ✅ Display canvas with all drawn lines  
- ✅ Create and modify circles  
- ✅ Encapsulation using getters/setters and properties  
- ✅ Use of composition and inheritance  
- ✅ Special dunder methods like `__str__`, `__repr__`, `__len__`
