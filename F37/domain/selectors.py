# Domain layer: Contains selectors for querying domain-specific data.
def select_active_items(items):
    # TODO: implement selection logic
    return [item for item in items if item.get('active')]
