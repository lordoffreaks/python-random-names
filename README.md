# Random Names

## Objetive
This is a pair programming exercise and the objective is to understand how you think, plan and structure as well as your problem solving skills, don't worry if you have some sintax mistakes or you end up with some broken test, make sure you communicate what you have in mind and don't hesitate to ask or share your thoughts about how/what would you do improve if you had some extra time.

## Instructions
We want to implement a function that given a file with a list of names and a number ``n``, will return a list with ``n`` randomly selected names from that names file, to achieve this you will need to implement the ``random_names`` function in the ``names.py`` script.
The format of the names data in the ``names.txt`` file is consists in a name and number of occurrences.
```bash
Richard 2467544
Joseph 2352889
Thomas 2160330
```

You have a number of tests to check that your function implements the requirements.
To run the test execute the following command from the ``random-names`` directory:
```bash
python tests.py
```

## Requirements
Implement the ``random_names`` function defined in names.txt
1. Returns a list of ``n`` random names, i.e: with ``n=3`` return ``["Richard", "Joseph", "Thomas"]``
1. Do not include blank names or new line characters
1. Do not include invalid names like digits
1. Do not include duplicates
1. If there is not enough valid names in the data file raise a ``ValueError``
1. Descending order by number of occurences
