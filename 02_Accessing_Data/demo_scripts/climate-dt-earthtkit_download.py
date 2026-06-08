
import earthkit

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
data = earthkit.data.from_source(
    "polytope",
    "destination-earth",
    request,
    stream=False,   t
    address = address
)

## save to file
data.to_target("file","earthkit_test_download.grib")


