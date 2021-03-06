import sys
import random
import svgwrite
from svgwrite.container import Hyperlink


## predefined constants
ration_text_width = round(130/7, 2)
all_text_y = 39
primary_text_bg='#5E6772'
primary_text='vikbert'
primary_text_x = 15 # X-Value of primary text
primary_text_width = 30 + int(len(primary_text) * ration_text_width) # X-value of primary text bg


def add_bg_mask(dwg, radius, container_width, container_height):
    mask_element= dwg.mask((0, 0), (container_width, container_height), id='a')
    mask_element.add(dwg.rect((0, 0), (container_width, container_height), fill='#eee', rx=5))
    dwg.add(mask_element)
    return dwg

def set_watermark_to_secondary(dwg, group, hex_color):
    def get_some_random10(num):
        results = ''
        for x in range(1, num):
            results += str(random.getrandbits(1))
        return results

    for x in range(0, 100, 5):
        text = get_some_random10(100)
        group.add(
            dwg.text(text, insert=(primary_text_width + 1, x), fill='#eee', font_size=4,
                     font_family='Inconsolata for Powerline',
                     opacity=0.3, transform="rotate(15 300, 0)"))

    return group

def add_text_with_shadow(dwg, text, x, y):
    # create a container element(shapes) for grouping together related graphics elements.
    # shapes will group together the two text elements
    shapes = dwg.g(id='shapes', fill='none')
    shapes.add(dwg.text(text, insert=(x + 1, y + 1), fill='#000', font_size=40, font_family='Helvetica', fill_opacity=0.3))
    shapes.add(dwg.text(text, insert=(x, y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    dwg.add(shapes)

    return dwg

def add_bg_watermark(dwg, container_width, container_height, secondary_text_bg):
    group = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    # draw secondary backgroud color
    group.add(dwg.rect((primary_text_width, 0), (container_width - primary_text_width, container_height), fill=secondary_text_bg))
    # draw secondary backgroun watermark
    group = set_watermark_to_secondary(dwg, group, secondary_text_bg)
    # draw primary background color
    group.add(dwg.rect((0, 0), (primary_text_width, container_height), fill=primary_text_bg))
    dwg.add(group)

    return dwg


def generate(secondary_text):
    secondary_text_x = primary_text_width + 15

    secondary_text_bg = '#2196F3'
    container_width = 80 + int(len(secondary_text+primary_text) * ration_text_width)
    container_height = 50

    dwg = svgwrite.Drawing('shields/'+secondary_text +'.svg', profile='full', size=(u'100%', u'100%'))

    # draw the background with round border
    dwg = add_bg_mask(dwg, 5, container_width, container_height)
    dwg = add_bg_watermark(dwg, container_width, container_height, secondary_text_bg)
    dwg = add_text_with_shadow(dwg, primary_text, primary_text_x, all_text_y)
    dwg = add_text_with_shadow(dwg, secondary_text, secondary_text_x, all_text_y)
    dwg.save()

generate('Design')
generate('Mobile')
generate('Coding')