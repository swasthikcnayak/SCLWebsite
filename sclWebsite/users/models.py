from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from teams.models import Teams

BATCH = (
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
    ("2015", "2015"),
    ("2016", "2016"),
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("None", "None"),
)

ROLE = (
    ('1', 'MENTEE'),
    ('2', 'MENTOR'),
    ('3', 'ADVISOR')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=20, choices=ROLE, help_text='Role of the user', default='1')
    batch = models.CharField(max_length=10, choices=BATCH, default="2019", null=True)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.PositiveBigIntegerField(default=None, blank=True, null=True)
    college = models.CharField(max_length=300, default=None, blank=True, null=True)
    degree = models.CharField(max_length=100, default=None, blank=True, null=True)
    branch = models.CharField(max_length=100, default=None, blank=True, null=True)
    profession = models.CharField(max_length=100, default=None, blank=True, null=True)
    guidance = models.TextField(default=None, blank=True, null=True)
    linkedin = models.URLField(default=None, blank=True, null=True)
    github = models.URLField(default=None, blank=True, null=True)

    def __str__(self):
        if self.name:
            try:
                return f'{self.name} - {self.team.name}'
            except:
                return f'{self.name}'
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_team_name(self):
        team = self.teams_set.first()
        if team:
            return team.name
        else:
            return ''

    @property
    def get_role(self):
        if self.role == '2':
            return 'Mentor'
        elif self.role == '1':
            return 'Participant'
        else:
            return 'Advisor'


STATUS = (
    ('1', 'INCOMPLETE'),
    ('2', 'BOOKED')
)


class Request(models.Model):
    date = models.DateField(auto_now_add=True, blank=True,null=True)
    requested_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentee_request')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, help_text='Status of the request', default='1')
