# -*- coding: utf-8 -*-

import codecs
import re
import sys

import urllib.request

def GetSourceFile(url):
  request = urllib.request.Request(url)
  response = urllib.request.urlopen(request)
  return response.read().decode("utf8")

def ExtractItems(raw_data):
  prices = []
  names = []

  patternPrice = re.compile(r'(\<dd class\=\"price\" itemprop=\"price\"\>)(\d+,?\d+)')
  for match in re.findall(patternPrice, raw_data):
    prices.append(int(match[1].replace(',', '')))

  patternName = re.compile(r'(data-toggle=\"modal\" itemprop=\"url\">)([A-Za-zČĆĐŠŽžšđćč ]+)')
  for match in re.findall(patternName, raw_data):
    names.append(match[1])

  return list(zip(prices, names))

assert len(sys.argv) == 4, "Command line arguments are url, price, and range."

initalPrice = int(sys.argv[2])
priceRange = int(sys.argv[3])

items = ExtractItems(GetSourceFile(sys.argv[1]))

combinations = {k:[] for k in range(0, int(sys.argv[2])+1)}
combinations[0] = [[]]

for item in items:
  for price in range(initalPrice, item[0] - 1, -1):
    oldPrice = price - item[0]
    if oldPrice in combinations.keys():
      for combo in combinations[oldPrice]:
        combinations[price].append(combo + [item[1]])

for price in range(initalPrice - priceRange, initalPrice + 1):
  if len(combinations[price]) > 0:
    print (str(price) + ":")
    for solution in combinations[price]:
      print ("    " + str(solution))