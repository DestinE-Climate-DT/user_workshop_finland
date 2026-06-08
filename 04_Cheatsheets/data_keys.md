# Data Keys

This overview can be found in the Climate DT user guide under "Data and Access" -> "Data Structure and Keys".

Climate DT data stored in the DestinE data bridges and served via the DestinE Platform can be
requested using a combination of keys and values. The table below lists the
available keys and their meaning. Keys are case-insensitive.

| Key | Relevant values | Description |
|-----|-----------------|-------------|
| activity | story-nudging, baseline, projections | The type of activity the simulation corresponds to |
| date | YYYYMMDD (YYYYMMDD/to/YYYYMMDD) | Date or dates for which the data is required (Valid only for clte stream) |
| experiment | cont, hist (baseline or story-nudging), ssp3-7.0 (projections) | Experiment name (in parenthesis, the associated activity related to each experiment) |
| levtype | sfc, pl, o2d, o3d, hl, sol | Level type depends on variable (sfc=surface, pl=pressure levels, o2d=ocean 2D, o3d=ocean 3D, hl=height levels in the atmosphere, sol=soil levels) |
| level | lev1/lev2/lev3 | Present only in the case of levtype=pl, o3d, hl or sol |
| model | ifs-fesom, ifs-nemo, icon | Available models in Climate DT |
| param | paramid (167/235/...) | [ParamID](https://codes.ecmwf.int/grib/param-db/). The correspondence between the param, the long name and the levtype is available in the portfolio documentation |
| realization | 1 or ensemble number | Number of the ensemble member |
| resolution | high or standard | HEALPix resolution: high=closest to the model native resolution (H1024 for 5 km, or H512 for 10 km depending on simulation), standard=interpolated to H128 (~50 km) |
| stream | clte, clmn | clte: Hourly instantaneous or daily mean values, clmn: monthly mean values |
| time | HHMM or HHMM/HHMM/HHMM | Select a specific time (Valid only for clte stream) |
| year | YYYY | To select a specific year (Valid only for the clmn stream) |
| month | MM | To select a specific month (Valid only for the clmn stream) |

The following keys are fixed for all simulations in this documentation:

| Key | Relevant values | Description |
|-----|-----------------|-------------|
| class | d1 | The data originates from Destination Earth |
| dataset | climate-dt | Selects the Climate DT data from Destination Earth |
| expver | 0001 | Experiment version for operational simulations |
| type | fc | All Climate DT data uses type forecast |
| generation | 2 | Climate DT generation |
