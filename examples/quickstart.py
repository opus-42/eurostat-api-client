#!/usr/bin/env python3

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
