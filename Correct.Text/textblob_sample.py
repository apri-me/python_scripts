from textblob import TextBlob

my_text = """Heello thise is Aprime. 
I wantt to chec iff textBlob workss or notr
"""

my_blob = TextBlob(my_text)
print(my_blob.correct())