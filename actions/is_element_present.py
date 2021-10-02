def is_element_present(context, element):
    try:
        context.element.find_element(*element)
        return True
    except:
        return False