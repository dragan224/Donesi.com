# Donesi.com
## Donesi.py

A python3 script that takes (url of donesi restaurant, price, range) as arguments and prints out all meal combos with the cost in the range [price-range, price].

Example usage:
  python3 donesi.py https://www.donesi.com/beograd/lat/pizzahaos-dostava-147.php 300 10 

Output:
290:
    ['Sendvič šunka', 'Sendvič pečenica']
    ['Sendvič šunka', 'Sendvič suvi vrat']
    ['Grčka salata']
    ['Kupus salata', 'Palačinka sa šunkom']
    ['Dodatak pomfrit', 'Palačinka sa eurokremom']
    ['Paradajz salata', 'Palačinka sa eurokremom']
    ['Sendvič pečenica', 'Palačinka sa pudingom']
    ['Sendvič suvi vrat', 'Palačinka sa pudingom']
    ['Sendvič pečenica', 'Palačinka sa karamelom']
    ['Sendvič suvi vrat', 'Palačinka sa karamelom']
    ['Sendvič pečenica', 'Palačinka sa jagodom']
    ['Sendvič suvi vrat', 'Palačinka sa jagodom']
    ['Sendvič pečenica', 'Palačinka sa čokoladom']
    ['Sendvič suvi vrat', 'Palačinka sa čokoladom']
    ['Palačinka sa eurokremom', 'Palačinka sa nutelom']
300:
    ['Margarita']
    ['Sendvič pršuta klasik']
    ['Dodatak pomfrit', 'Paradajz salata']
    ['Sendvič šunka', 'Palačinka sa šunkom']
    ['Sendvič pečenica', 'Palačinka sa eurokremom']
    ['Sendvič suvi vrat', 'Palačinka sa eurokremom']
    ['Palačinka sa šunkom', 'Palačinka sa pudingom']
    ['Palačinka sa šunkom', 'Palačinka sa karamelom']
    ['Palačinka sa šunkom', 'Palačinka sa jagodom']
    ['Palačinka sa šunkom', 'Palačinka sa čokoladom']
    ['Dodatak pomfrit', 'Palačinka sa nutelom']
    ['Paradajz salata', 'Palačinka sa nutelom']
