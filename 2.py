import matplotlib.pyplot as plt


text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget orci nec nisi lacinia posuere. Fusce eget risus sit amet lectus fringilla ullamcorper. Etiam tempus ultricies velit, vitae pharetra est faucibus nec. In hac habitasse platea dictumst. Pellentesque ac diam id ex placerat luctus. Nunc sed orci eu justo fringilla imperdiet id nec turpis. Quisque eget bibendum ex. Duis nec turpis id libero vehicula sodales vitae non odio. Cras eu dui nec odio ultrices fermentum. Proin vitae quam consectetur, fermentum elit ut, volutpat nisi. Donec sagittis est sed metus blandit, non varius velit interdum.
"""


letter_freq = {}
for char in text:
    if char.isalpha():
        char = char.lower() 
        if char in letter_freq:
            letter_freq[char] += 1
        else:
            letter_freq[char] = 1


sorted_freq = sorted(letter_freq.items())


chars, freqs = zip(*sorted_freq)


plt.figure(figsize=(10, 6))
plt.bar(chars, freqs)
plt.title('Гістограма частоти появи літер у тексті')
plt.xlabel('Літера')
plt.ylabel('Частота')
plt.savefig('letter_histogram.png')
plt.show()
