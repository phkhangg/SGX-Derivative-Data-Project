from indexcrawler import getFileDate, createTable, addTable
from downloader import downloader
import logging

# Initialize logging (you need to configure logging before using it)
logging.basicConfig(filename='daily_update.log', level=logging.INFO)

def getLatestIndex():
    with open('indextable/latestindex.txt', 'r') as f:
        a = f.read().split(' ')
    
    if not a:
        latestindex = 5492  # prepare for initializing
        latestdate = '20230824'
    else:
        latestdate, latestindex = a[:2]
    
    latestindex = int(latestindex)
    
    done = False
    while not done:
        temp = getFileDate(latestindex + 1)
        if temp == '0':
            done = True
        else:
            latestdate = temp
            latestindex += 1

    with open('indextable/latestindex.txt', 'w') as f:
        f.write(f'{latestdate} {latestindex}')

def dailyUpdate():
    getLatestIndex()
    with open('indextable/latestindex.txt', 'r') as f:
        a = f.read().split(' ')
    date, index = a[:2]
    addTable(int(index))
    downloader(date, int(index))
    logging.info(f'Daily update completed for date {date}, index {index}')

def recreateIndextable():
    getLatestIndex()
    with open('indextable/latestindex.txt', 'r') as f:
        a = f.read().split(' ')
    index = int(a[1])
    createTable(2755, index)
    
    with open('indextable/indexmissed.txt', 'r') as f:
        a = f.read().split(' ')
    for i in a:
        if i:
            addTable(int(i))
    print(f'Latest index created from 2755 to {index}')

