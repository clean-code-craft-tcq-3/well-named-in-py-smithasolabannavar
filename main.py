from get_color_and_pair_number import get_pair_number_from_color, get_color_from_pair_number
import constants

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)

def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def print_manual():
  for x in constants.MAJOR_COLORS:
    for y in constants.MINOR_COLORS:
      print(get_pair_number_from_color(x, y), x, y)

if __name__ == '__main__':
  print_manual()
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
