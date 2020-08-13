module "cwe" {
  source      = "git::https://github.com/cloudmitigator/reflex-engine.git//modules/cwe?ref=v2.0.0"
  name        = "S3VersioningDisabled"
  description = "A Reflex rule to alert when S3 bucket versioning is disabled "

  event_pattern = <<PATTERN
{
    "detail-type": ["AWS API Call via CloudTrail"],
    "source": ["aws.s3"],
    "detail": {
        "eventSource": ["s3.amazonaws.com"],
        "eventName": ["PutBucketVersioning"],
        "requestParameters": {
            "VersioningConfiguration": {
                "Status": ["Suspended"]
            }
        }
    }
}
PATTERN
}

