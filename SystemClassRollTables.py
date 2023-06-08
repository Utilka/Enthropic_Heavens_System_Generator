import RollTable

universal_rare_resources = ["Ionic Crystals", "Giga Lattice", "Amianthoid", "Mercurite", "Beryllium"]
gray_resources = ["Filler1", "Filler2"]
red_resources = ["Filler10", "Filler20"]
syst_unique_resources = ["RedSang", "Bluecap Mold", "Eden Incense", "Transvine", "Superspuds", "Proto-Orchid",
                         "Proto-Spores"]

syst_modifiers = [
    "Strong Magnetic Field", "Cyber Flora", "Low Gravity", "Molten Springs",
    "High Gravity", "Behemoth Song", "Talking World", ]


class RareResource:
    def __init__(self, name, effect, description):
        self.name = name
        self.effect = effect
        self.description = description

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return self.name


class SystemModifier:
    def __init__(self, name, effect, description):
        self.name = name
        self.effect = effect
        self.description = description

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return self.name


def create_rr_rolltables():
    pass


def create_mod_rolltables():
    universal_modifiers = [
        SystemModifier("Mineral Rich", "", ""),
        SystemModifier("Antonov Rings", "", ""),
        SystemModifier("Huygens Rings", "", ""),
        SystemModifier("Hollow Planet", "", ""),
        SystemModifier("Strong Magnetic Field", "", ""),
        SystemModifier("Low Gravity", "", ""),
        SystemModifier("High Gravity", "", "", ),
        SystemModifier("Behemoth Song", "", ""),
        SystemModifier("Shattered Crust", "", ""),
        SystemModifier("Ice-10", "", ""),
    ]
    fertile_modifiers = [
        SystemModifier("Psychoactive Air", "", ""),
        SystemModifier("Garden of Eden", "", ""),
        SystemModifier("Friendly Locals", "", ""),
        SystemModifier("Rich Soil", "", ""),
        SystemModifier("Hadopelagic Life", "", ""),
        SystemModifier("Permanent Monsoon", "", ""),
        SystemModifier("Long Season", "", ""),
        SystemModifier("Hostile Fauna", "", ""),
        SystemModifier("Poor Soil", "", ""),
        SystemModifier("Metallic Waters", "", ""),
        SystemModifier("Coral Reefs", "", ""),
        SystemModifier("Mutated Flora", "", ""),
        SystemModifier("Propitious Seasons", "", ""),
        SystemModifier("The Fallen Gardens", "", ""),
        SystemModifier("Tree of Worlds", "", ""),
    ]
    unique_modifiers = [
        SystemModifier("Cyber Flora", "", ""),
        SystemModifier("Kessler Syndrome", "", ""),
        SystemModifier("Ancient Ruins", "", ""),
        SystemModifier("Deserted Cities", "", ""),
        SystemModifier("Guardian", "", ""),
        SystemModifier("The Platform of Ys", "", ""),
        SystemModifier("Strange Fossils", "", ""),
        SystemModifier("Humeris Insidentes", "", ""),
        SystemModifier("Fearful Symmetry", "", ""),
        SystemModifier("Talking World", "", ""),
    ]
    young_modifiers = [
        SystemModifier("Molten Springs", "", ""),
        SystemModifier("Geothermic Activity", "", ""),
        SystemModifier("Seismic Activity", "", ""),
        SystemModifier("Komatiite Volcanoes", "", ""),
        SystemModifier("Acid Rains", "", ""),
        SystemModifier("Unstable Solar Winds", "", ""),
    ]
    extreme_modifiers = [
        SystemModifier("Meteor Strikes", "", ""),
        SystemModifier("Irradiated", "", ""),
        SystemModifier("Chthonian World", "", ""),
        SystemModifier("Aurora Waves", "", ""),
        SystemModifier("Radiation Belts", "", ""),
        SystemModifier("Spatial Vortexes", "", ""),
        SystemModifier("Exotic Particle Emissions", "", ""),
    ]

    universal_m_rolltable = RollTable.RollTable(options=[RollTable.Option(i, 1) for i in universal_modifiers])
    fertile_m_rolltable = RollTable.RollTable(options=[RollTable.Option(i, 1) for i in fertile_modifiers])
    unique_m_rolltable = RollTable.RollTable(options=[RollTable.Option(i, 1) for i in unique_modifiers])
    young_m_rolltable = RollTable.RollTable(options=[RollTable.Option(i, 1) for i in young_modifiers])
    extreme_m_rolltable = RollTable.RollTable(options=[RollTable.Option(i, 1) for i in extreme_modifiers])

    fertile_planet_rolltable = RollTable.RollTable(options=[
        RollTable.Option(None, 10)],
        rolltables=[
            RollTable.Option(fertile_m_rolltable, 20),
            RollTable.Option(universal_m_rolltable, 2),
        ])

    green_class_rolltable = RollTable.RollTable(options=[
        RollTable.Option(None, 12)],
        rolltables=[
            RollTable.Option(universal_m_rolltable, 2),
            RollTable.Option(unique_m_rolltable, 1),
        ])

    orange_class_rolltable = RollTable.RollTable(options=[
        RollTable.Option(None, 12)],
        rolltables=[
            RollTable.Option(universal_m_rolltable, 2),
            RollTable.Option(unique_m_rolltable, 1),
        ])

    red_class_rolltable = RollTable.RollTable(options=[
        RollTable.Option(None, 10)],
        rolltables=[
            RollTable.Option(universal_m_rolltable, 1),
            RollTable.Option(young_m_rolltable, 4),
            RollTable.Option(extreme_m_rolltable, 2),
        ])

    grey_class_rolltable = RollTable.RollTable(options=[
        RollTable.Option(None, 8)],
        rolltables=[
            RollTable.Option(universal_m_rolltable, 1),
            RollTable.Option(extreme_m_rolltable, 6),
        ])

    modifier_rolltables = {
        "fertile": fertile_planet_rolltable,
        "green": green_class_rolltable,
        "orange": orange_class_rolltable,
        "red": red_class_rolltable,
        "grey": grey_class_rolltable,
    }
    return modifier_rolltables


def main():
    mod_rolltables = create_mod_rolltables()
    print([str(mod_rolltables["fertile"]()) for i in range(10)])
    print([str(mod_rolltables["green"]()) for i in range(10)])
    print([str(mod_rolltables["orange"]()) for i in range(10)])
    print([str(mod_rolltables["red"]()) for i in range(10)])
    print([str(mod_rolltables["grey"]()) for i in range(10)])
    pass


if __name__ == '__main__':
    main()
