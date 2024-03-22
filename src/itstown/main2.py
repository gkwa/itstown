import xml.etree.ElementTree


def update_gui_address(config_file):
    tree = xml.etree.ElementTree.parse(config_file)
    root = tree.getroot()

    gui_element = root.find("gui")
    address_element = gui_element.find("address")
    address_element.text = "0.0.0.0:8384"
    tree.write(config_file)
