# 📋 DecodeLabs Task Engine (To-Do List CLI)

Welcome to **Project 1: To-Do List Engine**! This project is part of the **DecodeLabs Industrial Training Track**. It is designed to teach fundamental data management concepts in Python by building a command-line interface (CLI) task manager with permanent disk storage.

---

## 💡 What is this Project About?

This application allows users to create, view, and delete daily tasks through an interactive terminal menu. 

While a To-Do List seems simple on the surface, this project serves as a **micro-database engine**. Instead of just storing temporary words in memory, it demonstrates how real-world backend applications handle data structures, in-memory operations, and permanent file persistence (JSON).

---

## ⚙️ Key Technical Concepts (What Is Happening Under the Hood?)

### 1. Persistent Storage vs. Volatile RAM
- **The Problem:** Variables and lists created in Python only exist inside the computer's **RAM (Random Access Memory)**. When you close the terminal or switch off your computer, RAM is cleared and all data is lost.
- **The Solution:** We use **JSON Serialization** (`json.dump()` and `json.load()`) to write data to a text file (`my_tasks.json`) on your hard drive. Every time you open the program, it reads existing data from disk back into RAM.

### 2. In-Memory Database Structure
- Tasks are represented as **Python Dictionaries**:
  ```python
  {"id": 1, "title": "Complete Python Assignment"}
