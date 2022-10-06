from datetime import datetime

def create_context_processor(app):
    @app.context_processor
    def context_processor():
        """Add custom variables to all app contexts."""
        return {
            'current_year': lambda: datetime.utcnow().year
        }
