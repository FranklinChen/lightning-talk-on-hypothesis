## Material for lightning talk at [Pittsburgh Python Meetup](http://www.meetup.com/pghpython/)

5-minute lightning talk given on [June 26, 2013](http://www.meetup.com/pghpython/events/120442102)

PDF of slides provided.

### Run

To run the tests, make sure to have a recent version of [pytest](http://pytest.org/) installed.

Then type:

``` console
$ py.test -v
```

### More info

- My [personal blog](http://FranklinChen.com/)
- My programming blog: [The Conscientious Programmer](http://ConscientiousProgrammer.com/)

## A question asked about combining hand-parametrized and hypothesis test

A good question that was asked during the talk was whether you could get the best of both worlds by manually specifying examples as well as let `hypothesis` generate tests, so as to not rely solely on random generation.

The answer is yes, but not in the way that was suggested.

The suggestion was to pile up decorators like this:


``` python
@pytest.mark.parametrize (("x", "y"), [
    (5, 0),
    (6, 1)
])
@given (int, int)
def test_multiply_then_divide_is_same(x, y):
    assert (x * y) / y == x
```

This does not work because decorators in Python are actually mutating operators that replace a function with a wrapped function of the same name. Some decorators that only do simple things may be able to be composed in some fashion, but these testing decorators do major surgery so that the results do not compose.

One solution, if you don't want to duplicate a whole lot of code, is to extract the test and duplicate just calls to the test:

``` python
# A helper not marked as a test in itself
def the_property(x, y):
    assert (x * y) / y == x

@pytest.mark.parametrize (("x", "y"), [
    (5, 0),
    (6, 1)
])
def test_multiply_then_divide_is_same_by_examples(x, y):
    the_property(x, y):
    
@given (int, int)
def test_multiply_then_divide_is_same_by_hypothesis(x, y):
    the_property(x, y):
```

This way, each of the decorators operates on its own copy of the test template.
