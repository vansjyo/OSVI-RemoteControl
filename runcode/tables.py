import django_tables2 as tables
from .models import Pycode, UserVids


class PycodeTable(tables.Table):
    class Meta:
        model = Pycode
        template_name = 'django_tables2/bootstrap.html'

class UserVidsTable(tables.Table):
    class Meta:
        model = UserVids
        template_name = 'django_tables2/bootstrap.html'
