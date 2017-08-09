import argparse
import os
import re
import sandstone



def run_server():
    parser = argparse.ArgumentParser(description='Run Sandstone IDE via JupyterHub.')
    parser.add_argument('--port')
    parser.add_argument('--token')
    parser.add_argument('--cookie-name')
    parser.add_argument('--hub-host')
    parser.add_argument('--base-url')
    parser.add_argument('--hub-prefix')
    parser.add_argument('--hub-api-url')
    parser.add_argument('--ip')
    parser.add_argument('--user')
    args = parser.parse_args()

    # Set hub api url environment variable to be read by the login handler
    os.environ['JUPYTERHUB_API_URL'] = args.hub_api_url[1:-1]
    # Add the $WORK variable to the env so we can see it under volumes
    os.environ['WORK'] = re.sub('^\/home','/work',os.environ['HOME'])

    # Remove extraneous quotes from string
    prefix = args.base_url[1:-1]

    sandstone.app.main(port=args.port,prefix=prefix)
