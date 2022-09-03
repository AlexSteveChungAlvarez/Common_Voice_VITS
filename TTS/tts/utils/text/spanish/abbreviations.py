import re

# List of (regular expression, replacement) pairs for abbreviations in english:
abbreviations_es = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("srta", "señorita"),
        ("sr", "señor"),
        ("dr", "doctor"),
        ("lic", "licenciado"),
        ("mag", "magister"),
        ("dr", "doctor"),
        ("co", "colombia"),
        ("jr", "jirón"),
        ("av", "avenida"),
        ("gen", "generación"),
        ("sgt", "siguiente"),
        ("q", "que"),
        ("x", "por"),
        ("pq", "porque"),
        ("ps", "pues"),
    ]
]
