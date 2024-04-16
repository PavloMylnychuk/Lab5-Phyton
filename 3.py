import matplotlib.pyplot as plt


text = """
Suspendisse potenti. Nullam accumsan sollicitudin arcu, eget fermentum lorem dictum id. Mauris cursus viverra leo, eget laoreet odio finibus nec. Curabitur fringilla diam at orci fringilla, non suscipit libero dignissim. Pellentesque quis neque eu nisl posuere suscipit non at libero. Maecenas vel consequat leo. Sed in erat rutrum, dignissim risus eu, ullamcorper enim. Aliquam auctor scelerisque massa ut iaculis. Vivamus ut leo eu neque suscipit congue. Integer auctor libero at sem rhoncus, eget euismod sem volutpat. Nullam venenatis arcu nec ipsum tempor, nec tincidunt risus ullamcorper. Praesent bibendum tincidunt odio, sed pulvinar libero molestie eu.
Nullam id aliquet nisi. Aliquam pretium eros non lacus tincidunt, quis suscipit elit ullamcorper. Sed scelerisque ex nec nulla vehicula, quis volutpat turpis consequat. Quisque non bibendum lectus. Vestibulum ac eros vel nisi ullamcorper lobortis. In hac habitasse platea dictumst. Mauris nec tempor est. Vestibulum lacinia congue sapien, a volutpat sapien dignissim eu. Donec fermentum, enim id ullamcorper sagittis, felis diam ultrices nisl, non venenatis odio felis eu nisl. Sed vitae eros vitae justo iaculis venenatis. Curabitur elementum ipsum sit amet sapien fringilla convallis. Phasellus nec feugiat lorem.
Phasellus maximus tellus nec nulla ultrices, ac fringilla quam lobortis. Proin quis velit odio. Fusce commodo ipsum in risus varius, nec sodales metus scelerisque. Vestibulum vestibulum, nulla eu pretium facilisis, nulla ex efficitur purus, ac bibendum lectus nunc a felis. Maecenas pretium, nunc sed suscipit sollicitudin, tortor ipsum tincidunt nisi, eget fermentum risus ipsum vel risus. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis tempor sit amet ex nec varius. Integer nec placerat ligula, nec pellentesque turpis. Cras vestibulum, magna sit amet tempor varius, turpis enim gravida purus, ut tincidunt ante metus quis justo. Donec maximus diam nec nisl ultricies, at faucibus velit vehicula.
Donec varius nibh non sapien congue, et varius risus sollicitudin. In nec semper nulla. Nulla commodo vehicula neque sit amet commodo. Vivamus vestibulum tortor vel augue condimentum, sed aliquam mauris commodo. Integer feugiat metus at nulla vulputate, vitae pharetra sapien molestie. Vestibulum a tincidunt eros. Fusce nec quam pharetra, molestie velit ac, lacinia sem. Ut sollicitudin nisi ut mauris auctor, ac varius mauris semper. Fusce quis mauris neque. Nam id diam magna. Nam placerat, nisi vel dictum volutpat, arcu neque commodo ligula, vitae malesuada elit elit eu velit. Cras scelerisque sollicitudin nunc eget rutrum.
"""

sentences = text.split('. ')


ordinary_count = 0
question_count = 0
exclamation_count = 0
ellipsis_count = 0


for sentence in sentences:
    if sentence.endswith('?'):
        question_count += 1
    elif sentence.endswith('!'):
        exclamation_count += 1
    elif sentence.endswith('...'):
        ellipsis_count += 1
    else:
        ordinary_count += 1


labels = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапкові']
counts = [ordinary_count, question_count, exclamation_count, ellipsis_count]

plt.figure(figsize=(10, 6))
plt.bar(labels, counts)
plt.title('Гістограма типів речень у тексті')
plt.xlabel('Тип речення')
plt.ylabel('Кількість')
plt.savefig('sentence_types_histogram.png')
plt.show()
