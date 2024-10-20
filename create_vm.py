#!/usr/bin/env python3

import argparse
import os
import time
import googleapiclient.discovery
import google.auth
from google.cloud import compute_v1
from scipy.constants import value


# Creates instance in the specified zone. Code adopted from GCP documentation https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/compute/api/create_instance.py
def create_instance(
    compute: object,
    project: str,
    zone: str,
    name: str,
    bucket: str,
    tags: list,
) -> str:
    """Creates an instance in the specified zone.

    Args:
      compute: an initialized compute service object.
      project: the Google Cloud project ID.
      zone: the name of the zone in which the instances should be created.
      name: the name of the instance.
      bucket: the name of the bucket in which the image should be written.

    Returns:
      The instance object.
    """
    # Get the 'ubuntu-2204-lts' image family from 'ubuntu-os-cloud' project
    image_response = (
        compute.images()
        .getFromFamily(project="ubuntu-os-cloud", family="ubuntu-2204-lts")
        .execute()
    )
    source_disk_image = image_response["selfLink"]

    # Configure the machine - f1-micro type machine
    machine_type = "zones/%s/machineTypes/e2-standard-2" % zone
    startup_script = open(
        os.path.join(os.path.dirname(__file__), "startup-script.sh")
    ).read()


    # rest_client_script = open(
    #     os.path.join(os.path.dirname(__file__), "rest-client.py"), 'r').read()
    #
    # rest_server_script = open(
    #     os.path.join(os.path.dirname(__file__), "rest-server.py"), 'r').read()
    #
    # grpc_client_script = open(
    #     os.path.join(os.path.dirname(__file__), "grpc-client.py"), 'r').read()
    #
    # grpc_server_script = open(
    #     os.path.join(os.path.dirname(__file__), "grpc-server.py"), 'r').read()
    #
    # grpc_details_pb2_script = open(
    #     os.path.join(os.path.dirname(__file__), "grpc_details_pb2.py"), 'r').read()
    #
    # grpc_details_pb2_grpc_script = open(
    #     os.path.join(os.path.dirname(__file__), "grpc_details_pb2_grpc.py"), 'r').read()


    config = {
        "name": name,
        "machineType": machine_type,
        # Specify the boot disk and the image to use as a source.
        "disks": [
            {
                "boot": True,
                "autoDelete": True,
                "initializeParams": {
                    "sourceImage": source_disk_image,
                },
            }
        ],
        # Specify a network interface with NAT to access the public
        # internet.
        "networkInterfaces": [
            {
                "network": "global/networks/default", # Default to default network
                "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT"}],
            }
        ],
        # Allow the instance to access cloud storage and logging.
        "serviceAccounts": [
            {
                "email": "default",
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.read_write",
                    "https://www.googleapis.com/auth/logging.write",
                ],
            }
        ],
        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        "metadata": {
            "items": [

                {
                    "key": "bucket",
                    "value": bucket
                },
                # {
                #     "key": "rest_client_script",
                #     "value" : rest_client_script
                # },
                # {
                #     "key": "rest_server_script",
                #     "value" : rest_server_script
                # },
                # {
                #     "key": "grpc_client_script",
                #     "value": grpc_client_script
                # },
                # {
                #     "key": "grpc_server_script",
                #     "value": grpc_server_script
                # },
                # {   "key": "grpc_details_pb2_script",
                #     "value": grpc_details_pb2_script
                # },
                # {   "key": "grpc_details_pb2_grpc_script",
                #     "value": grpc_details_pb2_grpc_script
                # },
                {
                    # Startup script is automatically executed by the
                    # instance upon startup.
                    "key": "startup-script",
                    "value": startup_script,
                },



            ]
        },
        "tags": {
            "items": [
                tags
            ]
        }
    }

    return compute.instances().insert(project=project, zone=zone, body=config).execute()
# [END compute_create_instance]

# [START compute_wait_for_operation]
# Waits for operation specified by 'operation' arg to complete
def wait_for_operation(
    compute: object,
    project: str,
    zone: str,
    operation: str,
) -> dict:
    """Waits for the given operation to complete.

    Args:
      compute: an initialized compute service object.
      project: the Google Cloud project ID.
      zone: the name of the zone in which the operation should be executed.
      operation: the operation ID.

    Returns:
      The result of the operation.
    """
    print("Waiting for operation to finish...")
    while True:
        result = (
            compute.zoneOperations()
            .get(project=project, zone=zone, operation=operation)
            .execute()
        )

        if result["status"] == "DONE":
            print("done.")
            if "error" in result:
                raise Exception(result["error"])
            return result

        time.sleep(1)



credentials, _ = google.auth.default()
compute = googleapiclient.discovery.build("compute", "v1", credentials=credentials)
project_id = "shining-reality-434906-c1"
bucket_name = "csci5253-lab5-bucket"

tags = ['allow-5000']
print("Step 1: Creating instance")
operation = create_instance(compute, project=project_id, zone="us-west1-a", name="lab6-instance1", bucket=bucket_name, tags=tags)
wait_for_operation(compute, project_id, zone="us-west1-a", operation=operation["name"])

operation = create_instance(compute, project=project_id, zone="us-west1-a", name="lab6-instance2", bucket=bucket_name, tags=tags)
wait_for_operation(compute, project_id, zone="us-west1-a", operation=operation["name"])

operation = create_instance(compute, project=project_id, zone="europe-west3-a", name="lab6-instance3", bucket=bucket_name, tags=tags)
wait_for_operation(compute, project_id, zone="europe-west3-a", operation=operation["name"])


