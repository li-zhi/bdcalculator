bdcalculator
===================

BD-rate (Bjontegaard Delta rate) calculator for comparing bitrate-quality performance of codecs.

https://docs.google.com/document/d/17xuKoD-O77b9c5CqYntMBMWEKC0yanTwtCnt8MatAOQ/edit?usp=sharing

# Useful commands

## Run everything

```
tox
```

## Run tests with coverage

```
tox -e python
```

To run a single test (for example):
```
PYTHONPATH=bdcalculator python3 -m unittest test.bdcalculator_test.BDrateCalculatorTest.test_bd_rate_calculator_identical
```

## Run style check only

```
tox -e style
```
