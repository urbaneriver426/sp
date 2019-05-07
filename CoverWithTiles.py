def CoverWithTiles(lenOfRoad):
	if lenOfRoad % 2 > 0:
		result = -1
	else:
		x = lenOfRoad / 2
		result = (((2+3**0.5)**x) / (3-3**0.5)) + (((2-3**0.5)**x) / (3+3**0.5))
		result = round(result)
	return result
