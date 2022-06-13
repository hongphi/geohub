import json

from geohub.services.models import ActivityLog


def create_log(path, meta_data):
    data = json.dumps(meta_data)
    ActivityLog(path=path, meta_data=meta_data).save()
