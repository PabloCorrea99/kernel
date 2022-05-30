from django.apps import AppConfig
from .services.kernel_service import Kernel_Service
class KernelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kernel'
