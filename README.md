# reflex-aws-s3-versioning-disabled

A Reflex rule to alert when S3 bucket versioning is disabled

## Usage

To use this rule either add it to your `reflex.yaml` configuration file:
```
rules:
  - reflex-aws-s3-versioning-disabled:
      version: latest
```

or add it directly to your Terraform:
```
...

module "reflex-aws-s3-versioning-disabled" {
  source           = "github.com/cloudmitigator/reflex-aws-s3-versioning-disabled"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-s3-versioning-disabled/blob/master/LICENSE)
