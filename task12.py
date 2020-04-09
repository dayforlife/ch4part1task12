def MyDecorator(func):
    def wrapper(a, b=1, *args, **kwargs):
        print("argument a: ", a)
        print("argument b: ", b)
        print("argument args: ", args)
        print("argument kwargs: ", *kwargs.values())
        return a + b
    return wrapper

@MyDecorator
def function(a, b=1, *args, **kwargs):
    print('This is my Function')

function(2,3,4,5,c=6, d=7)