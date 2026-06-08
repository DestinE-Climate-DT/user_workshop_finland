import earthkit
import concurrent.futures as cf

address="polytope.lumi.apps.dte.destination-earth.eu"

def make_request(varid):
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
        "param": f"{varid}",
        "levtype": "sfc",
        "date": "20200101",
        "time": "0000"
    }
    return request

def getdata(varid):

    request = make_request(varid)

    data = earthkit.data.from_source(
        "polytope",
        "destination-earth",
        request,
        stream=False,   
        address = address
    )

    return data

GETPARALLEL=True  ### Change here from serial to parallel ###

if GETPARALLEL:
    varlist = ["165","166","167","168"]

    with cf.ThreadPoolExecutor(max_workers=4) as exe:
        futures = [exe.submit(getdata, var) for var in varlist]

    handles = [ff.result() for ff in futures]

else:
    varids = "165/166/167/168"
    handles = getdata(varids)

    











