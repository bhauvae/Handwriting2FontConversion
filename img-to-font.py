import potrace
from PIL import Image
import numpy as np
import svgwrite

def raster_to_vector(image_path):
    bmp = Image.open(image_path).convert('1')
    bmp_data = np.array(bmp).astype(np.uint32)
    path = potrace.Bitmap(bmp_data).trace()
    return path

def save_svg(vector_path, svg_path):
    dwg = svgwrite.Drawing(svg_path, profile='tiny')
    for curve in vector_path:
        start_point = curve.start_point
        path_data = f'M {start_point[0]},{start_point[1]}'
        
        for segment in curve:
            if segment.is_corner:
                c1 = segment.c
                c2 = segment.d
                path_data += f' L {c1[0]},{c1[1]} L {c2[0]},{c2[1]}'
            else:
                c1 = segment.c
                c2 = segment.d
                path_data += f' C {c1[0]},{c1[1]} {c2[0]},{c2[1]} {segment.end_point[0]},{segment.end_point[1]}'
        
        path_data += ' Z'
        dwg.add(dwg.path(d=path_data, fill='black'))
    
    dwg.save()

# Example usage
vector_path = raster_to_vector('img to font/a.png')
save_svg(vector_path, 'a.svg')
