import xml.etree.ElementTree as et


def test_1():

    # Strings are better contained by tags to avoid creating trailing spaces.
    a_xml_data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">+1 374 303 4456</phone>
        <email hide="yes" />
    </person>
    '''

    # Read the xlm data to the library.
    a_xml_tree = et.fromstring(a_xml_data)

    # Get a leaf data.
    a_name = a_xml_tree.find("name").text
    print(f"A leaf node text 'name' is: {a_name}")

    # Get a leaf data.
    a_phone = a_xml_tree.find('phone').text
    print(f"A leaf node text 'phone' is: {a_phone}")

    # Get an attribute of a node.
    a_leaf_attribute = a_xml_tree.find('email').get('hide')
    print(f"Email node, attribute 'hide' is: {a_leaf_attribute}")

    # Get another attribute of a node.
    b_leaf_attribute = a_xml_tree.find('phone').get('type')
    print(f"Phone node, attribute 'type' is: {b_leaf_attribute}")

    # End function
    return


if __name__ == '__main__':

    test_1()
