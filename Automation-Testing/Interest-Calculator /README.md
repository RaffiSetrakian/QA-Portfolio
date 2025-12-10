# Compound Interest Calculator – Data-Driven Test Automation

This project automates the compound interest calculator at:
https://www.calculatestuff.com/financial/compound-interest-calculator

## What the script does
The automation uses a data-driven testing approach:
1. Reads input values and expected results from an Excel file.
2. Enters the data into the calculator fields.
3. Extracts the calculated “Actual Result” from the web application.
4. Writes the Actual Result back into the Excel file.
5. Compares Expected vs Actual.
6. Marks each row as Pass or Fail.

## Technologies Used
- Python (with pycharm)
- Selenium WebDriver  
- OpenPyXL (for Excel read/write)  
- ChromeDriver  

## Folder Structure
- **Scripts/** – Python automation scripts  
- **Test-Data/** – Excel file containing input values, expected results, actual results, and pass/fail  
- **Screenshots/** – Before/after execution screenshots  

## Purpose of the Project
This project demonstrates:
- Data-driven testing  
- Reading/writing Excel data programmatically  
- Validating system output against expected results  
- Complete workflow automation from input → validation → reporting  
