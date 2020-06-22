def my_for(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            print("End of iterator")
            break
        else:
            func(thing)

my_for([1,2,3,4], print)