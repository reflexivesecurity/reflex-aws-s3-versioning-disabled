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

    def remediate(self):
        """ Fix the non-compliant resource """
        self.enable_versioning_for_bucket()

    def enable_versioning_for_bucket(self):
        self.client.put_bucket_versioning(
            Bucket=self.bucket_name, VersioningConfiguration={"Status": "Enabled"}
        )

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        message = f"S3 bucket versioning was disabled on {self.bucket_name}."
        if self.should_remediate():
            message += " Versioning has been re-enabled for the bucket."
        return message


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = S3VersioningDisabled(event_payload)
    rule.run_compliance_rule()
