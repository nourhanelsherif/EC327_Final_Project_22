## EC327 Final Project

Team Name: Auto BOM

Team Members: Nashr El Auliya, Prakruti Dholiya, Nourhan El Sherif, Yidi Wu

Overview: One of the preliminary steps of an engineering project includes creating a Bill of Materials (BOM), which is a comprehensive list of all the components required to build a product. However, this task can be a very time-consuming process, especially with budget constraints that exist on student projects. Our team opted to create a program that would automate the decision-making for creating a BOM. Previous BU classes that required materials and BOMs often used Newark Electronics, and so our team opted to scrape from the Newark Electronics Catalog. The program takes into consideration the user’s budget and informs the user if the list of items is attainable with the specified budget. Taking the quantity of each item into consideration, the program finds the optimal quantity to purchase in order to get the best deal from Newark. The final output of the program is a csv file of the BOM with the cheapest option of each item, along with details like quantity and the item’s url.

How to Build: One way to build or replicate this project is to create the program using the Python language to web scrape. Python’s three key web scraping libraries are Pandas, Beautiful Soup 4, and Selenium. First, declare data structures to store the values in. Then, use the webdriver and the correct url based on the user input to open the chrome page then scrape data. Save the scraped information into their appropriate data structures, ensuring that the data structures are iterable or accessible to the algorithm in some way. Next, create an algorithm that finds the cheapest variant of each item. Finally, return the data and output it to a CSV. Then, optimize the search results for the best option out of all available options. Store the final price for the item, its quantity, name, and url into the data structures previously made. Use the Excel library in python to output to a csv file with the stored data. Finally, build a GUI that can take in user inputs rather than directly taking inputs from the command line. Run test cases for the BOM and the GUI, and troubleshoot. 

# YouTube Link: https://youtu.be/w7t5iaJ1ddY

NOTE: Program needs following library to work. Download using ‘pip install openpyxl’

install everything:

pip install tkinter

pip install pandas

pip install bs4

pip install selenium

pip install openpyxl
