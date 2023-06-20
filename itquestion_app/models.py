from django.db import models




class RequestModel(models.Model):
    Requestor = models.TextField()
    Beneficiary = models.TextField()
    AssetNumber = models.TextField()
    Category = models.TextField()
    Comment = models.TextField()

    def is_valid(self):
        pass





