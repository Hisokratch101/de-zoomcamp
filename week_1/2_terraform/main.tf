terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
    credentials = "./keys/my-creeds.json"
  project = "eminent-yen-411522"
  region  = "us-central1"
}

resource "google_storage_bucket" "auto-expire"  {
  name          = "eminent-yen-411522-terra-bucket"
  location      = "US"
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}