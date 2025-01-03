# <copyright_statement>
#   CodeBuddy: A programming assignment management system for short-form exercises
#   Copyright (C) 2023 Stephen Piccolo
#   This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details. You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
# </copyright_statement>

from BaseUserHandler import *

class ProfileStudentHelpRequestsHandler(BaseUserHandler):
    async def get(self):
        try:
            self.render("profile_student_help_requests.html", page="help_requests", result=None, user_info=self.user_info, help_requests=self.content.get_student_help_requests(self.get_current_user()), is_administrator=self.is_administrator)
        except Exception as inst:
            render_error(self, traceback.format_exc())