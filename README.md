# Python Package Template
A step-by-step introduction to python packaging

To see what happend between steps, you can do
```
git diff step2 step1
```


### Step 1 – Share your code
Add one of your many python scripts, that somebody asked you for.

> Hey this is cool stuff, i also need to do this often. Why don't you share it?

In this example, I will use a simplistic json to yaml converter.

Repository after [step 1](https://github.com/MaxNoe/python_package_template/tree/step1)
### Step 2 – Create an installable python package

Make it an installable python package, so people can do:

```
pip install git+https://github.com/<myuser>/<mypackage>
```

This is mostly explained here: https://packaging.python.org/distributing

Repository after [step 2](https://github.com/MaxNoe/python_package_template/tree/step2)

### Step 3 – Unit tests

Add unit tests.

We are using the now standard [pytest](http://doc.pytest.org/en/latest/).

You should also read http://doc.pytest.org/en/latest/goodpractices.html

Repository after [step 3](https://github.com/MaxNoe/python_package_template/tree/step3)

### Step 4 – Continous Integration

Setup travis

### Step 5 – Proper documentation

Setup sphinx

### Step 6 – Publish

Deploy to (test)-PyPI using travis
