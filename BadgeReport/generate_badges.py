import json

from pybadges import badge
import pytest

def badge_python(badge_folder, version):
    """
        Generates badge for python version
    Args:
        badge_folder (str): Path to the output svg file
        version (str): Python version
    """
    file_path = badge_folder + '/b_python.svg'
    b_file = badge(left_text='Python', right_text=version, right_color='blue')

    with open(file_path, 'w') as f:
        f.write(b_file)


def badge_pytest(badge_folder, tests_folder):
    """
           Generates badge for pytest tests
       Args:
           badge_folder (str): Path to the output svg file
           tests_folder(str): Folder where the tests are
       """
    file_path = badge_folder + '/b_pytest.svg'

    test_log = badge_folder + 'log.json'

    pytest.main([tests_folder, '-q', '--report-log='+test_log])

    # Parse json output:
    log_file = open(test_log, 'r')
    log_lines = log_file.readlines()
    total = 0
    passed = 0

    for line in log_lines:
        line_data = json.loads(line)
        if line_data.get("when", False) and line_data.get("when", False) == "call":
            total += 1
            if line_data['outcome'] == "passed":
                passed += 1

    text = f'{passed}/{total}'

    percentage = passed / total

    color = 'red'
    if 0.4 <= percentage < 0.6:
        color = 'orange'
    if percentage < 0.8:
        color = 'yellow'
    if percentage > 0.8:
        color = 'green'

    b_file = badge(left_text='Pytest', right_text=text, right_color=color)

    with open(file_path, 'w') as f:
        f.write(b_file)


if __name__ == '__main__':
    badge_python(badge_folder='./badges/', version='3.8.11')
    badge_pytest(badge_folder='./badges/', tests_folder='../Example/Tests/')