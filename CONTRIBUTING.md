###Contributing to #eXchange

All forms of contributions are welcome. Improvement of the Python (Flask) code, UI, etc.

###Setup Requirements
- [Python 2.7][Python]
- [Flask][], a Python microframework.
- [MongoDB][] (I know it's a bad choice, I know.)

There's awesome setup guides for both technologies on their respective homepages. You'd need [pip][] to install Flask. If you don't have plans to use [Flask][] for any more projects (even though I recommend you to give it a really good shot), setup your virtual environment first.

###Setting up a Python virtual environment (venv)
Again another [wonderful guide](http://www.virtualenv.org/en/latest/) by the project's authors. That should be good.


###Activating #eXchange's venv and installing required modules
(Someone should contribute the Windows way.)
For \*nix machines. It's as straight-forward as:

    $ source venv/bin/activate
    $ pip install -r requirements.txt

To run the server: `$ python home.py`

You're set to submit those [PRs](https://github.com/devcongress/eXchange/pulls).

I'd provide a guide on how to do PRs properly if the need arises.

[Flask]: http://flask.pocoo.org
[MongoDB]: https://www.mongodb.org
[pip]: https://pypi.python.org/pypi/pip
[Python]: https://www.python.org/download/releases/2.7
