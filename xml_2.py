import xml.etree.ElementTree as et


def xml_2():

    a_xml_data = '''
        <stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Brent</name>
                </user>
            </users>
        </stuff>
        '''

    # Read the xlm data to the library.
    a_xml_tree = et.fromstring(a_xml_data)

    # Select a path and create a list of all instances bellow that node.
    a_xml_node_list = a_xml_tree.findall('users/user')
    print(f"User count: {len(a_xml_node_list)}")

    for a_node_user in a_xml_node_list:

        print(f"Name: {a_node_user.find('name').text}")
        print(f"ID: {a_node_user.find('id').text}")
        print(f"Attribute x: {a_node_user.get('x')}")

    # End function
    return


if __name__ == '__main__':
    xml_2()
