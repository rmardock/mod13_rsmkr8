import unittest
# Import datetime module for testing date formats
import datetime

# Class to test the symbol input
class SymbolTest(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Value to be tested
        self.a = "AAPL"
    
    # Function to test if characters are letters
    def test_symbol_value(self):
        # Act
        result = self.a.isalpha()
        # Assert
        self.assertTrue(result)
        
    # Function to test if there are between 1 and 7 characters in symbol
    def test_symbol_character_count(self):
        # Act
        result = len(self.a)
        # Assert
        self.assertIn(result, range(1, 8, 1))
    
# Class to test the chart input
class ChartTest(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Value to be tested
        self.a = 2 
    
    # Function to test if the chart input is an integer
    def test_chart_value_type(self):
        # Act
        result = isinstance(self.a, int)
        # Assert
        self.assertTrue(result)
    
    # Function to test if the chart input is between 1 and 2
    def test_chart_value(self):
        # Act
        result = self.a
        # Assert
        self.assertIn(result, range(1, 3, 1))
        
# Class to test the time series input
class TimeSeriesTest(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Value to be tested
        self.a = 1
    
    # Function to test if the time series input is an integer
    def test_time_series_value_type(self):
        # Act 
        result = isinstance(self.a, int)
        # Assert
        self.assertTrue(result)
    
    # Function to test if the time series input is between 1 and 4
    def test_time_series_value(self):
        # Act 
        result = self.a
        # Assert 
        self.assertIn(result, range(1, 5, 1))
      
# Class to test the start date input  
class StartDateTest(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Value to be tested
        self.a = '2000-01-01'
        
    # Function to test if the start date adheres to the correct format
    def test_start_date_value(self):
        # Act
        result = date_format_ex(self.a)
        # Assert
        self.assertTrue(result)

# Function for handling ValueError exceptions in StartDateTest  
def date_format_ex(x):
    # Format test date against
    format = "%Y-%m-%d"
    # If date format is correct, return True
    try:
        # Attempt to convert date string to datetime object
        # If the date format is incorrect, a ValueError exception will be thrown
        datetime.datetime.strptime(x, format)
        return True
    # If date format is incorrect, handle exception and return false
    except ValueError:
        print("Value Error! Date format incorrect!")
        return False
    
if __name__ == "__main__":
    unittest.main()