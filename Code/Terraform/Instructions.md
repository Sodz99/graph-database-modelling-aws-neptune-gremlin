### Prerequisites:

Install AWS CLI and configure your credentials using aws configure. Install Terraform on your system.

### AWS CLI Installation Link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


### Configure AWS CLI on Your System

## Execute this command on Terminal to setup AWS CLI on the local system
```aws configure```


1. Enter your AWS Access Key ID and Secret Access Key.
2. Specify the region where your IAM user has access.


This sets up local system to interact with AWS services using the CLI and necessary for the execution using terraform.


### Terraform Installation Link

https://developer.hashicorp.com/terraform/downloads

###### Install Terraform on Windows 

1. https://releases.hashicorp.com/terraform/1.13.4/terraform_1.13.4_windows_amd64.zip
2. Download the ZIP file and extract it.
3. Copy the extracted terraform.exe file.
4. Open File Explorer → navigate to C:\Program Files.
5. Create a new folder named Terraform and paste the terraform.exe file inside it.
6. Add Terraform to your system PATH:
7. Click Environment Variables → under System variables, select Path → click Edit.
8. Click New, then paste the Terraform folder path (e.g., C:\Program Files\Terraform) and Click OK to save changes.

Open Command Prompt and verify installation:

```terraform -version```


###### Install Terraform on macOS

If you don’t have Homebrew installed, first install it by executing this command on the terminal:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


## Run this commmand to install terraform on macOS
1. brew tap hashicorp/tap
2. brew install hashicorp/tap/terraform


### Note:

1. After the S3 bucket is created using Terraform, make sure you follow the data-preparation steps shown in the video. Those steps explain how to prepare the dataset and upload it to the S3 bucket.

2. Please note that the Neptune notebook cannot be created using Terraform. After the Neptune database is created, you must create the Neptune notebook manually from the AWS Console UI inside the Neptune cluster section.

##### Terraform Commands
Step 1: Initialize Terraform
```terraform init```


This command sets up your working directory for Terraform. It downloads the required providers and prepares the environment for deployment.


Step 2: Preview Terraform Plan
```terraform plan```


This command shows all the changes Terraform will make to infrastructure. You can review the changes safely before actually applying them.

Step 3: Validate Terraform Configuration


This command checks all Terraform files for syntax errors. It ensures that configuration is correct before applying it.

Step 4: Apply Terraform Changes
```terraform apply```


This command applies your Terraform configuration to create or update resources in AWS. You will be prompted to confirm before Terraform makes any changes.


Step 5: Apply Terraform Changes Automatically
```terraform apply --auto-approve```


This command applies all Terraform changes without asking for confirmation. It is useful for automated deployments or pipelines.


Step 6: Destroy Terraform Resources
```terraform destroy```

This command removes all resources that were created and managed by Terraform. Use this command carefully to avoid accidentally deleting important resources.


Step 7: Set EC2 Key File Permissions on Windows

```icacls "terraform-ec2-key-graph.pem" /inheritance:r```

```icacls "terraform-ec2-key-graph.pem" /grant:r "%USERNAME%:R"```


These commands remove inherited permissions and grant read-only access to the current user. This is necessary to avoid permission warnings when connecting to your EC2 instance.