import math 
import xml.etree.ElementTree as ET

def circle_to_point(circle):
    return (float(circle.attrib['cx']),
            float(circle.attrib['cy']))

def get_points_from_svg(svg_file_name):
    tree = ET.parse(svg_file_name)
    return [circle_to_point(circle)
     for circle in tree.iter('{http://www.w3.org/2000/svg}circle')]

def distance(point1, point2):
	x1, y1 = point1
	x2, y2 = point2

	dx = x1 - x2
	dy = y1 - y2

	return math.sqrt(dx * dx + dy * dy)

def closest_point(all_points, new_point):
    best_point = None
    best_distance = None

    for current_point in all_points:
        current_distance = distance(new_point, current_point)

        if best_distance is None or current_distance < best_distance:
            best_distance = current_distance
            best_point = current_point
    
    return best_point
