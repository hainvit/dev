'''function in python
'''

print('=== function in python ===')


def func_args(*args):
    print('* function *args')
    for x in args:
        print(x)


def func_kwargs(**kwargs):
    print('* function **kwargs')
    print('kwargs[name]', kwargs['name'])


func_args('hainv', '23')
func_kwargs(name="Tobias", lname="Refsnes")

print('=== lambda functions ===')