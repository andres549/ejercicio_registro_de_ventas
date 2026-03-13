# Daily Sales Log System

A simple Python program to record and summarize daily product sales Introduction

The Daily Sales Log System is a simple Python program that allows you to record product sales and generate a summary of all sales made during the day.
The program runs in the terminal and prompts the user to enter the product name, price, and quantity sold. It automatically calculates the total sale amount and stores the information in memory.At the end of the session, the program displays a summary with all products sold, their quantities, and the total amount collected.
This project demonstrates the use of functions, modules, dictionaries, input validation, and basic program organization in Python.

# Features

* Record multiple product sales during a session
* Automatically calculate the total sale amount
* validate user input to ensure only numbers are entered for price and quantity
* Store sales history using a dictionary
* Display a final summary with all sold products
* Code organized using independent Python modules

# Project Structure

Daily Sales System

 main.py
 title.py
 register.py
 history.py

# File Description
* main.py
This is the program's main file. It controls the program flow, calls functions from other modules, and manages the daily sales process.

* title.py
Contains the function that displays the welcome title when the program starts.

* register.py
Manages the registration of product sales. It prompts the user for the product name, price, and quantity, validates the input, calculates the total sale, and stores the information.

* history.py
It displays the final daily summary with all products sold, their quantities, and the total amount collected.

# How the program works

* The program starts by displaying a welcome message.
* The user enters the product name.
* The user enters the product price.
* The program validates that the price contains only numbers.
* The user enters the quantity sold.
* The program calculates the total sale.
* The user decides whether to register another product.
* At the end, the program displays a daily sales summary.

# Installation (for users)

* Make sure Visual Studio Code is installed on your computer with the Python extension.
* Download or clone the repository.
* Open a terminal in the project folder.
* Run the program:
* python main.py
* Installation (For contributors)

If you want to modify or improve the project:

Clone the repository

git clone <repository-url>

Open the project folder

cd Daily-Sales-System

Run the program locally

python main.py
Example output
==========================================
DAILY SALES LOG
=========================================

Product Name: Shirt
Product Price: 20
Quantity Sold: 2
Total Sale Amount: 40

Do you want to register another product? (Yes/No): Yes

Product Name: Pants
Product Price: 30
Quantity Sold: 1
Total Sale Amount: 30

Do you want to register another product? (Yes/No): No

======================================
DAILY SUMMARY
====================================

Product: Shirt
Quantity Sold: 2
----------------------------

Product: Pants
Quantity Sold: 1
----------------------------

Total Collected: 70
Known Issues

Currently, the program only stores sales during execution (data is not saved permanently).

* If the program is closed, the sales history is lost.
* Future improvements may include:
* Saving sales data to a file
* Adding more advanced reports

