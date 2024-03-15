import os

i = 0
while os.path.exists("output%.mid" % i):
    i + 1

