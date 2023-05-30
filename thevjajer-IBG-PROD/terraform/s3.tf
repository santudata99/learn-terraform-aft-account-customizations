data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "thevjajer-IBG-PROD_bucket" {
  bucket = "aft-thevjajer-IBG-PROD-${data.aws_caller_identity.current.account_id}"
  acl    = "private"
}
