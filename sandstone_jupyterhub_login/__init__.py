import argparse
import os
import sandstone



def run_server():
    parser = argparse.ArgumentParser(description='Run Sandstone IDE via JupyterHub.')
    parser.add_argument('port')
    parser.add_argument('token')
    parser.add_argument('cookie-name')
    parser.add_argument('hub-host')
    parser.add_argument('base-url')
    parser.add_argument('hub-prefix')
    parser.add_argument('hub-api-url')
    parser.add_argument('ip')
    parser.add_argument('user')

    args = parser.parse_args()

    os.environ['SANDSTONE_PORT'] = args.port
    os.environ['SANDSTONE_PREFIX'] = args.base_url

    sandstone.app.main()
