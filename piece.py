class piece:
    'base class for tetris pieces' #documentation string
   
    def __init__(self,id,location_y,location_x)
	self.id = id
	self.__location_y = location_y
	self.__location_x = location_x
    def rotate_right        (self)
    def rotate_left         (self)
    def set_location_x      (self, new_x)
    def set_location_y      (self, new_y)
    def display	            (self)
    def remove_bottom_lines (self, num_lines)
    def is_in_play          (self, is_in_play)
