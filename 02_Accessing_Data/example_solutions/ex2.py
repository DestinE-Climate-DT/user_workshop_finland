

import earthkit

address="polytope.mn5.apps.dte.destination-earth.eu"

request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "experiment": "cont",
    "expver": "0001",
    "generation": "2",
    "model": "ifs-nemo",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "type": "fc",
    "param": "228164",
    "levtype": "sfc",
    "date": "19960610",
    "time": "0000"
}

## Gets data to memory
data = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,   
    address = address
)

print(data.ls())
