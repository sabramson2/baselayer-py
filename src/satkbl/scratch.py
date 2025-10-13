import threading
import multiprocessing
import queue

# init array to a specific size
def initArray(size):
    return [None for i in range(size)]

ia = initArray

# struct for job result
class JobResult:
    def __init__(s, id, result):
        s.id = id
        s.result = result

def ioPool(func, args):
    return parallelPool(func, args,
                        lambda: queue.Queue(),
                        lambda x,y: threading.Thread(target=x, args=y))

def ioSingle(func, args):
    return parallelPool(func, args,
                        lambda: queue.Queue(),
                        lambda x,y: threading.Thread(target=x, args=y))[0]

def cpuPool(func, args):
    return parallelPool(func, args,
                        lambda: multiprocessing.Queue(),
                        lambda x,y: multiprocessing.Process(target=x, args=y))

# multi process
# func - the function to perform in prallel
# args - the list of args, one for each job, will be passed to the func
# resultGenFunc - ?
# threadGenFunc -?
# returns the results array
def parallelPool(func, args, resultGenFunc, threadGenFunc):
    jobCount = len(args)
    results = resultGenFunc()
    threads = []
    # create all threads and start them
    for i in range(jobCount):
        p = threadGenFunc(func, (i, args[i], results))
        threads.append(p)
        p.start()
    # wait for all threads to complete
    for t in threads:
        t.join()
    resultArray = ia(jobCount)
    for t in threads:
        qresult: JobResult = results.get()
        resultArray[qresult.id] = qresult.result
    return resultArray

# test function for exampleCpuPool() below
def myFunc(index, param, results):
    # do your normal work here, params can be anything
    max = 1_000_000_000
    x = 0
    for _ in range(max):
        x = x + x
    resultOfSomeWork = f'some result for param {param}'
    # the function needs to create a JobResult with the index and send it to the queue
    results.put(JobResult(index, resultOfSomeWork))

# an example calling a threading pool
def exampleCpuPool():
    params = [1, 2, 3, 4, 5, 6, 7 , 8]
    # my function to run in parallel
    resultsArray = cpuPool(myFunc, params)
    for result in resultsArray:
        print(f'{result=}')

exampleCpuPool()