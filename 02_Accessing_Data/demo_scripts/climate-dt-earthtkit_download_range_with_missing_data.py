
import earthkit
import numpy as np


address="polytope.lumi.apps.dte.destination-earth.eu"



request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "date": "20141231/to/20150101",   ## This will fail
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "levtype": "sfc",
    "model": "icon",
    "param": "167",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "time": "0000",
    "type": "fc",
}

## Gets data to memory
data = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,   
    address = address
)




