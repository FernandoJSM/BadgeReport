from pybadges import badge


def badge_python(file_path, version):
    """
        Generates badge for python version
    Args:
        file_path (str): Path to the output svg file
        version (str): Python version
    """

    b_file = badge(left_text='Python', right_text=version, right_color='blue')

    with open(file_path, 'w') as f:
        f.write(b_file)


if __name__ == '__main__':
    badge_python(file_path='./b_python.svg', version='3.8.11')