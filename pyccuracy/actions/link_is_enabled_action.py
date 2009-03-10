from pyccuracy.errors import *
from pyccuracy.page import Page
from pyccuracy.actions.action_base import *
from pyccuracy.actions.element_is_visible_base import *

class LinkIsEnabledAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(LinkIsEnabledAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["link_is_enabled_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        link_name = values[0]		
        link = self.resolve_element_key(context, Page.Link, link_name)
        self.assert_element_is_visible(link, self.language["link_is_visible_failure"] % link_name)        
        
        error_message = self.language["link_is_enabled_failure"]
        if not self.browser_driver.is_element_enabled(link):
            self.raise_action_failed_error(error_message % link_name)
