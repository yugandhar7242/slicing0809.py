# Dictionary Built-in Methods

#1. dict.clear()
d = {"a": 1, "b": 2}
d.clear()
print(d)  # {}


#---------------
# 2. dict.copy()
d = {"a": 1, "b": 2}
new_d = d.copy()
print(new_d)  # {"a": 1, "b": 2}

#-----------------
# dict.fromkeys(seq, value=None)
# Creates a new dictionary with keys from a sequence and values set to the specified value.
keys = ["a", "b", "c"]
print(dict.fromkeys(keys, 0))  # {"a": 0, "b": 0, "c": 0}


# -----------------
# 4. dict.get(key, default=None)
# Returns the value of the key if it exists, else returns default.
d = {"a": 1}
print(d.get("a"))      # 1
print(d.get("b", 0))   # 0

# -------------------------------------------------------------------
# 5. dict.items()
# Returns a view object containing (key, value) pairs.
d = {"a": 1, "b": 2}
print(list(d.items()))  # [("a", 1), ("b", 2)]

# -------------------------------------------------------------------------
# 6. dict.keys()
# Removes and returns the value of the given key. If not found, returns default./
d = {"a": 1, "b": 2}
print(list(d.keys()))  # ["a", "b"]



# ----------------------------------------------------------------------------
# 7. dict.pop(key, default)
# Removes and returns the value of the given key. If not found, returns default.
d = {"a": 1, "b": 2}
print(d.pop("a"))  # 1
print(d)           # {"b": 2}

# -----------------------------------------------------------------------
# 8. dict.popitem()
# Removes and returns the last inserted (key, value) pair.
d = {"a": 1, "b": 2}
print(d.popitem())  # ("b", 2)

# ------------------------------------------------------------------------------
# 9. dict.setdefault(key, default=None)
# Returns the value of a key. If not found, inserts it with the default value.
d = {"a": 1}
print(d.setdefault("a", 100))  # 1
print(d.setdefault("b", 100))  # 100
print(d)  # {"a": 1, "b": 100}


#-------------------------------------------------------------------------------
# 10. dict.update([other])
# Updates the dictionary with key–value pairs from another dictionary or iterable.
d = {"a": 1}
d.update({"b": 2})
print(d)  # {"a": 1, "b": 2}

# 11. dict.values()
# Returns a view object containing dictionary values.
d = {"a": 1, "b": 2}
print(list(d.values()))  # [1, 2]

#
# Internal Code for fromkeys()
# Python’s fromkeys() method creates a new dictionary with the given sequence of keys and assigns all of them the same default value.
# Let’s write a simple internal implementation:

def custom_fromkeys(keys, value=None):
    new_dict = {}
    for key in keys:
        new_dict[key] = value
    return new_dict

# Example usage
keys = ["a", "b", "c"]
print(custom_fromkeys(keys, 0))  
# Output: {'a': 0, 'b': 0, 'c': 0}

#
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, [])
d["a"].append(1)
print(d)  # {'a': [1], 'b': [1], 'c': [1]}  (all share same list)


#
keys = ["a", "b", "c"]
# Use fromkeys as a dict class method
a = dict.fromkeys(keys, 1)

print(a)