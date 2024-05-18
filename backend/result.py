from processing import classify_message

# Test the new sentence
new_message = "Let's engage in money laundering."
result = classify_message(new_message)
print(f'The message "{new_message}" is classified as: {result}')
