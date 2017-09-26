# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# This program calculates the cost of a pizza when given the diameter

import ui

def calculate_button_touch_up_inside(sender):
    # calculate circumference
    
    # constants
    PI = 3.14
    LABOUR_AND_RENT_COSTS = 1.75
    MATERIAL_COST = 0.50
    HST = 1.13
    
    # input
    diameter = float(view['diameter_textbox'].text)
    
    # process
    cost = (LABOUR_AND_RENT_COSTS + MATERIAL_COST * diameter) * HST
    
    # output
    # got currency format from here:
    # http://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
    view['answer_label'].text = 'The cost is: ' + '${:,.2f}'.format(cost)

view = ui.load_view()
view.present('full_screen')
