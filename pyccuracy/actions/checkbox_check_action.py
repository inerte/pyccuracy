from pyccuracy.errors import *
from pyccuracy.page import Page
from pyccuracy.actions.action_base import *
from pyccuracy.actions.element_is_visible_base import *

class CheckboxCheckAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(CheckboxCheckAction, self).__init__(browser_driver, language)
    def matches(self, line):
        reg = self.language["checkbox_check_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        checkbox_name = values[0]
        checkbox = self.resolve_element_key(context, Page.Checkbox, checkbox_name)
        self.assert_element_is_visible(checkbox, self.language["checkbox_is_visible_failure"] % checkbox_name)
        self.browser_driver.checkbox_check(checkbox)
