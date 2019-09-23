# escher2cyjs

escher2cyjs converts [Escher](https://escher.github.io) pathway JSON to Cytoscape.js JSON (.cyjs).

## Installation
```
git clone git://github.com/ecell/escher2cyjs
cd escher2cyjs
python setup.py install
```

## How to use
```
import escher2cyjs as e2c
a = e2c.escher2cyelements("https://raw.githubusercontent.com/escher/community-maps/master/iJO1366/iJO1366.Central%20metabolism.json")
e2c.cyelements2cyjs(a, "e2c.cyjs")
```
