import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def is_spam(email):
    # Defining the stopwords to be removed
    stop_words = set(stopwords.words('english'))
    
    # Tokenizing the email content
    tokens = word_tokenize(email.lower())
    
    # Removing stopwords from the tokens
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Checking if the email contains any spam-related keywords
    spam_keywords = ['viagra', 'lottery', 'free', 'money', 'prize']
    for token in filtered_tokens:
        if token in spam_keywords:
            return True
    
    return False

# Enter E-mail for email inputs
email1 = input("Enter email 1: ")


# Check if the emails are spam or not
if is_spam(email1):
    print("Email 1 is spam.")
else:
    print("Email 1 is not spam.")
