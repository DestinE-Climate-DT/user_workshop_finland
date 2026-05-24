
import earthkit.data
import numpy as np

address="polytope.lumi.apps.dte.destination-earth.eu"



request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "date": "20100102",
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "levtype": "sfc",
    "model": "ifs-fesom",
    "param": "167",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "time": "0000",
    "type": "fc"
}

## Gets data to memory
data_full = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,   
    address = address
)



request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "date": "20100102",
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "levtype": "sfc",
    "model": "ifs-fesom",
    "param": "167",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "time": "0000",
    "type": "fc",
    "feature": {
        "type": "boundingbox",
        "points" : [[53.55, 2.76], [50.66, 7.86]]
    }
}

## Gets data to memory
data_bbox = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,    
    address = address
)

xfull = data_full.to_xarray()

xbbox = data_bbox.to_xarray()

print(f"\n full field:\n {'-' * 15}\n {xfull} \n")

print(f"Bounding box:\n {'-' * 15}\n {xbbox} \n")


