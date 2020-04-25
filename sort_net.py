#!/usr/bin/env python3

def wire(name=None, debug=None):

    comparators = list()

    def connect(comparator):
        if debug:
            print(f'wire({name}): adding comparator {comparator["get_name"]()}')
        comparators.append(comparator)

    def get_comparators():
        return comparators

    def is_set():
        return not link['value'] is None

    def get_value():
        return link['value']

    def get_name():
        return link['name']

    def set_value(src_comparator, value):
        if debug:
            if src_comparator is None:
                print(f'wire({name}): setting value {value} by comparator None')
            else:
                print(f'wire({name}): setting value {value} by comparator {src_comparator["get_name"]()}')
        link['value'] = value
        for comparator in comparators:
            if comparator is not src_comparator:
                if debug:
                    print(f'wire({name}): sending update to comparator {comparator["get_name"]()}')
                comparator['update'](link)

    # A dispatch dictionary
    link = { 'name': name,
             'value': None,
             'connect': connect,
             'set': set_value,
             'get': get_value,
             'is_set': is_set,
             'get_name': get_name,
             'comparators': get_comparators }

    return link

def comparator(inn, inx, outx, outn, inn_f, inx_f, outx_f, outn_f, name=None, debug=None):

    def update(src_wire):
        if debug:
            print(f'comparator({name}): got update from wire {src_wire["get_name"]()}')
        if src_wire in (inn, inx) and inn['is_set']() and inx['is_set']():
            outx_val = outx_f(inn['get'](), inx['get']())
            if debug:
                print(f'comparator({name}): setting value {outx_val} to wire {outx["get_name"]()}')
            outx['set'](node, outx_val)
            outn_val = outn_f(inn['get'](), inx['get']())
            if debug:
                print(f'comparator({name}): setting value {outn_val} to wire {outn["get_name"]()}')
            outn['set'](node, outn_val)
        elif src_wire in (outn, outx) and outn['is_set']() and outx['is_set']():
            inx_val = inx_f(outn['get'](), outx['get']())
            if debug:
                print(f'comparator({name}): setting value {inx_val} to wire {inx["get_name"]()}')
            inx['set'](node, inx_val)
            inn_val = inn_f(outn['get'](), outx['get']())
            if debug:
                print(f'comparator({name}): setting value {inn_val} to wire {inn["get_name"]()}')
            inn['set'](node, inn_val)

    def get_name():
        return node['name']

    # A dispatch dictionary
    node = { 'name': name,
             'get_name': get_name,
             'update': update }

    for conn in (inn, inx, outx, outn):
        if debug:
            print(f'comparator({name}): sending connect to wire {conn["get_name"]()}')
        conn['connect'](node)

    return node
