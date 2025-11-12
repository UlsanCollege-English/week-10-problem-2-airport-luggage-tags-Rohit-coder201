"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""

# Step 4: create unique marker objects
EMPTY = object()
DELETED = object()

def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    return [EMPTY for _ in range(m)]

def _find_slot_for_insert(t, key):
    """Return index to insert/overwrite (may return DELETED slot). Return None if full."""
    m = len(t)
    h = hash(key) % m
    first_deleted = None
    
    for i in range(m):
        idx = (h + i) % m
        slot = t[idx]
        
        if slot is EMPTY:
            # Empty slot: prefer previously seen DELETED, else this empty
            return first_deleted if first_deleted is not None else idx
        
        if slot is DELETED:
            if first_deleted is None:
                first_deleted = idx
            continue
        
        # slot is a (key, value) tuple
        if slot[0] == key:
            return idx  # overwrite existing key
    
    # table probed fully
    return first_deleted  # may be None if no DELETED found

def _find_slot_for_search(t, key):
    """Return index where key is found; else None. DELETED does not stop search."""
    m = len(t)
    h = hash(key) % m
    
    for i in range(m):
        idx = (h + i) % m
        slot = t[idx]
        
        if slot is EMPTY:
            return None  # never seen -> not present
        
        if slot is DELETED:
            continue  # skip deleted, keep searching
        
        if slot[0] == key:
            return idx
    
    return None

def put_open(t, key, value):
    """Insert or overwrite (key, value). Return True on success, False if table is full."""
    idx = _find_slot_for_insert(t, key)
    if idx is None:
        return False
    t[idx] = (key, value)
    return True

def get_open(t, key):
    """Return value for key or None if not present."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return None
    return t[idx][1]

def delete_open(t, key):
    """Delete key if present. Return True if removed, else False."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return False
    t[idx] = DELETED
    return True

if __name__ == "__main__":
    # Optional manual checks (not graded)
    pass