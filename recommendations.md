# Data Cleaning Recommendations

The BPE dataset is a great source of a wide variety of home sensor data. However, the current dataset is very noisy and needs to be cleanned up in order to explore further into it.

Some of the challenges we faced are:

*	API is not documented so it's not trivial to access to the BPE dataset.
*	2154 out of 2804 reading’s type don’t match with the standards provided in https://github.com/MastodonC/AMON#standard-reading-types
*	Some devices have *Whole House* readings alongside individual readings. Furthermore, the only way to identify *Whole House* readings is by looking at: device description, alias and type or device -> metadata -> placement. For example we found things like: "name:B1_total, site:pp_park_road, Whole house electricity (old id: b4f58930-cdfa-4b9d-b9a3-6bec7331c6ee)"
*	Unit fragmentaion in readings: °C, degreesC, Degrees C, degrees, Degrees, degC.
*	Some of the measurements have crazy values such as temperatures of 5000°C. Maybe the unit is wrong?
*	Some readings have median values but not min or max?
*	Some readings have max but no min or median?
*	Some people might preferred with other storage systems such as: HDFS, Realtional Database, Non-relational database


## What to do?

*	Make all the data available as .csv file so users can use a preferred data storage system.
*	Document the API and give examples of how to use it.
*	Fix all the readings types according the standards specified in https://github.com/MastodonC/AMON#standard-reading
*	Find a better way to display *Whole House* readings alongside individual readings. Maybe there should be a reading type such as: electricityConsumptionWholeHouse.
*	Fix units.
*	Check that the values of the measurements are using the right units.
*	Fix min,max and median issue.