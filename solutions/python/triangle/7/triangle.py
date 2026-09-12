"""Module providing a function printing python version."""
import sys
def equilateral(sides):
    """
    Parameter: sides
    result: Let know if the triangle is equilateral
    """
    return sides[0] == sides[1] == sides[2] and (sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1])

def isosceles(sides):
    """
    Parameter: sides
    result: Let know if the triangle is isosceles
    """
    return (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]) and (sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1])

def scalene(sides):
    """
    Parameter: sides
    result: Let know if the triangle is scalene
    """
    return not(sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]) and (sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1])