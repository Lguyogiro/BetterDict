Mergeable Python dictionary/OrderedDict/defaultdict with arithmetic operator support.
```python
   from BetterDicts import BetterDict, BetterOrderedDict, BetterDefaultDict, merged

   # add values of like keys with `+` operator
   >>> hour1_views = BetterDict({"user1": 4, "user2": 5, "user3": 1})
   >>> hour2_views = BetterDict({"user4": 9, "user2": 2, "user6": 6})
   >>> hour1_views + hour2_views
   {'user1': 4, 'user2': 7, 'user3': 1, 'user4': 9, 'user6': 6}
```
Merge dictionaries with custom logic:

```python
   # in-place
   >>> en = BetterDict({1: "one", 2: "two", 3: "three"})
   >>> es = BetterDict({1: "uno", 2: "dos", 3: "tres"})
   >>> en.merge(es, lambda a, b: [a,b])
   >>> en
   {1: ['one', 'uno'], 2: ['two', 'dos'], 3: ['three', 'tres']}

   # or return a new, merged BetterDict:
   >>> en = BetterDict({1: "one", 2: "two", 3: "three"})
   >>> es = BetterDict({1: "uno", 2: "dos", 3: "tres"})
   >>> merged(en, es, lambda a, b: [a, b])
   {1: ['one', 'uno'], 2: ['two', 'dos'], 3: ['three', 'tres']}
```

You can also perform arithmetic with BetterDicts and scalars:
```python
    >>> raw_counts = BetterDict({'the': 1432, 'she': 600, 'wookie': 25})
    >>> total = 10000.
    >>> relative_freqs = raw_counts / total
    >>> relative_freqs
    {'she': 0.06, 'the': 0.1432, 'wookie': 0.0025}
    >>> relative_freqs * 100
    {'she': 6.0, 'the': 14.32, 'wookie': 0.25}
```
    
