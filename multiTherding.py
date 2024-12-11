import threading
import time

def update_db():
    print("start to Updating...")
    time.sleep(5)
    print("Updated")

print(" ")
def display_num(num):
    
    print(num * num)
    
# update_db()
db = threading.Thread(target=update_db)
db.start()
display_num(10)

print(threading.active_count())
print(threading.enumerate())

db.join()
print("bye...")

