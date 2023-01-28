# random-destination
Simply drops a pin N km from your location.  I use this for out-and-back runs.  For exmample, if I want to run 10km, I drop a pin 5km or a bit less away and go there.  

Take a walk.  Explore your neighborhood.  A bit like randonauting, except we don't get special magic quantum random bits piped over from Australia, so your walk will not be haunted.

Command line / very simple / personal use

## Usage:

Set home

```python destination.py home 50.363 2.4848```

Generate destination

```python destination.py goal 5```, 

prints out a link to an OpenStreetMap pin to terminal.  It's clickable on my machine.

## Hints

May well drop a pin in a body of water or somewhere else you can't go, just reroll.

Distances are as the crow flies, the actual distance along streets is longer.

## TODO
- Future improvements to dostance could be to estimate the average factor or look at actual OpenStreetMap graphhopper path.
- Better parse inputted coordinates, address, or previously saved location.
