# Scheme interpreter in Python

## About
This interpreter is based on the Simply Scheme implementation of the Scheme language. User interaction is provided using a read-eval-print loop([REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)), which receives user input and returns the output on the screen.


## Installation and usage
1. Get a copy of this project by using `git clone https://github.com/lucaskenji/scheme-python`.
2. With Python already installed on your machine, run `python scheme.py` inside the cloned folder.
3. Optionally, [activate](https://virtualenv.pypa.io/en/latest/user_guide.html#activators) the virtual environment and run `pytest` to run the unit tests.


## Example
```
> (+ 1 2)
3
> (+ (* 2 5) 10)
20
> (word 'foo 'bar)
foobar
```
* To see a list of all available primitive procedures, check primitives.py