import json


def json_1():

    a_json_data = '''
    {
        "name": "Chuck",
        "phone": 
        {
            "type": "intl",
            "number": "+1 734 303 4456"
        },
        "email": 
        {
            "hide": "yes"
        }
    }
    '''

    # Loads the data to a dictionary structure.
    a_json_struct = json.loads(a_json_data)

    print(f"Name= {a_json_struct['name']}")
    print(f"Hide= {a_json_struct['email']['hide']}")

    # End of function.
    return


if __name__ == '__main__':

    json_1()
