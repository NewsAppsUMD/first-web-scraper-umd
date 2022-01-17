# First web scraper

A step-by-step guide to writing a web scraper with Python.

* Documentation: [first-web-scraper-umd.rtfd.org](https://first-web-scraper-umd.readthedocs.io/en/latest/)

### Contributing to the documentation

After installing the repository, the Sphinx documentation can be edited in the
``docs`` directory and published to ReadTheDocs by pushing changes to the ``master`` branch.

First install the requirements.

```bash
$ pipenv install
```

Fire up the test server, which will automatically update to show changes made
to the restructured text files in the ``docs`` directory.

```bash
$ make docs
```

Open ``http://localhost:8000`` in your browser and start making changes.
