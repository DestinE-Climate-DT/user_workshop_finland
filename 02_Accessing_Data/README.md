
## Accessing the data
* demo_scripts contains simple examples to run  for a few key use cases
  * Simple parameter request
  * Limited area request
  * Error on missing data
  * Parallel download
## Excercises: start from the examples and modify for different variables, models, timeframes ... All required information is found in the Climate DT user guide https://platform.destine.eu/services/documents-and-api/doc/?service_name=climate-dt-user-guide
  * Ex1: Explore different ways to handle the data with `earthkit.data` (save to disk, convert to xarray etc.). You can use one of the demo scripts as a starting point.
  * Ex2: Download 'total cloud cover' for IFS-NEMO control experiment 10 June 1996 (hint: polytope server address)
  * Ex3: Download a variable (for example ICON projection, specific humidity) on a pressure level grid for the pressure levels 850,500,200. Select a valid date and time. 
  * Ex4: Download several variables with a single request. Also try parallel requests. Try for example ICON, sfc-level variables 10-meter u-wind, 10 meter v-wind, 2 meter temperature, 2 meter dewpoint 
    temperature (sfc-level recommended to keep the data volume in check)
  * Ex5: make a request for monthly mean 10 m wind speed for ICON from 01/2010 to 06/2010
