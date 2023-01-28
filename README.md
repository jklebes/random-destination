# random-destination
Simply drops a pin N km from your location.  I use this for out-and-back runs.  For exmample, if I want to run 10km, I drop a pin 5km or a bit less away and go there.  

Take a walk.  Explore your neighborhood.  A bit like randonauting, except we don't get special magic quantum random bits piped over from Australia, so your walk will not be haunted.

Command line / very simple / personal use

## Usage:

#### Set and save starting location

(Windows: replace ```python``` with ```python -m``` or ```py -m```)

```python destination.py home "123 Example Street, 18992 Mytown, Germany"``` 

-> Attempts OpenStreetmap address lookup.

If that doesn't work, find our your coordinates (here)[https://gps-coordinates.org/my-location.php] or elsewhere.

```python destination.py home 50.363 2.4848```

#### Generate destination

Destination approximately 5km away.

```python destination.py dest 5```

Destination 5+-.1 km away.

```python destination.py dest 5 .1```

prints out a link to an OpenStreetMap pin to terminal.  It's clickable on my machine.

## Hints

May well drop a pin in a body of water or somewhere else you can't go, just reroll.

Distances are as the crow flies, the actual distance along streets is longer.

## TODO
- Future improvements to distance could be to estimate the average factor or look at actual OpenStreetMap graphhopper path.
- Better parse inputted coordinates, address, or previously saved location.
