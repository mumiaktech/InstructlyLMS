# middleware.py
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class RoleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user

        # Check if user is authenticated
        if user.is_authenticated:
            # Access control for Instructor
            if request.path.startswith('/instructor/') and not user.groups.filter(name='Instructor').exists():
                return HttpResponseForbidden("You don't have permission to access the instructor page.")

            # Access control for Student
            if request.path.startswith('/student/') and not user.groups.filter(name='Student').exists():
                return HttpResponseForbidden("You don't have permission to access the student page.")
        
        # Allow access if the user is not authenticated
        return None
