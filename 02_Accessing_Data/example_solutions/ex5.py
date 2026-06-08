

import earthkit

address="polytope.lumi.apps.dte.destination-earth.eu"

request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "model": "icon",
    "realization": "1",
    "resolution": "high",
    "stream": "clmn",
    "type": "fc",
    "param": "228005",
    "levtype": "sfc",
    #"date": "20100102",  ## Not valid with stream clmn
    #"time": "0000"       ## Not valid with stream clmn
    "year": "2010",       ## Required with stream clmn
    "month": "1/2/3/4/5/6"          ## Required with stream clmn
}

## Gets data to memory
data = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,    ## stream == true would return an iterator-like object
    address = address
)

data.ls()
