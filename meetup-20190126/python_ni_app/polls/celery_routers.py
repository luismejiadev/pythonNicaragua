# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

class PollRouter(object):

    def route_for_task(self, task, args=None, kwargs=None):
        if task == "polls.tasks.add":
            return {
                "queue": "add"
            }
        return None
