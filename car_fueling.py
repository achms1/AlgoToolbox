# python3
import sys
def compute_min_refills(distance, tank, stops):
	refils = 0
	currpos = 0
	nextpos = 0
	stops.append(distance)
	stops.insert(0,0)
	while stops[currpos]+tank<distance:
		currpos=nextpos
		while  nextpos<len(stops)-1 and stops[nextpos+1]<=stops[currpos]+tank :
			nextpos = nextpos+1
		if stops[currpos]+tank<distance:
			refils+=1
		if nextpos==currpos:
			return -1
	return refils
    # write your code here
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
