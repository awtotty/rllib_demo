# Tutorial: 
# https://medium.com/distributed-computing-with-ray/a-step-by-step-guide-to-scaling-your-first-python-application-in-the-cloud-8761fe331ef1

import ray
import time
from datetime import datetime as dt

@ray.remote
def adder(input_value): 
    time.sleep(1) 
    return input_value + 1

def main(): 
    ray.init()
    values = list(range(10))
    start = dt.now()

    # run adder() on available nodes
    # each call returns an object reference to the returned value
    # that is stored somewhere on the network
    new_values = [adder.remote(x) for x in values]

    # get the values from the references
    returned_values = ray.get(new_values)

    end = dt.now()

    print(f"Values: {values}")
    print(f"New values: {new_values}")
    print(f"Returned values: {returned_values}")
    print(f"Time: {(end-start).total_seconds()}")

if __name__ == "__main__": 
    main()