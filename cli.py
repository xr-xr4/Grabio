import argparse
from grabio import Grabio

parser = argparse.ArgumentParser(description='Grabio CLI - Extract website information')
parser.add_argument('--url', required=True, help='Target website URL')
parser.add_argument('--info', action='store_true', help='Extract full website info')
parser.add_argument('--ip', action='store_true', help='Extract IP address only')
parser.add_argument('--whois', action='store_true', help='Extract WHOIS info only')

args = parser.parse_args()

grabio = Grabio(args.url)

if args.info:
    grabio.show_info()

if args.ip:
    print(grabio.ip())

if args.whois:
    print(grabio.whois_info())