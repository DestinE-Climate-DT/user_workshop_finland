# Important commands

Here is an overview of some commands that return repeatedly.

Convert earthkit object to xarray: `ds = data.to_xarray()`.

Download data with earthkit: `earthkit.data.from_source("polytope", "destination-earth", request, address="polytope.<machine>.apps.dte.destination-earth.eu", stream=False)` with `machine=lumi,mn5`.

Choosing a specific area:
```python
request = request | {
    "feature": {
        "type": "boundingbox",
        "points" : [[59, 19], [71, 32]],
    },
}
```
