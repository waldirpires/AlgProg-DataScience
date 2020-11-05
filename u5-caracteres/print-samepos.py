import time
for i in range(10):
    time.sleep(0.4)
    print ("\r Loading... {}".format(i)+str(i), end="")
print()