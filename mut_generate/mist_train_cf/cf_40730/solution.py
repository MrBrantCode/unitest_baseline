"""
QUESTION:
Implement a `search` method that performs a case-insensitive search on the `content_auto` field of a model based on a query. The method should only execute the search if the `cleaned_data` attribute exists and contains a 'q' key with a non-empty value. The search results should be returned as a filtered queryset of the model instances.
"""

def search(self):
    if hasattr(self, 'cleaned_data') and 'q' in self.cleaned_data:
        query = self.cleaned_data['q']
        if query:
            return self.get_model().objects.filter(content_auto__icontains=query)