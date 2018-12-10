from Zoom import largeMap
from mymap import Map

def createBasicLargeMap():
    size = 100
    half_size = int(10/2)
    large_map = largeMap(size, size, "data/large_basic_map.txt")
    large_map.draw((0,0), (size-1,0), Map.mark_target)
    large_map.draw((0,1), (size-1,1), Map.mark_target)
    large_map.draw((0,2), (half_size-1,2), Map.mark_wall)
    large_map.draw((half_size+1,2), (size-1,2), Map.mark_wall)
    large_map.draw((0,3), (0,size-1), Map.mark_wall)
    large_map.draw((size-1,3), (size-1,size-1), Map.mark_wall)
    large_map.draw((0,size-1), (size-1,size-1), Map.mark_wall)
    large_map.output()

if __name__ == "__main__":
    createBasicLargeMap()