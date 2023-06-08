import RollTable
import StarRollTable
import random

# IF there are no rare resources or syst_modifiers available, insert a "placeholder", as the code no likey when rare resources or system modifiers are empty.

hex_types = ["nursery", "arm", "inter-arm", "core"]

final_result = ["Star Type", "placehold", "Star Amount", "0", "Rare Resources", "none", "System Modifier", "none",
                "No. of Planets", "0", "No. of Moons", "0"]


class Planet:
    size_options = {"Small": 0.8, "Medium": 1, "Large": 1.4}
    sterility_options = ["Gas giant", "Sterile", "Moderate", "Fertile"]
    temperature_options = ["Cold", "Temperate", "Hot"]

    def __init__(self, sterility=None, temperature=None, size=None, moons=None, name=None, description=None):
        if moons is None:
            moons = []
        assert sterility in self.sterility_options
        self.sterility = sterility
        assert sterility in self.temperature_options
        self.temperature = temperature
        assert sterility in self.size_options
        self.size = size
        self.moons = moons
        self.name = name
        self.description = description


class StarSystem:

    def __init__(self, stars: [StarType] = None, coordinates=None, name=None, planets=None, modifier=None,
                 rare_resource=None, rare_resource_quantity=None):
        if stars is None:
            stars = []
        if planets is None:
            planets = []
        self.stars = stars
        self.coordinates = coordinates
        self.name = name
        self.planets = planets
        self.modifier = modifier
        self.rare_resource = rare_resource
        self.rare_resource_quantity = rare_resource_quantity

    @property
    def system_class(self):
        for star_class in StarType.star_class_rank:
            for star in self.stars:
                if star.type == star_class:
                    return star_class
        return "grey"

def main():
    star_rolltables = create_star_rolltables()


if __name__ == '__main__':
    main()
