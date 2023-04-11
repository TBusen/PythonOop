# Cocci
# Bacilli
# Spirilla


from xmlrpc.client import Boolean


class Bacteria:
    
    def __init__(self, species, shape, flagella: Boolean , cell_material, x, y) -> None:
        self.species = species
        self.shape = shape
        self.flagella = flagella
        self.cell_material = cell_material
        self.single_cell = True
        self.x = x
        self.y = y

    