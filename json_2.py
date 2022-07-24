import json


def json_2():

    a_json_data = '''
    [
        {
            "id": "001",
            "x": "2",
            "name": "Chuck"
        },
        {
            "id": "009",
            "x": "7",
            "name": "Terry"
        }
    ]
    '''

    # Loads the data to a dictionary structure.
    a_json_struct = json.loads(a_json_data)

    for a_json_item in a_json_struct:

        print(f"Name= {a_json_item['name']}")
        print(f"ID= {a_json_item['id']}")
        print(f"Attribute= {a_json_item['x']}")

    # End of function.
    return


if __name__ == '__main__':

    json_2()