import functools
import operator

a = [1,2,3,4,5]


"""
to add python interpreter

https://stackoverflow.com/questions/24769117/how-do-i-configure-a-python-interpreter-in-intellij-idea-with-the-pycharm-plugin

"""


# add using reduce
print(functools.reduce(operator.add,a));


#multiply using reduce
print(functools.reduce(operator.mul, a));

#concatenate string
print(functools.reduce(operator.add, ["Kumar ", "Vaduganthan"]))