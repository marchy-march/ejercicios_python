import random

list1 = []
for x in range(1,1001):
    if x%7==0:
        list1.append(x)

list2 = [x for x in range(1,1001) if x%7 ==0]
print(list2)


Lst1 = []
for x in range(1,1001): 
    if "3" in str(x): 
        Lst1.append(x)

Lst1 = [x for x in range(1,1001) if "3" in str(x)]
print(Lst1)


list5 = ["cat", "dog", "iguana", "tiger", "elephant"]
no_vowels = []
vowels = ["a", "e", "i", "o", "u"]
# for i in range(len(list5)):
#     for x in vowels:
#         if x not in list5[i]:
#             continue
#         else:
#             no_vowels.append(list5[i].replace(x,""))


for i in list5:
    no_vowels.append("".join([l for l in i if l not in vowels]))

            

print(no_vowels)





list7 = []
lst8 = [random.randint(1,100) for x in range(101)] 
lst9 = [random.randint(1,100) for x in range(101)] 
for i in lst8:
    if i in lst9:
        list7.append(i)

print(sorted(lst8))
print(sorted(lst9))

list10 = [i for i in lst8 if i in lst9]
print(sorted(list10))



#HOMEWORK
#encontrar todas las palabras de una lista que tenga 5 o menos letras
word_list = ['All', 'the', 'Best', 'Cowboys', 'Have', 'Daddy', 'Issues', 'Beira', 'Mar', 'Brasil', 'Ben', 'Franklin', 'O', 'Último', 'Romântico', '(Ao', 'Vivo)', 'Freewheel', 'Burning', "That's", 'The', 'Way', 'Mellowship', 'Slinky', 'In', 'B', 'Major', 'Diga', 'Lá,', 'Coração', 'Come', 'As', 'You', 'Are', 'The', 'Spirit', 'Of', 'Radio', 'Midnight', 'Blue', 'Se', 'Liga', 'Carnival', 'Of', 'Sorts', 'Paranoid', 'Got', 'That', 'Feeling', 'What', 'Is', 'And', 'What', 'Should', 'Never', 'Be', 'The', 'Zephyr', 'Song', 'Run', 'Silent', 'Run', 'Deep', 'Realidade', 'Virtual', 'Há', 'Quanto', 'Tempo', 'Oprah', 'As', 'Aparências', 'Enganam', 'Confidence', 'Man', 'Os', 'Alquimistas', 'Estão', 'Chegando', 'Springsville', 'Wake', 'Up', 'Ave', 'Maria', 'A', 'Banda', 'Fight', 'Fire', 'With', 'Fire', 'Sound', 'of', 'a', 'Gun', 'RV', 'É', 'que', 'Nessa', 'Encarnação', 'Eu', 'Nasci', 'Manga', 'Do', 'The', 'Evolution', 'Prowler', 'They', "Can't", 'Take', 'That', 'Away', 'From', 'Me', 'The', 'Real', 'Problem', 'Tempus', 'Fugit', 'Diwali', "Bring'em", 'Back', 'Alive', 'Time', 'Is', 'On', 'My', 'Side', 'The', 'Ocean', 'Minority', 'The', 'Messenger', 'Quanta', '(Live)', 'Ironic', 'Faraó', 'Divindade', 'Do', 'Egito', 'Nabucco:', 'Chorus,', '"Va,', 'Pensiero,', "Sull'ali", 'Dorate"', 'Redundant', 'Leave', 'Us', 'Leap', 'Flight', 'Of', 'The', 'Icarus', 'Adoled', '(Ocean)', "Let's", 'See', 'Action', 'Toccata', 'and', 'Fugue', 'in', 'D', 'Minor,', 'BWV', '565:', 'I.', 'Toccata', 'Blind', 'Curve:', 'Vocal', 'Under', 'A', 'Bloodlight', '/', 'Passing', 'Strangers', '/', 'Mylo', '/', 'Perimeter', 'Walk', '/', 'Threshold', 'Dirty', 'Little', 'Thing', 'Só', 'Tinha', 'De', 'Ser', 'Com', 'Você', 'Slug', 'Black', 'Mountain', 'Side', 'Pensamento', 'Even', 'Better', 'Than', 'The', 'Real', 'Thing', 'Powerslave', 'Loud', 'Love', '2', 'Minutes', 'To', 'Midnight', 'Out', 'Of', 'Exile', 'Spank', 'Thru', 'London', 'Calling', 'Break', 'on', 'Through', 'We', 'Are', 'The', 'Champions', 'Hard', "Lovin'", 'Man', 'Jingo', '200', 'Years', 'Old', 'Santa', 'Clara', 'Clareou', 'Juventude', 'Transviada', '(Ao', 'Vivo)', 'Rollover', 'D.J.', 'Leave', 'God', 'Part', 'II', 'Cold', 'Gin', 'Sister', 'Morphine', 'Nefertiti', 'Take', 'the', 'Box', 'Good', 'Riddance', '(Time', 'Of', 'Your', 'Life)', "Can't", 'Keep', 'Wall', 'Of', 'Denial', 'If', 'God', 'Will', 'Send', 'His', 'Angels', 'Viradouro', 'Surrender', 'Funky', 'Monks', 'Back', 'in', 'the', 'Village', 'Freedom', 'For', 'My', 'People', 'Um', 'Jantar', 'Pra', 'Dois', 'Hang', "'Em", 'High', "Spirit's", 'in', 'the', 'Material', 'World', 'Maquinarama', 'Believe', 'The', 'Wait', 'Near', 'Wild', 'Heaven', 'Desordem', 'Canário', 'Do', 'Reino', 'O', 'Pulso', 'Fear', 'Of', 'The', 'Dark', 'Every', 'Little', 'Thing', 'She', 'Does', 'is', 'Magic', 'O', 'Livro', 'Dos', 'Dias', 'Arc', 'All', 'My', 'Life', 'Put', 'You', 'Down', 'Já', 'Foi', 'Gatas', 'Extraordinárias', 'Carta', 'Ao', 'Tom', '74', 'Babyface', 'Light', 'My', 'Way', 'Solar', 'Something', 'Nice', 'Back', 'Home', 'Murder', 'On', 'the', 'Rising', 'Star', 'Think', 'Ando', 'Meio', 'Desligado', 'Trac', 'Trac', 'Whiplash', 'Brave', 'New', 'World', 'A', 'Statistic', 'Manifest', 'Destiny', 'Falamansa', 'Song', 'Song', 'For', 'Lorraine', 'Diamante', 'De', 'Mendigo', 'Corcovado', '(Quiet', 'Nights', 'Of', 'Quiet', 'Stars)', 'KKK', 'Bitch', 'União', 'Da', 'Ilha', 'Your', 'Mirror', 'Maybe', "I'm", 'A', 'Leo', 'Not', 'The', 'Doctor', 'Suck', 'My', 'Kiss', 'The', 'Unforgettable', 'Fire', 'You', 'Learn', 'Losing', 'My', 'Religion', 'Concert', 'pour', '4', 'Parties', 'de', 'V**les,', 'H.', '545:', 'I.', 'Prelude', 'Flip', 'The', 'Switch', 'Enquanto', 'O', 'Mundo', 'Explode', 'So', 'Central', 'Rain', 'Riviera', 'Paradise', 'Caffeine', 'Palco', '(Live)', 'Walk', 'On', 'Layla', 'End', 'Of', 'The', 'Night', 'Revolution', 'Sweet', 'Child', "O'", 'Mine', 'Heaven', 'Can', 'Wait', 'Love', 'Comes', 'The', '23rd', 'Psalm', 'Dude', '(Looks', 'Like', 'A', 'Lady)', 'Minas', 'Pride', '(In', 'The', 'Name', 'Of', 'Love)', 'Put', 'The', 'Finger', 'On', 'You', 'Get', 'On', 'The', 'Snake', 'A', 'Festa', 'Do', 'Santo', 'Reis', 'Wanted', 'Dread', 'And', 'Alive', 'Tanto', 'Tempo', 'Infinite', 'Dreams', 'Feirinha', 'da', 'Pavuna/Luz', 'do', 'Repente/Bagaço', 'da', 'Laranja', 'Motéis', 'Corduroy', 'Why', 'Go', 'Hail,', 'Hail', 'Flight', 'Of', 'The', 'Rat', 'Groovus', 'Interruptus', 'Wrathchild', 'Nene', '2001', 'Nightrain', 'Elderly', 'Woman', 'Behind', 'The', 'Counter', 'In', 'A', 'Small', 'Town', 'The', 'Outlaw', 'Torn', 'Battery', 'Lords', 'Of', 'The', 'Backstage', 'The', 'River', '(Remix)', 'Bowels', 'Of', 'The', 'Devil', "Don't", 'Go', 'Back', 'To', 'Rockville', 'Macô', 'Love', 'Is', 'The', 'Colour', 'Without', 'You', 'Phantom', 'Lord', "Don't", 'Take', 'Your', 'Love', 'From', 'Me', 'On', 'The', 'Run', 'Set', 'It', 'Off', 'Get', 'Me', 'Outta', 'Here', 'Surprise!', "You're", 'Dead!', 'Linha', 'Do', 'Horizonte', 'Cigano', 'She', 'Wears', 'Black', 'Losfer', 'Words', 'Blood', 'Brothers', 'War', 'of', 'the', 'Gods,', 'Pt.', '2', 'Let', 'There', 'Be', 'Rock', 'The', 'Negotiation', 'Vida', 'Boa', 'Fast', 'And', 'Loose', "They're", 'Red', 'Hot', 'Dr.', 'Heckyll', '&', 'Mr.', 'Jive', 'Territorial', 'Pissings', 'The', 'Pan', 'Piper', 'Ali', 'Sangue', 'De', 'Bairro', 'Beijo', 'do', 'Olhar', 'Pretinha', 'Fortuneteller', 'Surrender', 'Killers', 'Be', 'Quick', 'Or', 'Be', 'Dead', 'Pau-De-Arara', 'On', 'Mercury', 'On', 'A', 'Plain', 'Lost', '(Pilot,', 'Part', '2)', 'O', 'Bicho', 'Tá', 'Pregando', "Lookin'", 'For', 'A', 'Reason', 'Be', 'Yourself', 'Não', 'Sei', 'O', 'Que', 'Eu', 'Quero', 'Da', 'Vida', 'Shamrocks', 'And', 'Shenanigans', '(Boom', 'Shalock', 'Lock', 'Boom/Butch', 'Vig', 'Mix)', 'Talk', 'About', 'The', 'Passion', 'Rasul', 'Tim', 'Tim', 'Por', 'Tim', 'Tim', 'Pini', 'Di', 'Roma', '(Pinien', 'Von', 'Rom)', '\\', 'I', 'Pini', 'Della', 'Via', 'Appia', 'Die', 'Die', 'My', 'Darling', 'Enter', 'Sandman', 'Harvester', 'Of', 'Sorrow', 'Child', 'In', 'Time', '(Son', 'Of', 'Aleric', '-', 'Instrumental)', "I'm", 'A', 'Greedy', 'Man', 'Pt.1', 'The', 'One', 'I', 'Love', 'Onibusfobia', 'O', 'Estrangeiro', 'Voce', 'Nao', 'Entende', 'Nada', '-', 'Cotidiano', 'Planet', 'Home', 'Give', 'Peace', 'a', 'Chance', 'Flor', 'De', 'Lis', 'Esperando', 'Por', 'Mim', 'Iron', 'Maiden', 'Dead', 'Horse', 'Sheer', 'Heart', 'Attack', 'Light', 'My', 'Fire', 'Chão', 'de', 'Giz', '(Elba', 'Ramalho)', 'Waiting', 'On', 'A', 'Sign', 'Wildest', 'Dreams', 'Murders', 'In', 'The', 'Rue', 'Morgue', 'Pot-Pourri', 'N.º', '4', 'The', 'Witch', 'Sobremesa', 'Outbreak', 'Construção', '/', 'Deus', 'Lhe', 'Pague', 'My', 'Funny', 'Valentine', '(Live)', 'Angel', 'Heaven', 'Can', 'Wait', 'Company', 'Man', 'Perfect', 'Sleep', 'On', 'The', 'Sidewalk', 'Domingo', 'Seu', 'Balancê', 'Alive', 'Get', 'Up', '(I', 'Feel', 'Like', 'Being', 'A)', 'Sex', 'Machine', 'Blood', 'Brothers', "Runnin'", 'With', 'The', 'Devil', 'Milk', 'It', 'Gone', 'When', 'You', 'Gonna', 'Learn', '(Digeridoo)', 'Angela', 'Locomotive', 'The', 'Angel', 'And', 'The', 'Gambler', 'Bye', 'Bye', 'Blackbird', 'Angel', 'Of', 'Harlem', 'Hello', 'Mary', 'Lou', 'Bushleager', 'The', 'Worst', 'Saint', 'Of', 'Me', 'Dirty', 'Water', 'Dog', 'Times', 'of', 'Trouble', 'Jerusalem', 'Pretty', 'Noose', 'Bê-a-Bá', 'Esquinas', 'Wasting', 'Love', 'Hot', 'Dog', 'As', 'Rosas', 'Não', 'Falam', '(Beth', 'Carvalho)', 'Boogie', 'Blues', 'Numbers', 'Beach', 'Games', 'Maracatu', 'Atômico', 'Eruption', 'Tempo', 'Perdido', 'You', 'Got', 'No', 'Right', 'Wasting', 'Love', 'Somebody', 'Stole', 'My', 'Guitar', "'Round", 'Midnight', 'Aquilo', 'Flash', 'Smooth', 'Childhoods', 'End?', 'Dream', 'Of', 'Mirrors', 'Royal', 'Orleans', 'The', 'Wicker', 'Man', "It's", 'Too', 'Funky', 'In', 'Here', 'Night', 'Flight', "Won't", 'Get', 'Fooled', 'Again', '(Full', 'Length', 'Version)', 'She', 'Loves', 'Me', 'Not', 'Beth', 'Exploder', 'Os', 'Cegos', 'Do', 'Castelo', 'The', 'Star', 'Spangled', 'Banner']
five_or_less = [word for word in word_list if len(word)<5]
print(five_or_less)

#lista que encuentre el num de espacios en una oración
sentence = "I never knew what hardship looked like until it started raining bowling balls."
spaces = [i for i in sentence if i == " "]
print(len(spaces))
#is there a way to use a counter inside a list comprehension?

#lista que a partir de otra lista de números aleatorios sea divisible por 2 o 3
random_numbers = [random.randint(1,100) for x in range(50)]
divisible_by_2or3 = [x for x in random_numbers if x%2==0 or x%3==0]
print(divisible_by_2or3)