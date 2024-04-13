

def categorize_transactions(transactions, preset_categories):
    """
    Categorizes transactions based on a preset list of categories and keywords.
    
    Args:
    - transactions (list of str): List of transaction names to categorize.
    - preset_categories (dict): Dictionary where keys are categories and values are lists of keywords associated with each category.
    
    Returns:
    - categorized_transactions (dict): Dictionary where keys are categories and values are lists of transactions belonging to each category.
    """
    categorized_transactions = {category: [] for category in preset_categories}

    for transaction in transactions:
        categorized = False
        for category, keywords in preset_categories.items():
            for keyword in keywords:
                if keyword.lower() in transaction.lower():
                    categorized_transactions[category].append(transaction)
                    categorized = True
                    break
            if categorized:
                break
        if not categorized:
            categorized_transactions["Uncategorized"].append(transaction)

    return categorized_transactions

# Preset list of categories and keywords
preset_categories = {
    "Groceries": ["grocery", "food", "supermarket"],
    "Dining Out": ["restaurant", "dinner", "cafe"],
    "Online Shopping": ["amazon", "online shopping", "ecommerce"],
    "Transportation": ["gas", "fuel", "car"],
    "Housing": ["rent", "mortgage", "housing"]
}


