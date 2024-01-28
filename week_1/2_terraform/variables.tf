variable "credentials"{
    description = "My credentials"
    default = "./keys/my-creeds.json"
}   
variable "project" {
  description = "Project id"
  default     = "eminent-yen-411522"
}

variable "region" {
  description = "region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "eminent-yen-411522-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}