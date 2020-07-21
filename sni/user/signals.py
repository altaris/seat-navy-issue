"""
ODM signal handlers
"""

from typing import Any

import mongoengine.signals as signals

from sni.scheduler import scheduler

from .models import User
from .jobs import update_user_autogroup


@signals.post_save.connect_via(User)
def on_user_post_save(_sender: Any, **kwargs):
    """
    Whenever a NEW user is saved in the database.
    """
    if kwargs.get('created', False):
        usr: User = kwargs['document']
        if usr.character_id == 0:
            return
        # scheduler.add_job(update_user_from_esi, args=(usr, ))
        scheduler.add_job(update_user_autogroup, args=(usr, ))
