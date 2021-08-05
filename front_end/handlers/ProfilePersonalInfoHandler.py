from helper import *
import traceback
from BaseUserHandler import *
from content import *


settings_dict = load_yaml_dict(read_file("/Settings.yaml"))
content = Content(settings_dict)

class ProfilePersonalInfoHandler(BaseUserHandler):
    def get(self, user_id):
        try:
            self.render("profile_personal_info.html", page="personal_info", registered_courses=content.get_registered_courses(user_id), user_info=self.get_user_info(), is_administrator=self.is_administrator(), is_instructor=self.is_instructor(), is_assistant=self.is_assistant())
        except Exception as inst:
            render_error(self, traceback.format_exc())

