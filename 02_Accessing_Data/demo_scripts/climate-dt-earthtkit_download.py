
import earthkit

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
    "type": "fc",
}

## Gets data to memory
data = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,    ## stream == true would return an iterator-like object
    address = address
)

## save to file
data.to_target("file","earthkit_test_download.grib")


