

import earthkit

address="polytope.lumi.apps.dte.destination-earth.eu"

request = {
    "activity": "projections",
    "class": "d1",
    "dataset": "climate-dt",
    "experiment": "ssp3-7.0",
    "expver": "0001",
    "generation": "2",
    "model": "icon",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "type": "fc",
    "param": "133",
    "levtype": "pl",
    "level": "850/500/200",
    "date": "20200101",
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
