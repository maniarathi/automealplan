# perishibility currently 14, 30, or 100 (basically doesn't go bad)
# rareness should be "common", "uncommon" or "rare"
# special quantities: "any": can buy any amount (e.g, cremini mushies)
#                     "all": can by "infinite" amount (e.g, red pepper flakes)

INGREDIENTS = {
    "egg": {
        "perishability": 30,
        "purchase_quantities": ["6"],
        "rareness": "common"
    },
    "kale": {
        "perishability": 14,
        "purchase_quantities": ["1 bunch"],
        "rareness": "common"
    },
    "scallions": {
        "perishability": 14,
        "purchase_quantities": ["1"],
        "rareness": "common"
    },
    "dried shiitake mushrooms": {
        "perishability": 30,
        "purchase_quantities": ["1 oz"],
        "rareness": "common"
    },
    "peppadew": {
        "perishability": 100,
        "purchase_quantities": ["1"],
        "rareness": "common"
    },
    "red pepper flakes": {
        "perishability": 100,
        "purchase_quantities": ["all"],
        "rareness": "common"
    },
    "pearled barely": {
        "perishability": 100,
        "purchase_quantities": ["30 oz"],
        "rareness": "common"
    },
    "cremini mushrooms": {
        "perishability": 14,
        "purchase_quantities": ["any"],
        "rareness": "common"
    },
    "garlic": {
        "perishability": 30,
        "purchase_quantities": ["1"],
        "rareness": "common"
    },
    "parmesan": {
        "perishability": 100,
        "purchase_quantities": ["8 oz"],
        "rareness": "common"
    },
    "coconut aminos": {
        "perishability": 30,
        "purchase_quantities": [],
        "rareness": "rare"
    },
    "soy sauce": {
        "perishability": 100,
        "purchase_quantities": ["20 oz"],
        "rareness": "common"
    }
}
