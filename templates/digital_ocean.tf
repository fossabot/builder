// Select Digital Ocean
provider "digitalocean" {

  // API Token

  token = "{{{credentials.do_token}}}"

}

resource "digitalocean_droplet" "builder" {

  // Selected digital ocean image
  // This define the operating system ...

  image           = "{{{command.identifier}}}"

  // Droplet name

  name = "builder"

  // Droplet region
  // It is configured as owner closest region (Frankfurt)

  region = "fra1"

  // Smallest droplet

  size = "512mb"

  // This file is generated
  // It is used for SSH / SCP usage

  ssh_keys = ["${digitalocean_ssh_key.builder.fingerprint}"]

  // Cloud-init
  user_data = "#cloud-config\n{{{application.user_data}}}"

}

resource "digitalocean_ssh_key" "builder" {
  name = "builder"
  public_key = "{{{application.ssh_key}}}"
}
