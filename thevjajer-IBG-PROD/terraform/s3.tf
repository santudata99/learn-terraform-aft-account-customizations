data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "thevjajer-ibg-prod_bucket" {
  bucket = "aft-thevjajer-ibg-prod-${data.aws_caller_identity.current.account_id}"
  acl    = "private"
}
