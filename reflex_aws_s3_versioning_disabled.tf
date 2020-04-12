module "reflex_aws_s3_versioning_disabled" {
  source           = "git::https://github.com/cloudmitigator/reflex-engine.git//modules/cwe_lambda?ref=v0.5.8"
  rule_name        = "S3VersioningDisabled"
  rule_description = "A Reflex rule to alert when S3 bucket versioning is disabled "

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

  function_name   = "S3VersioningDisabled"
  source_code_dir = "${path.module}/source"
  handler         = "reflex_aws_s3_versioning_disabled.lambda_handler"
  lambda_runtime  = "python3.7"
  environment_variable_map = {
    SNS_TOPIC = var.sns_topic_arn,
  }

  queue_name    = "S3VersioningDisabled"
  delay_seconds = 0

  target_id = "S3VersioningDisabled"

  sns_topic_arn  = var.sns_topic_arn
  sqs_kms_key_id = var.reflex_kms_key_id
}
