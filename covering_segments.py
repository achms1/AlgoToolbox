# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    while (len(segments) > 0):
        maxi = 0
        for s in segments:
            if s.start > maxi:
                maxi = s.start
        points.append(maxi)
        for s in segments[:]:
            if s.start <= maxi and s.end >= maxi:
                segments.remove(s)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
