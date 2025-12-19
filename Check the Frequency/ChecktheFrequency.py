from collections import Counter
data_dict = {
    'item1': 'apple'
    'item2': 'banana',
    'item3': 'apple',
    'item4': 'orange',
    'item5': 'banana',
    'item6': 'apple'
}
value_counts = Counter(data_dict.values())
print('Frequency of 'apple' using Counter: ', {value_counts['apple']})