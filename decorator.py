import datetime
import time
import Log

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    # get the start datetime
    st = datetime.datetime.now()
    sum_x = 0
    for i in range(1000000):
        sum_x += i
    # wait for 3 seconds
    time.sleep(3)
    print('Sum of first 1 million numbers is:', sum_x)
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    execution_time = 'Execution time:', elapsed_time, 'seconds'
    print(execution_time)
    # Write the specified text to the logfile
    Log.logging.info(execution_time)

ordinary()

