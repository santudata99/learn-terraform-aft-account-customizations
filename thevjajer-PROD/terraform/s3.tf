data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "thevjajer-prod_bucket" {
  bucket = "aft-thevjajer-prod-${data.aws_caller_identity.current.account_id}"
  acl    = "private"
}
