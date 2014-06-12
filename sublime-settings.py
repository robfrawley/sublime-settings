import sublime
import sublime_plugin

class ToggleTabCompletionCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        tab_completion = True if settings.get("tab_completion", True) != True else False
        settings.set("tab_completion", tab_completion)
        sublime.save_settings("Preferences.sublime-settings")
        return "off" if tab_completion == False else "on"

    def is_checked(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        return settings.get("tab_completion", True) == True