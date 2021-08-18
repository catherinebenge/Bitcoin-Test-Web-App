import pandas as pd

## for my data scrubbing I used the pandas module

# reading orginal data set from file path
og_data = pd.read_csv('data/bitcoin.csv')

# creating a list of only the field I need
field_filter = ['date', 'symbol','open', 'high', 'low', 'close', 'Volume BTC', 'Volume USD']

# filtering data set
data = og_data[field_filter]

# split date
data['date'] = pd.to_datetime(data['date']).dt.date

# creating new data set after scrubbing complete
data.to_csv('data/bitcoin_clean.csv', index = False, header=True)

