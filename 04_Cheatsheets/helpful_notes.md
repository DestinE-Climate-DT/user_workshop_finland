# Helpful Notes

## Commands

Here is an overview of some commands that return repeatedly.

Convert earthkit object to xarray: `ds = data.to_xarray()`.

Download data with earthkit:   
```python
data = earthkit.data.from_source("polytope", "destination-earth", request, address="polytope.<machine>.apps.dte.destination-earth.eu", stream=False)
```
with `machine=lumi,mn5`.

Choosing a specific area:
```python
request = request | {
    "feature": {
        "type": "boundingbox",
        "points" : [[59, 19], [71, 32]],
    },
}
```
## Data Bridges

| Data Bridge | Address |
| -------- | ---------------------------------------------- |
| LUMI | `polytope.lumi.apps.dte.destination-earth.eu` |
| Marenostrum5 | `polytope.mn5.apps.dte.destination-earth.eu` |

LUMI: All ICON runs, IFS-FESOM multi-decadal runs   
MN5: All IFS-NEMO runs, IFS-FESOM storyline runs

## Links
- [Large collection of Polytope and other examples](https://github.com/destination-earth-digital-twins/polytope-examples)
- [Polytope documentation](https://polytope.readthedocs.io/en/stable/)
- [EArthkit documentation](https://earthkit.readthedocs.io/en/stable/)
- [Destination Earth Service Platform](https://platform.destine.eu/)
- [Climate DT user guide](https://platform.destine.eu/services/documents-and-api/doc/?service_name=climate-dt-user-guide)
- [Insula code](https://platform.destine.eu/services/service/insula-code/)
- [Climate DT community resources](https://github.com/DestinE-Climate-DT/climatedt-community-resources)