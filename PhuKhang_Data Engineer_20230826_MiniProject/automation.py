import logging
import schedule
import time
import sys
from dailyupdate import dailyUpdate

logging.basicConfig(filename='automation.log', level=logging.INFO)

def automation():
    logging.info('Automation started!')
    schedule.every().day.at("07:30").do(dailyUpdate)
    #You can change your time of dailyUpdate at here and yeah is 24hrs clock
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        logging.error(f'Automation failed: {e}')

