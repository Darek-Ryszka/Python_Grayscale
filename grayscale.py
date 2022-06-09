from argparse import ArgumentParser

parser = ArgumentParser(description='Changing pictures on grayscale.')
parser.add_argument('--input', help='Color image.', required=True)
parser.add_argument('--output', help='Grayscale image.', required=True)
args = parser.parse_args()
