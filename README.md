bdcalculator
===================

BD-rate (Bjontegaard Delta rate) calculator for comparing bitrate-quality performance of codecs.

https://docs.google.com/document/d/17xuKoD-O77b9c5CqYntMBMWEKC0yanTwtCnt8MatAOQ/edit?usp=sharing

# Run tests

```
PYTHONPATH=bdcalculator python3 -m unittest discover --start test \
    --pattern '*_test.py' --verbose --buffer
```

# Run style check

```
python3 -m flake8 bdcalculator test
```
