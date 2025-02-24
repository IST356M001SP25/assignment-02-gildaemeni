'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''
    final_list = []
    parts = packaging_data.split(' / ')
    for i, part in enumerate(parts):  # Loop through each packaging description
        items = part.strip().split(" in ")  # Step 2: Split on " in "
        
        # Extract the item name and quantity
        quantity, item = items[0].split(" ", 1)
        quantity = int(quantity)

        # Store the extracted item first
        final_list.append({item: quantity})

        # If there's a second part (packaging level), extract it
        if len(items) > 1:
            packaging_quantity, packaging = items[1].split(" ", 1)
            packaging_quantity = int(packaging_quantity)

            # Only store packaging if it's the last level (not an intermediate step)
            if i == len(parts) - 1:
                final_list.append({packaging: packaging_quantity})
                
    return final_list
def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    pass # TODO: Replace this line and write code


def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    pass # TODO: Replace this line and write code

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")