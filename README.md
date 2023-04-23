
# Benford app

It uses benford law to check whether the digits are complying it or not.




## Overview
Benford's Law is a mathematical phenomenon that describes the frequency distribution of the first digit in many naturally occurring datasets. The law states that in many naturally occurring datasets, the first digit is more likely to be a small number, such as 1, 2 or 3, rather than a larger number, such as 8 or 9.

For example, if you look at the population of all countries in the world, you would expect the first digit of the population numbers to follow Benford's Law. This means that you would expect to see a lot of population numbers starting with 1, fewer numbers starting with 2, even fewer starting with 3, and so on, with very few starting with 8 or 9.

The law is named after American physicist Frank Benford, who first described the phenomenon in 1938. Benford's Law is used in various fields, such as forensic accounting and auditing, to detect anomalies in data and identify potential fraud or errors.


## How to Use

Install the dependencies

```bash
  pip install pyramid
```

Create or download a csv file of 10k+ words in root directory of project
and run
```bash
  python app.py
```

Open `index.html` and upload the csv. Then click on `check` the result is given in `json` format.

    
## Screenshots

![Screenshot]()

