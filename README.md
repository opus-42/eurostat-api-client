# Eurostat API Client (Python)

Use the Eurostat API Client to quickly retrieve json data from Eurostat REST service and convert it to a pandas DataFrame. A simple description of the service can be found [here](https://wikis.ec.europa.eu/display/EUROSTATHELP/API+Statistics+-+data+query)

## Installation

Install Eurostat API Client using pip.

```bash
pip install eurostatapiclient
```

## Quick start

This example shows how to retrieve a dataset and a pandas dataframe from it.

```python
from eurostatapiclient import EurostatAPIClient

# Choose service version : only 1.0 is currently available
VERSION = '1.0'

# Only json is currently available
FORMAT = 'json'

# Specify language : en, fr, de
LANGUAGE = 'en'

client = EurostatAPIClient(VERSION, FORMAT, LANGUAGE)

# Optionnal : working behing a proxy :
# client.set_proxy({'http':'my.proxy.com/8080', 'https':'my.proxy.com/8080'})

dataset = client.get_dataset('tps00001')
print(dataset.label)

dataframe = dataset.to_dataframe()
print(dataframe.head())

# Add some filters (only mono-filtering is available for now)
params = {
    'geo': 'DE',
}

# Note that some keys may be repeated in eurostat's api
# In that case, you will want to pass params as a list of tuples
# ex. : 
# params = [
#  ('siec', 'TOTAL'),
#  ('precision', '1'),
#  ('unit', 'KTOE'),
#  ('nrg_bal', 'AFC'),
#  ('nrg_bal', 'DL'),
#  ('nrg_bal', 'EXP'),
#  ('nrg_bal', 'FC_E'),
#  ('nrg_bal', 'FEC2020-2030')]
# filtered_dataset = client.get_dataset('nrg_bal_c', params=params)

filtered_dataset = client.get_dataset('tps00001', params=params)
filtered_dataframe = filtered_dataset.to_dataframe()
print(filtered_dataframe.head())
```

## Contributions

Contributions are welcome !

Feel free to suggest modifications/enhancements in the "issues" section, or to create a pull request
