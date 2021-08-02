import sys
sys.path.append("..")
from app.helper import *
from app.content import *
import traceback
from app.handlers.BaseUserHandler import *
class HelpRequestsHandler(BaseUserHandler):
    def get(self, course):
        try:
            if self.is_administrator() or self.is_instructor_for_course(course) or self.is_assistant_for_course(course):
                self.render("help_requests.html", courses=content.get_courses(), course_basics=content.get_course_basics(course), assignments=content.get_assignments(course), help_requests=content.get_help_requests(course), user_info=self.get_user_info(), is_administrator=self.is_administrator(), is_instructor=self.is_instructor_for_course(course), is_assistant=self.is_assistant_for_course(course))
            else:
                self.render("permissions.html")
        except Exception as inst:
            render_error(self, traceback.format_exc())

