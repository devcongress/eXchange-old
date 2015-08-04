## The #eXchange series

`#eXchange` is a monthly remote Google Hangouts session with the most
proactive and pragmatic of software engineers, designers, and copywriters in
Ghana. It's run in the format of any programming podcast you've listened: a
guest who tells his story, patiently answers questions from everyone part of
the discussion, and then we have a nice time together. Want to join any ***#eXchange*** session? Register for all so you get automatically invited to every episode or register on a per episode basis. (Protip: Register once and for
all.)

Got something to #eXchange? [Volunteer as a guest or recommend somebody else](http://exchange.devcongress.com/guests/new). We'd contact you.
immediately.

## Contributing to #eXchange

All forms of contributions are welcome. Improvement of the Python (Flask) code, UI, etc.

### Setup Requirements
- [Python 2.7][Python]
- [Flask][], a Python microframework.
- [PostgreSQL][]

There's awesome setup guides for both technologies on their respective homepages. You'd need [pip][] to install Flask. If you don't have plans to use [Flask][] for any more projects (even though we recommend you to give it a really good shot), setup your virtual environment first.

### Setting up a Python virtual environment (`venv`)
Again, another [wonderful guide](http://www.virtualenv.org/en/latest/) by the project's authors. That should be good. The requirements for the virtual env are:
- It should use Python 2.7.x
- You should name it `venv`. If you name it otherwise please make sure to update
  `.gitignore` with that name.


### Activating #eXchange's `venv` and installing required packages

(Can someone contribute the Windows way? Thanks.)

For \*nix machines. It's as straightforward as:

    $ source venv/bin/activate

Your prompt text should be prefixed with `(venv)` (or whatever name you chose). Go ahead and install the required packages:

    (venv) $ pip install -r requirements.txt


### Running the migrations on your database

Set `EXCHANGE_DATABASE_URL` to your database URL. The URL should have the form:
`postgres://username:password@database_server:port/database_name`. The user (or role)
used should have the right permissions on the database.

Then run the following commands:

    (venv) $ python manage.py db init
    (venv) $ python manage.py db upgrade

Make sure the current command succeeds before moving on to the next.

### Starting the server

    (venv) $ python home.py



By now you have a working application you're set to submit your [pull requests][PR]. Otherwise [submit an issue][GI].

We'd provide a guide on how to do PRs properly if the need arises.




[Flask]: http://flask.pocoo.org
[PostgreSQL]: https://www.postgresql.org
[pip]: https://pypi.python.org/pypi/pip
[Python]: https://www.python.org/download/releases/2.7
[GI]: https://github.com/devcongress/exchange/issues
[PR]: https://github.com/devcongress/eXchange/pulls
