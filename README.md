# Surfs_Up

## Project Overview
The purpose of this analysis was to analyze temperature trends in Oahu in June and December in order to determine if a surf and ice cream shop business is sustainable year-round.

## Resources
- Data Source: hawaii.sqlite
- Software: Visual Studio Code 1.60.1

## Results
- The summary statistics for June are shown in the following table:

![image_name](https://github.com/zackzydonik/surfs_up/blob/b39c448d8cb5e194913fca735966410065667717/June%20Temps.png)

- The summary statistics for December are shown in the following table:

![image_name](https://github.com/zackzydonik/surfs_up/blob/b39c448d8cb5e194913fca735966410065667717/December%20Temps.png)

- The average temperatures for June and December are 74.9 °F and 71.0 °F, respectively.

## Summary
The average temperature is higher in June than in December. The range in temperatures in December is consistently colder than in June; however the minimum temperature never drops below 56 °F, which is not too cold for ice cream consumption - at least in my opinion. While the shop will liekly perform better in the month of June, the data suggests that the shop should be sustainable year-round when considering temperature.

Two additional queries to gather more weather data for June and December are as follows:

        session.query(Measurement.date, Measurement.prcp).\
        filter(extract('month', Measurement.date) == 6).all()

        session.query(Measurement.date, Measurement.prcp).\
        filter(extract('month', Measurement.date) == 12).all()