#elapsed time
import time

start = time.perf_counter()
print("hello" + str(start))
end = time.perf_counter()
elapsed = end - start
print(elapsed)

