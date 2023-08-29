import logging
from ast import literal_eval
from downloader import downloader

# Download files by index table retrieval
def retrieval(date):
    try:
        with open('indextable/indextable.txt', 'r') as f:
            index_table = literal_eval(f.read())
        
        index = index_table.get(str(date))
        if index is None:
            logging.error(f"{date} is not in the index table. Please check the index table contents.")
            return
        
        downloader(date, index)
    
    except FileNotFoundError:
        logging.error("Index table file not found.")
    except ValueError:
        logging.error("Error while parsing the index table. Make sure it's properly formatted.")
    except KeyError:
        logging.error(f"{date} is not found in the index table. Please check the date format or content of the index table.")
    except Exception as e:
        logging.error(f"An error occurred during retrieval of {date}: {e}")
