# 📊 Sales Data Analyzer — Python OOP Project

A beginner-friendly, menu-driven Sales Data Analyzer made using **Python modules, packages, and Object-Oriented Programming**.

## Important

This version does **NOT require any external dataset**.

All sample sales records are created inside `sales_analyzer/data.py`, so you can concentrate on learning Python and OOP first.

No Pandas, NumPy, database, API, or other external library is required.

## Project Structure

```text
Sales_Data_Analyzer_No_Dataset/
│
├── main.py
├── README.md
├── requirements.txt
│
└── sales_analyzer/
    ├── __init__.py
    ├── data.py
    ├── models.py
    ├── analyzer.py
    ├── reports.py
    └── utils.py
```

## How to Run

Open the terminal in the project folder and run:

```bash
python main.py
```

## What Each File Does

### `main.py`
The starting point of the program. It displays the menu and calls the required methods.

### `data.py`
Creates sample sales records using Python objects. There is no CSV dataset.

### `models.py`
Contains the `SalesRecord` class. One object represents one sales transaction.

### `analyzer.py`
Contains the analysis logic such as total sales, total profit, best product, category analysis, and region analysis.

### `reports.py`
Displays the results neatly in the terminal.

### `utils.py`
Contains small reusable helper functions such as safe integer input.

### `__init__.py`
Makes `sales_analyzer` a Python package and exposes important classes.

## OOP Concepts Used

### 1. Class
`SalesRecord` is a class used as a blueprint for sales transactions.

### 2. Object
Each call such as:

```python
SalesRecord(1001, "2026-01-05", "Laptop", ...)
```

creates an object.

### 3. Constructor
`__init__()` initializes the values of each object.

### 4. Methods
Methods such as `total_sales()` and `total_profit()` perform operations.

### 5. Inheritance
`SalesAnalyzer` inherits from `AnalyzerBase`.

`ConsoleReport` inherits from `Report`.

### 6. Encapsulation
The data and operations are organized inside classes instead of putting everything into one large function.

### 7. Polymorphism
`ConsoleReport` provides its own `show()` behavior while inheriting from the base `Report` class.

## Program Flow

```text
main.py
   ↓
create_sample_data()
   ↓
SalesRecord Objects
   ↓
SalesAnalyzer
   ↓
ConsoleReport
   ↓
Terminal Output
```

## Menu Features

1. Display all sales
2. Calculate total sales
3. Calculate total profit
4. Calculate average order value
5. Find best-selling product
6. Find most profitable product
7. Analyze sales by category
8. Analyze sales by region
9. Search for a product
10. Display complete summary
0. Exit

## Easy Viva Explanation

**Question: Why did you divide the project into modules?**

Answer: I divided the project into modules so that each module has one clear responsibility. This makes the code easier to understand, maintain, and reuse.

**Question: What is a package?**

Answer: A package is a folder containing related Python modules. The `sales_analyzer` folder is my package.

**Question: Why did you use a class?**

Answer: I used a class to represent a sales transaction as an object and keep related data and behavior organized.

**Question: Where is the data?**

Answer: The sample data is generated in `data.py` using `SalesRecord` objects. I intentionally did not use an external dataset.

**Question: What happens when the program starts?**

Answer: `main.py` creates the sample records, creates a `SalesAnalyzer` object, creates a `ConsoleReport` object, and then displays the menu.

**Question: What happens when I select Total Sales?**

Answer: The program calls `total_sales()`, which uses a loop internally through the sales objects and adds their sales values.

## Future Improvements

After understanding this version, the project can later be extended with:

- CSV file handling
- User-added sales records
- Data validation
- Monthly analysis
- Graphs
- Database storage

Those features are intentionally left out of this beginner version.
