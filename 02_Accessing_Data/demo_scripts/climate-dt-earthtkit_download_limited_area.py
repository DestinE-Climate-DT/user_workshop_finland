
import earthkit.data

address="polytope.lumi.apps.dte.destination-earth.eu"

request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "model": "ifs-fesom",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "type": "fc",
    "param": "167",
    "levtype": "sfc",
    "date": "20100102",
    "time": "0000"
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
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "model": "ifs-fesom",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "type": "fc",
    "param": "167",
    "levtype": "sfc",
    "date": "20100102",
    "time": "0000",
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


