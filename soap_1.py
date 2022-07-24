from zeep import Client

# Run this command in the terminal if want to access the schema definition.
# python -mzeep http://www.dneonline.com/calculator.asmx?WSDL


def soap_1():

    # Create a client instance to connect to service.
    a_soap_client = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')

    # Call web service.
    a_add_result = a_soap_client.service.Add(65, 7)
    print(f"65 + 7 = {a_add_result}")

    # End main function.
    return


if __name__ == '__main__':

    soap_1()
