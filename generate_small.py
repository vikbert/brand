import random

import svgwrite
from svgwrite.container import Hyperlink

phodal_width = 176
secondary_text_x = 200
basic_text_y = 35
author='vikbert'


def generate_idea():
    y_text_split = phodal_width + 1
    height = 50
    rect_length = 2
    width = 290
    max_rect_length = 10

    dwg = svgwrite.Drawing('shields/idea-small.svg', profile='full', size=(u'290', u'50'))

    rect_with_radius_mask = dwg.mask((0, 0), (width, height), id='a')
    rect_with_radius_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))
    dwg.add(rect_with_radius_mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))
    g.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#2196F3'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    slogan_link = Hyperlink('https://www.phodal.com/', target='_blank')
    shapes.add(dwg.text(author, insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    slogan_link.add(dwg.text(author, insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    dwg.add(slogan_link)

    def draw_for_bg_plus():
        for x in range(y_text_split + rect_length, width, rect_length):
            shapes.add(dwg.line((x, 0), (x, height), stroke='#EEEEEE', stroke_width='0.5', stroke_opacity=0.1))

        for y in range(rect_length, height, rect_length):
            shapes.add(
                dwg.line((y_text_split, y), (width, y), stroke='#EEEEEE', stroke_width='0.5', stroke_opacity=0.1))

        for x in range(y_text_split + max_rect_length, width, max_rect_length):
            for y in range(0, height, max_rect_length):
                shapes.add(dwg.line((x, y - 2), (x, y + 2), stroke='#EEEEEE', stroke_width='0.8', stroke_opacity=0.15))

        for y in range(0, height, max_rect_length):
            for x in range(y_text_split + max_rect_length, width, max_rect_length):
                shapes.add(dwg.line((x - 2, y), (x + 2, y), stroke='#EEEEEE', stroke_width='0.8', stroke_opacity=0.15))

    draw_for_bg_plus()

    shapes.add(
        dwg.text('idea', insert=(secondary_text_x + 1, basic_text_y + 1), fill='#000', font_size=40, fill_opacity=0.3,
                 font_family='Helvetica'))
    shapes.add(dwg.text('idea', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))
    dwg.save()


def generate_article():
    dwg = svgwrite.Drawing('shields/article-small.svg', size=(u'323', u'50'))

    height = 50
    width = 323

    rect_with_radius_mask = dwg.mask((0, 0), (width, height), id='a')
    rect_with_radius_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))
    dwg.add(rect_with_radius_mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))
    g.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#ffeb3b'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    slogan_link = Hyperlink('https://www.phodal.com/', target='_blank')
    shapes.add(dwg.text(author, insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    slogan_link.add(
        dwg.text(author, insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    dwg.add(slogan_link)

    def create_text():
        g.add(dwg.text(insert=(phodal_width, 6), fill='#34495e', opacity=0.2, font_size=4,
                       text='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, fe-'))
        g.add(dwg.text(insert=(phodal_width, 12), fill='#34495e', opacity=0.2, font_size=4,
                       text='ugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi'))
        g.add(dwg.text(insert=(phodal_width, 18), fill='#34495e', opacity=0.2, font_size=4,
                       text='vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, '))
        g.add(dwg.text(insert=(phodal_width, 24), fill='#34495e', opacity=0.2, font_size=4,
                       text='condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum '))
        g.add(dwg.text(insert=(phodal_width, 30), fill='#34495e', opacity=0.2, font_size=4,
                       text='rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus,'))
        g.add(dwg.text(insert=(phodal_width, 36), fill='#34495e', opacity=0.2, font_size=4,
                       text=' neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi,'))
        g.add(dwg.text(insert=(phodal_width, 42), fill='#34495e', opacity=0.2, font_size=4,
                       text=' tincidunt quis, accumsan porttitor, facilisis luctus, metus'))
        g.add(dwg.text(insert=(phodal_width, 48), fill='#34495e', opacity=0.2, font_size=4,
                       text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget '))
        g.add(dwg.text(insert=(phodal_width, 54), fill='#34495e', opacity=0.2, font_size=4,
                       text='ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus '))
        g.add(dwg.text(insert=(phodal_width, 60), fill='#34495e', opacity=0.2, font_size=4,
                       text='turpis elit sit amet quam. Vivamus pretium ornare est.'))

    create_text()

    g.add(dwg.text('article', insert=(secondary_text_x + 1, basic_text_y + 1), fill='#000', fill_opacity=0.3,
                   font_size=40, font_family='Helvetica'))
    g.add(dwg.text('article', insert=(secondary_text_x, basic_text_y), fill='#34495e', font_size=40,
                   font_family='Helvetica'))

    dwg.save()


def get_some_random10(num):
    results = ''
    for x in range(1, num):
        results += str(random.getrandbits(1))
    return results


def generate_works():
    width = 316
    height = 50

    dwg = svgwrite.Drawing('shields/works-small.svg', size=(u'316', u'50'))

    rect_with_radius_mask = dwg.mask((0, 0), (width, height), id='a')
    rect_with_radius_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))
    dwg.add(rect_with_radius_mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#2c3e50'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    for x in range(0, 100, 5):
        text = get_some_random10(100)
        g.add(
            dwg.text(text, insert=(phodal_width + 1, x), fill='#27ae60', font_size=4,
                     font_family='Inconsolata for Powerline',
                     opacity=0.3, transform="rotate(15 300, 0)"))

    g.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))

    slogan_link = Hyperlink('https://www.phodal.com/', target='_blank')
    shapes.add(dwg.text(author, insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    slogan_link.add(
        dwg.text(author, insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    dwg.add(slogan_link)

    shapes.add(
        dwg.text('works', insert=(secondary_text_x + 1, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                 font_family='Helvetica'))
    shapes.add(dwg.text('works', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))

    dwg.save()


def generate_design():
    # for D Rect
    red_point = 272
    design_width = 162
    width = 338
    height = 50

    dwg = svgwrite.Drawing('shields/design-small.svg', size=(u'338', u'50'))
    rect_with_radius_mask = dwg.mask((0, 0), (width, height), id='a')
    rect_with_radius_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))

    dwg.add(rect_with_radius_mask)
    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    g.add(dwg.rect((0, 0), (phodal_width, 50), fill='#5E6772'))

    shapes.add(dwg.rect((phodal_width, 25.6), (design_width, 30), fill='#2196f3'))

    shapes.add(dwg.text('design', insert=(secondary_text_x + 5, 36), fill='#000', stroke_width=4, font_size=40,
                        font_family='Helvetica'))
    shapes.add(dwg.rect((phodal_width, 0), (design_width, 26), fill='#03a9f4'))
    shapes.add(dwg.rect((phodal_width, 25.6), (design_width, 0.6), fill='#000'))
    shapes.add(dwg.text('design', insert=(secondary_text_x + 4, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))

    def draw_red_point():
        shapes.add(dwg.ellipse((red_point, 8), (3, 3), fill='#000'))
        shapes.add(dwg.ellipse((red_point + 1, 8), (3, 3), fill='#f44336'))

    draw_red_point()

    slogan_link = Hyperlink('https://www.phodal.com/', target='_blank')
    shapes.add(dwg.text(author, insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    slogan_link.add(
        dwg.text(author, insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    dwg.add(slogan_link)

    dwg.save()

def generate_book():
    dwg = svgwrite.Drawing('shields/book-small.svg', size=(u'323', u'50'))
    height = 50
    width = 308

    rect_with_radius_mask = dwg.mask((0, 0), (width, height), id='a')
    rect_with_radius_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))
    dwg.add(rect_with_radius_mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))
    g.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#2ECC71'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    slogan_link = Hyperlink('https://www.phodal.com/', target='_blank')
    shapes.add(dwg.text(author, insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    slogan_link.add(
        dwg.text(author, insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    dwg.add(slogan_link)

    def draw_for_bg_plus():
        for y in range(0, 50, 5):
            shapes.add(dwg.line((180, y), (304, y), stroke='#EEEEEE', stroke_width='0.2', stroke_opacity=0.5))

    draw_for_bg_plus()

    shapes.add(dwg.text('book', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))

    dwg.save()


generate_idea()
generate_article()
generate_book()
