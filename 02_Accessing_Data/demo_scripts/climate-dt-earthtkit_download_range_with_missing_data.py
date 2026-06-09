
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
    "stream": "clte",
    "type": "fc",
    "param": "167",
    "levtype": "sfc",
    "date": "20141231/to/20150101",  ## this will fail
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




