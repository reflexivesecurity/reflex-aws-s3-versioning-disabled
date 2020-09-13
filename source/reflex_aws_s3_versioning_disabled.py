""" Module for S3VersioningDisabled """

import json
import os

import boto3
from reflex_core import AWSRule, subscription_confirmation


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
        return f"S3 bucket versioning was disabled on {self.bucket_name}."


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    if subscription_confirmation.is_subscription_confirmation(event):
        subscription_confirmation.confirm_subscription(event)
        return
    rule = S3VersioningDisabled(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()
