# Eurostat API Client (Python)

Use the Eurostat API Client to quickly retrieve json data from Eurostat REST service and convert it to a pandas DataFrame. A simple description of the service can be found [here](https://ec.europa.eu/eurostat/web/json-and-unicode-web-services/about-this-service)

## Installation

Install Eurostat API Client using pip.

```bash
pip install eurostatapiclient
```

## Quick start

This example shows how to retrieve a dataset and a pandas dataframe from it.

```python
from eurostatapiclient import EurostatAPIClient

# Choose service version : only v2.1 is currently available
VERSION = 'v2.1'

# Only json is currently available
FORMAT = 'json'

# Specify language : en, fr, de
LANGUAGE = 'en'

client = EurostatAPIClient(VERSION, FORMAT, LANGUAGE)
dataset = client.get_dataset('tps00001')
print(dataset.label)

dataframe = dataset.to_dataframe()
print(dataframe.head())

# Add some filters (only mono-filtering is available for now)
params = {
    'geo': 'DE',
}
filtered_dataset = client.get_dataset('tps00001', params=params)
filtered_dataframe = filtered_dataset.to_dataframe()
print(filtered_dataframe.head())
```

## Contributions

Contributions are welcome !

Feel free to suggest modifications/enhancements in the "issues" section, or to create a pull request
