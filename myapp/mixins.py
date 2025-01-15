class ExtraContentMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = {}
        if self.extra_context:
            context.update(self.extra_context)
        return context
