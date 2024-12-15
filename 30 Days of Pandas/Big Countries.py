import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[['name', 'population', 'area']][ (world['area'] >= 3000000) | (world['population'] >= 25000000) ]

# alternative: world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ['name', 'population', 'area']]
