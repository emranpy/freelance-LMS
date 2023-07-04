from BaseUserHandler import *
import datetime as dt

class ViewAtRiskStudentsHandler(BaseUserHandler):
    async def get(self, course_id, recent_submissions_days_threshold):
        try:
            if self.is_administrator or await self.is_instructor_for_course(course_id) or await self.is_assistant_for_course(course_id):
                course_basics = await self.get_course_basics(course_id)
                assignments = await self.get_assignments(course_basics)

                self.render("view_at_risk_students.html", no_recent_submissions=self.content.get_students_no_recent_submissions(course_id, recent_submissions_days_threshold), recent_submissions_days_threshold=int(recent_submissions_days_threshold), course_basics=course_basics, courses=self.courses, user_info=self.user_info, is_administrator=self.is_administrator)
            else:
                self.render("permissions.html")
        except Exception as inst:
            render_error(self, traceback.format_exc())