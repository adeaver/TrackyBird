class Rectangle():
    
    def __init__(self, left, top, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def contains(self, rect):
        if(rect.get_right() >= self.left and rect.get_left() <= self.left+self.width):
            if(rect.get_top() <= self.top+self.height and rect.get_bottom() >= self.top):
                return True

        return False

    def get_left(self):
        return self.left

    def get_right(self):
        return self.left + self.width

    def get_top(self):
        return self.top

    def get_bottom(self):
        return self.top + self.height
