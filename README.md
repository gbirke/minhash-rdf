# Exploration of comparing RDF files with MinHash and different shingling types

This repository contains code that takes DBPedia instance type data, changes it and uses the MinHash algorithm and different partioning strategies to test, which partioning strategy is most suitable for RDF data.

To reproduce the results, run the following commands:

    python prepare_test_data.py test_data/instance_types.ttl
    python prepare_signatures.py
    python compare_signatures.py

The folder `test_data` contains only the first 1000 lines from the DBPedia 2014 "instance types" data set. For a bigger sample you need to replace it.

The results of the signature comparison are stored in a sqlite3 database called "comparison_results.db". The data can be visualized by using the IPython notebook Comparison-Results.ipynb