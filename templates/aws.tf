provider "aws" {
  access_key = "{{{credentials.aws_access_key}}}"
  secret_key = "{{{credentials.aws_secret_key}}}"
  region     = "us-east-1"
}

resource "aws_instance" "builder" {
  ami           = "{{{command.identifier}}}"
  instance_type = "t2.micro"
}
