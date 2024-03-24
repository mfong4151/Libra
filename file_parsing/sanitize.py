from re import escape, IGNORECASE, compile, split
#Do a regex match for each token and see if they are in the config file

#Does the following:
# 1. Unloads all of the names to sanitize from the json
# 2. Checks the input string for each of the names to sanitize
# 3. Uses a regex match to see if theres any string matches
# 4. Should replaces the strings with a match based on strings that we generated

def sanitze_contents(config, contents: str) -> str:
    names_to_sanitize = config["names_to_sanitize"]
    names_to_sanitize = [escape(name) for name in names_to_sanitize]
    replacements = create_replacements(names_to_sanitize)
    sanitized_patterns = []
    for name in names_to_sanitize:
        if all(c.isupper() for c in name):  # If all characters are uppercase, match as is
            pattern = name
        else:  # Otherwise, match the name with flexibility for internal capital letters
            pattern = ''.join(f'{c}[^A-Z]*' for c in name[:-1]) + name[-1]
        sanitized_patterns.append(pattern)
    pattern = '|'.join(sanitized_patterns)
    
    regex = compile(pattern, IGNORECASE)
    def get_replacement(match):
        matched_text = match.group(0)  # Get the matched text
        # Find the correct case-insensitive match in the replacements dictionary
        for key in replacements.keys():
            if key.lower() == matched_text.lower():
                return replacements[key]
        return matched_text  # Fallback, should not happen    
    
    sanitzed_file_contents= regex.sub(get_replacement, contents)
    return sanitzed_file_contents

def create_replacements(names_to_sanitize: str):
    return {name: create_abbreviation(name) for name in names_to_sanitize}

def create_abbreviation(name):
    pattern = r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])'
    return "".join([c[0] for c in split(pattern, name)])