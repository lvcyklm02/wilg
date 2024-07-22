from django.db import models
from enum import Enum

class Exec(Enum):
    PRESIDENT = "President"
    VICE_PRESIDENT = "Vice President"
    FOOD_STEWARD = "Food Steward"
    TREASURER = "Treasurer"
    HOUSE_MANAGER = "House Manager"
    MEMBERSHIP_COORDINATOR = "Membership Coordinator"
    SECRETARY = "Secretary"
    RUSH_CHAIR = "Rush Chair"
    SOCIAL_CHAIR = "Social Chair"
    RISK_MANAGER = "Risk Manager"
    MEMBER = "Member"

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    classyear = models.PositiveIntegerField()
    description = models.TextField(default="wilglette")
    exec_position = models.CharField(
        max_length=100, 
        choices=[(exec.name, exec.value) for exec in Exec], 
        default=Exec.MEMBER.name
    )

    def __str__(self):
        return self.name
