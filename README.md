# random-destination
Simply drops a map pin N km from your location.  I use this to inspire out-and-back runs.  For example, if I want to run 10km, I drop a pin 5km or a bit less away and go there.  

Take a walk.  Explore your neighborhood.  A bit like randonauting, except we don't get special magic quantum random bits piped over from Australia, so your walk will not be haunted.

Command line / very simple / personal use

## Usage:

#### Set and save starting location

(Windows: replace ```python``` with ```python -m``` or ```py -m```)

Find our your coordinates from openstreetmap or elsewhere and set coordinates:

```python destination.py home 50.363 2.4848```

#### Generate destination

Pin at destination approximately 5km away (default precision is +- 0.1 km in Gaussian distribution).

```python destination.py dest 5```

Path to destination approximately 5km away 

```python destination.py path 5```

Pin at destination 5+-2 km away.

```python destination.py dest 5 2```

Path to destination exactly 5 km away.

```python destination.py path 5 0```

prints out a link to the OpenStreetMap in the terminal.  It's clickable on my machine, on windows you may have to copy-paste the link to a browser.

## Hints

May well drop a pin in a body of water or somewhere else you can't go, just reroll.  If requesting a ```path``` and the destination generates in a body of water, it will move the endpoint to the shore and the path will be shorter than expected.

Distances are as the crow flies, the actual distance along streets is longer - so input a number a bit less than half the run distance.

## TODO
- Future improvements to distance could be to estimate the average factor or look at actual OpenStreetMap graphhopper path.
- Better parse inputted coordinates, address, or previously saved location.
