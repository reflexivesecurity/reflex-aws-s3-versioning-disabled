""" Module for S3VersioningDisabled """

import json
import os

import boto3
from reflex_core import AWSRule


class S3VersioningDisabled(AWSRule):
    """A Reflex rule to alert when S3 bucket versioning is disabled """

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.bucket_name = event["detail"]["requestParameters"]["bucketName"]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        # Always return false because any request we receive should be reported.
        return False

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        # TODO: Provide a human readable message describing what occured. This
        # message is sent in all notifications.
        #
        # Example:
        return f"S3 bucket versioning was disabled on {self.bucket_name}."


def lambda_handler(event, _):
    """ Handles the incoming event """
    rule = S3VersioningDisabled(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()
