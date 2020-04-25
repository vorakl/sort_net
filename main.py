#!/usr/bin/env python3

# A network for 4 numbers:
#
# a1 -||-- a2 -------------||------------------ a3
# b1 -||-- b2 --\ /-- c2 --||--\ /-- b3 --|| -- b4
#                X              X         ||
# c1 -||-- c2 --/ \-- b2 --||--/ \-- c3 --|| -- c4
# d1 -||-- d2 -------------||------------------ d3

import sort_net as sn

def wires(num):
    return (sn.wire() for i in range(num))

def comparator(w1, w2, w3, w4):
    return sn.comparator(w1 ,w2, w3, w4, min, max, max, min)

def main():
    # Create wires
    a1, a2, a3, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3 = wires(14)

    # Link wires to a network using comparators
    comparator(a1, b1, a2, b2)
    comparator(c1, d1, c2, d2)
    comparator(a2, c2, a3, c3)
    comparator(b2, d2, b3, d3)
    comparator(b3, c3, b4, c4)

    # Set values on the left side of a network
    for wire, value in ((a1,2), (b1,5), (c1,1), (d1,6)):
        wire['set'](None, value)

    # Get values on the right side of a network
    for wire in (a3, b4, c4, d3):
        print(wire['get']())

    print('------------')

    # Set values on the right side of a network
    for wire, value in ((a3,7), (b4,2), (c4,10), (d3,7)):
        wire['set'](None, value)

    # Get values on the left side of a network
    for wire in (a1, b1, c1, d1):
        print(wire['get']())

if __name__ == '__main__':
    main()
