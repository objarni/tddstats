![image](https://user-images.githubusercontent.com/68198/126142048-c5cd0b65-4c6d-481b-9e21-abd920852cc2.png)


# tddstats

Monitor your TDD practice and understand where you spend most (and least) time!


# Explanation

I wanted to explore how much time I spend in the different 'modes/states' of Test-Driven Development (TDD); see [this twitter thread](https://twitter.com/olofb/status/1409051072182865920) for more info!

# How to install?

This is a POC written i Python3; it has some dependencies, set it up like this:

   - clone this repo
   - make a virtual env, e.g `python3 -m venv venv`
   - install dependencies: e.g `./venv/bin/pip install -r requirements.txt`


# How to run?

    ./venv/bin/python tddstats.py
  
.. then follow instructions!


# How to run tests?

Use pytest:

    ./venv/bin/pytest
