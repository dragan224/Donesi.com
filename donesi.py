# -*- coding: utf-8 -*-

import codecs
import re
import sys

import urllib.request

def GetSourceFile(url):
  request = urllib.request.Request(url)
  response = urllib.request.urlopen(request)
  return response.read().decode("utf8").split("<h3>Pića</h3>")[0].split("<h3>Piće</h3>")[0]

def ExtractItems(raw_data):
  prices = []
  names = []

  patternPrice = re.compile(r'(\<dd class\=\"price\" itemprop=\"price\"\>)(\d+,?\d+)')

  for match in re.findall(patternPrice, raw_data):
    # print (match)
    prices.append(int(match[1].replace(',', '')))

  if not prices:
    patternPrice2 = re.compile(r'(content=\")(\d+,?\d+)([A-Za-z0-9\.\+ ]*\" itemprop=\"price\")')
    for match in re.findall(patternPrice2, raw_data):
      # print (match)
      prices.append(int(match[1].replace(',', '')))

  patternName = re.compile(r'(.php\"[ ]*itemprop=\"url\">)([A-Za-zČĆĐŠŽžšđćč0-9,\.\!\?\"\'\- ]+)')
  for match in re.findall(patternName, raw_data):
    # print (match)
    names.append(match[1])

  if not names:
    patternName2 = re.compile(r'(modal\"[ ]*itemprop=\"url\">)([A-Za-zČĆĐŠŽžšđćč0-9,\.\!\?\"\'\- ]+)')
    for match in re.findall(patternName2, raw_data):
      # print (match)
      names.append(match[1])

  return list(zip(prices, names))

def safeprint(s):
  try:
    print(s)
  except UnicodeEncodeError:
    if sys.version_info >= (3,):
      print(s.encode('utf8').decode(sys.stdout.encoding))
    else:
      print(s.encode('utf8'))

if __name__== "__main__":
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

  for price in range(max(1, initalPrice - priceRange), initalPrice + 1):
    if len(combinations[price]) > 0:
      safeprint (str(price) + ":")
      for solution in combinations[price]:
        safeprint ("    " + str(solution))
