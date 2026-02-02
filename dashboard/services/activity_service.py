from dashboard.models import NGOActivity

class ActivityService:
    @staticmethod
    def get_available_activities():
        """get all active activities sorted by date"""
        return NGOActivity.objects.filter(is_active=True).order_by('date_time')

    @staticmethod
    def get_all_activities():
        """Get all registered activities (for admin view)"""
        return NGOActivity.objects.all().order_by('date_time')

    @staticmethod
    def create_activity(data):
        """create new NGO activity"""
        return NGOActivity.objects.create(**data)

    @staticmethod
    def update_activity(activity_id, data):
        """update existing NGO activity"""
        NGOActivity.objects.filter(id=activity_id).update(**data)
        return NGOActivity.objects.get(id=activity_id)

    @staticmethod
    def toggle_activity_status(activity_id):
        """toggle NGO activity status"""
        activity = NGOActivity.objects.get(id=activity_id)
        activity.is_active = not activity.is_active
        activity.save()
        return activity