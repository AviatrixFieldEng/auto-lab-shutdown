# Auto Lab Shutdown
Don't let your resources run overnight!  This Terraform configuration deploys a lambda function that executes at a scheduled interval and shuts down ALL AWS EC2 resources in the target regions.  If you would like it to skip a resource, ensure that that resource has "Shut Down Protection" enabled.  Support for Azure VMs is a next step if anyone wants to contribute to the repo =).

# Usage
Clone the repository.
```
git clone https://github.com/AviatrixFieldEng/auto-lab-shutdown.git
cd auto-lab-shutdown
```

Edit `var.tfvars` with your variables:
* aws_deployment_region -> 
* shutdown_target_aws_regions -> A comma-separated list of AWS regions. These are the regions that the script will attempt to shutdown resources.  Example: `us-east-1,us-east-2`
* lambda_schedule_expression -> A schedule expression to determine when you want the lambda to execute.  The default schedule expression is `cron(0 5 * * ? *)` which translates to 9PM EST daily.  For more information on creating schedule expressions see the following guide: https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html

Execute the Terraform:
```
terraform init
terraform plan --var-file=var.tfvars
terraform apply --var-file=var.tfvars
```
