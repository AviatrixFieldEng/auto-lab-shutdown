variable "aws_deployment_region" {
  default = "us-east-2"
}

variable "shutdown_target_aws_regions" {
    description = "List of AWS regions comma separated to scan for resources to shutdown.  Defaults to all AWS regions"
    default = "all"
}

variable "lambda_schedule_expression" {
  description = "Schedule to execute the in crontab format.  Defaults to 9PM EST"
  default = "cron(0 5 * * ? *)"
}