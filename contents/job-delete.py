#!/usr/bin/env python -u
import logging
import sys
import os
import common
from kubernetes import client
from kubernetes.client.rest import ApiException


logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='%(levelname)s: %(name)s: %(message)s')
log = logging.getLogger('kubernetes-service-delete')


def main():

    if os.environ.get('RD_CONFIG_DEBUG') == 'true':
        log.setLevel(logging.DEBUG)
        log.debug("Log level configured for DEBUG")

    data = {}

    data["name"] = os.environ.get('RD_CONFIG_NAME')
    data["namespace"] = os.environ.get('RD_CONFIG_NAMESPACE')

    common.connect()

    k8s_client = client.BatchV1Api()

    try:

        body = client.V1DeleteOptions()  # V1DeleteOptions |
        pretty = 'pretty_example'

        api_response = k8s_client.delete_namespaced_job(
            name=data["name"],
            namespace=data["namespace"],
            body=body,
            pretty=pretty
        )
        print("Deployment deleted '%s'" % str(api_response.status))

    except ApiException as e:
        log.error("Exception when calling delete_namespaced_job: %s\n" % e)
        sys.exit(1)


if __name__ == '__main__':
    main()
