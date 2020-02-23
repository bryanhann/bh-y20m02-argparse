def parents4dott(dott):
    def _iter_parents4dott(dott):
        parts = dott.split('.')
        while parts:
            yield '.'.join( parts )
            parts.pop()
    return list(_iter_parents4dott(dott))


