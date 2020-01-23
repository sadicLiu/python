from time import time

start_time = time()
print('Start time: ', start_time)

for i in range(10000000):
    pass

end_time = time()
print('End time: ', end_time)

print('Time spent: ', end_time - start_time)
