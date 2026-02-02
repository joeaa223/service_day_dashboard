from dashboard.models import NGOActivity

class ActivityService:
    @staticmethod
    def get_available_activities():
        # Only show activities that are not past the cutoff date and are active
        return NGOActivity.objects.filter(is_active=True).order_by('date_time')