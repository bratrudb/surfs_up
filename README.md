# surfs_up

## Overview of the Analysis
The purpose of this analysis was to analyze Hawaii temperature and precipitation data over time using SQLalchemy and Python to determine the prospect of opening a surf and ice cream shop on the island of Oahu.

## Results
  - The mean temperature on Oahu is almost 4 degrees higher in June than in December.
  - As we see in the descriptive statistics below, the standard deviation of temperatures is higher in December than in June. This shows that temperatures are more varied in December than in June.
  - The minimum temperature in December is 8 degrees lower than in June.

![June Descriptive Statistics](https://user-images.githubusercontent.com/90737940/142348882-82e329d1-950d-49ce-bb03-4fb23d25b7b3.png)
![December Descriptive Statistics](https://user-images.githubusercontent.com/90737940/142348887-f50c788c-016a-4e3f-ad5e-1a72c233e7c4.png)

## Summary
Overall we can conclude that temperatures in Hawaii are fairly stable year round with only an eight degree difference in minimum temperatures in June and December and a 2 degree difference in maximum temperatures in June and December. While temperatures may be fairly stable, there are additional analysis that should be performed to determine the impacts of weather.
  - One additional query would be to run the same analysis we did above on temperature for the precipitation data. The level of rainfall in different seasons would play just as important of a role in determining good weather days as the temperature data.
  - Another query that would be helpful is running descriptive statistics on both temperature and rainfail across different weather stations. While Oahu is a small area land-wise, the weather can vary significantly on different parts of the island. It could be helpful to compare weather data across different parts of the island to determine if one spot would be better for opening a surf and ice cream shop than another.
