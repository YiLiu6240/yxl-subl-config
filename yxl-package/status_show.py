# coding=utf8
# referencing package: show files
import sublime, sublime_plugin

class StatusShow(sublime_plugin.EventListener):

    def __init__(self):
        return

    def on_activated(self, view):
        self.update_status(view)
    def on_new(self, view):
        self.update_status(view)
    def on_post_save(self, view):
        self.update_status(view)
    def on_selection_modified_async(self, view):
        self.update_status(view)

    def update_status(self, view):
        is_wrap = view.settings().get('word_wrap')
        if is_wrap == True:
            state_wrap = 'W'
        else:
            state_wrap = 'NW'
        is_centered = view.settings().get('draw_centered')
        n_wrapWidth = view.settings().get('wrap_width')
        if n_wrapWidth == 0:
            state_wrapWidth = "Auto"
        else:
            state_wrapWidth = str(n_wrapWidth)
        state_match = view.settings().get('auto_match_enabled')
        if state_match == 0:
            state_match = ", NOT matching"
        else:
            state_match = ""
        view.set_status('ShowWrapStatus', "-%s: %s%s%s-" % (state_wrap, state_wrapWidth, ("C" if is_centered == True else ""), state_match) )
