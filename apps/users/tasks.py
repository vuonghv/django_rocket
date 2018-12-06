from celery import shared_task
from celery.utils.log import get_task_logger

from django.utils import timezone

_logger = get_task_logger(__name__)


@shared_task(ignore_result=True)
def demo_scheduled_task():
    _logger.info('Excecute demo scheduled task at {}'.format(timezone.now()))
