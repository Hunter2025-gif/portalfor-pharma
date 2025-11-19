from django.apps import AppConfig

class WorkflowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workflow'
    
    def ready(self):
        """Initialize the workflow app"""
        # Import signals for automatic overrun detection
        from . import signals
