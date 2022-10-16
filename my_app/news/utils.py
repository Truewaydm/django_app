class MyMixin(object):
    mixin_properties = ''

    def get_properties(self):
        return self.mixin_properties.upper()

    def get_upper(self, string):
        if isinstance(string, str):
            return string.upper()
        else:
            return string.title.upper()
