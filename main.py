import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

print("####################################################\n")
print("             Python-based Web Crawler               \n")
print("####################################################\n")
print("\n")
HOMEPAGE = input("Enter URL to crawl: ")
PROJECT_NAME = 'SPY_WEB'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 2
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create Threads
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t  = threading.Thread(target=work)
        t.daemon = True
        t.start()

#Do the next job in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each link is new job
def create_job():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


#Check for items and if found, crawl
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links))+ " links in the queue")
        create_job()


create_spiders()
crawl()
