// Select AWS as provider
provider "aws" {

  // AWS access key

  access_key = "{{{credentials.aws_access_key}}}"

  // AWS Secret key

  secret_key = "{{{credentials.aws_secret_key}}}"

  // First AWS region
  // There is technical reasons about using this region instead of others

  region     = "us-east-1"
}

resource "aws_instance" "builder" {

  // Selected AMI
  // This define the operating system ...

  ami           = "{{{command.identifier}}}"

  // By defaul twe choose the cheaper instance type
  // A greather instance could be choosed, but this is charged

  instance_type = "t2.micro"

  // SSH Key
  // This file is generated
  // It is used for SSH / SCP usage

  key_name = "${aws_key_pair.builder.key_name}"

  // Cloud-init
  user_data = "#cloud-config\n{{{application.user_data}}}"

}

resource "aws_key_pair" "builder" {
  public_key = "{{{application.ssh_key}}}"
}
