Python & Spreadsheets: VancHouVer Edition
------------------------------------------
I'll be presenting this talk at `PyCascades <https://www.pycascades.com/schedule/>`_. I also presented this at the `2017-12 PyHouston meetup <https://www.meetup.com/python-14/events/drtltlywqbzb/>`_.

NOTE 2017-12-21T11:27:14-06:00
===============================
THIS REPO WILL CHANGE!

I first presented *this* version of the talk at the PyHouston meetup on 20112-12-19. I'm presenting it again at PyCascades 2018 on 2018-01-23. I'll be making adjustments/updates between those dates, so if you first saw this talk in Houston, don't be shocked by changes. These changes may or may not include "Canadaianizing" the data set.

I don't know exactly what "Canadaianizing" means, as I just made that word up AS I TYPED IT in the prior sentence. I apologize for any confusion. Just know that I'm confused too. 😮 😁

As of 2018-02-23, the ``master`` branch is the one that works. Focus on the Key Files below. While they are still a bit of a hot mess, the other files are a HOTTER mess. So, there's that. But, the key files function.

Key Files
==========
-  ``headcount_summary.xlsx``: The primary input file
-  ``functional_sheets.py``: The primary code file. It transforms the primary input into the primary output.
-  ``headcount_by_function.xlsx``: The primary output file.
-  ``costCenter_Function_map.json``: The mapping of cost centers to Functional Groups they're part of.
-  ``pycascades_2018.key``: the slides from PyCascades 2018

Note that a BUNCH of these names are TERRIBLE (they're from 2013, sorry) and I'll probably change them. They NEED changing.

Running
========
1. Create a virtual environment with the tool of you choice. I use `virtualenvwrapper <http://virtualenvwrapper.readthedocs.io/en/latest/>`_, but there are other tools. I should probably change to `pipenv <https://docs.pipenv.org/>`_, but I haven't figured it out yet.
	- Virtual environments are a good practice and you should use them all the time. I'll go into that in more detail in another talk at 
	- If you've got another way to handle dependencies (Docker container, etc), use that.
	- This is Python 3 code (adapted from old, bad, Python 2 code). I've run this with Python 3.5.1 and 3.6.2
2. From inside that virtual environment: 
	-  ``pip install -r requirements.txt`` (OpenPyXL is the only dependency)
	-  ``python functional_sheets.py``



