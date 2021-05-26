from datetime import datetime
import time

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
         30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

for i in range(5):
    right_this_second = datetime.today().second

    if right_this_second in evens:
        print("This second seems a little even")
    else:
        print("Not an even second")