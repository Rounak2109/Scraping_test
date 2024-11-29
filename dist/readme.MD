## Scraping Application
# Overview
Welcome to the Scraping Application! This is an initial draft of the application that allows users to calculate the median of prices of different products and also see the product detail in a JSON format in Console. While the core functionality is in place, there is significant potential for improvement and enhancement.

## Getting Started
# Prerequisites
    Python: 
        1. Ensure you have Python installed on your system. You can download it from python.org.
        2. Make sure you have pip installed in your system.

    Git: For version control

    Dependencies: 
        The application relies on python packages which is mentioned in requirements.text 
    Set Up Virtual Environment:
        python -m venv <env_name>. Eg: python -m venv env
    
    Activate the Environment:
        C:\Python_project>cd env
        C:\Python_project\env>cd Scripts
        C:\Python_project\env\Scripts>activate
        (env) C:\Python_project\env\Scripts>cd ../..
        (env) C:\Python_project> pip install -r <Path of the requirement.text file>


# Running the Application
    To run the application, simply double-click the provided executable file (scraping_test.exe). The console application will launch, and you will be prompted to select two options either 1 or 2.
    By pressing 1, the application will run and scrape different product names and prices and calculate the median and run *Test Cases* to check whether the calculated median is correct or not

# Features
    Median Calculation: Calculate the median of different product.
    User-Friendly Interface: Interact with the application through a simple console interface.

## Future Improvements
This is just the beginning! Here are some ideas for future enhancements:

# Need to Omit the Server Call:
    In the next release, numerous server calls will be reduced for fetching dynamic contents

# Getting the Short Description: 
    Need to fetch the product description from product detail page.

# Improved User Interface: 
    Develop a graphical user interface (GUI) for better user experience.

# Error Handling: 
    Enhance error handling to manage invalid inputs gracefully.

# Unit Tests: 
    Implement unit tests for other functionalities.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.

