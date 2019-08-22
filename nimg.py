# input: the number of images to be stored,
# their urls, and names to be given to them
# action: downloading and storing them
# all the while using multithreading

import os
import threading

n = int(input("Enter the number of images you intend to download."))

url, fname, t = [], [], []

# the function which actually does all the labour
def the_worker(u, f):
    str = "wget -O {0} {1}".format(f, u)
    os.system(str)

i = 1
while (i <= n):
    url.append(input("Enter the url for image no." + str(i) + ": "))
    fname.append(input("Enter the name for the file for this image: ") + ".jpg")
    # t[i - 1] represents the ith task
    t.append(threading.Thread(target = the_worker, args = (url[i - 1], fname[i - 1])))
    i += 1

i = 1
while (i <= n):
    t[i - 1].start()
    i += 1

i = 1
while (i <= n):
    t[i - 1].join()
    i += 1

print("Task accomplished.")
