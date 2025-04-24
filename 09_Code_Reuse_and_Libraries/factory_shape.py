class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "CIRCLE":
            return "ini adalah lingkaran"
        elif shape_type == "SQUARE":
            return 'ini adalah persegi'
        elif shape_type == "RECTANGLE":
            return 'ini adalah persegi panjang'
        else:
            raise ValueError("Unknown shape type")

print(ShapeFactory.get_shape("CIRCLE"))
print(ShapeFactory.get_shape("SQUARE"))
print(ShapeFactory.get_shape("RECTANGLE"))