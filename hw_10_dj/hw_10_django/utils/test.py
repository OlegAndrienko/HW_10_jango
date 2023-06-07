
import json

dict_h10 = [
    {
        "tag": ["change", "deep-thoughts", "thinking", "world"],
        "author": "Albert Einstein",
        "quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
    },
    {
        "tag": ["abilities", "choices"],
        "author": "J.K. Rowling",
        "quote": "It is our choices, Harry, that show what we truly are, far more than our abilities.",
    },
    {
        "tag": ["inspirational", "life", "live", "miracle", "miracles"],
        "author": "Albert Einstein",
        "quote": "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.",
    },
    {
        "tag": ["aliteracy", "books", "classic", "humor"],
        "author": "Jane Austen",
        "quote": "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
    },
    {
        "tag": ["be-yourself", "inspirational"],
        "author": "Marilyn Monroe",
        "quote": "Imperfection is beauty, madness is genius and its better to be absolutely ridiculous than absolutely boring.",
    },
    {
        "tag": ["adulthood", "success", "value"],
        "author": "Albert Einstein",
        "quote": "Try not to become a man of success. Rather become a man of value.",
    },
    {
        "tag": ["life", "love"],
        "author": "André Gide",
        "quote": "It is better to be hated for what you are than to be loved for what you are not.",
    },
    {
        "tag": ["edison", "failure", "inspirational", "paraphrased"],
        "author": "Thomas A. Edison",
        "quote": "I have not failed. Ive just found 10,000 ways that wont work.",
    },
    {
        "tag": ["misattributed-eleanor-roosevelt"],
        "author": "Eleanor Roosevelt",
        "quote": "A woman is like a tea bag; you never know how strong it is until its in hot water.",
    },
    {
        "tag": ["humor", "obvious", "simile"],
        "author": "Steve Martin",
        "quote": "A day without sunshine is like, you know, night.",
    },
    {
        "tag": ["friends", "heartbreak", "inspirational", "life", "love", "sisters"],
        "author": "Marilyn Monroe",
        "quote": "This life is what you make it. No matter what, youre going to mess up sometimes, its a universal truth. But the good part is you get to decide how youre going to mess it up. Girls will be your friends - theyll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - theyre your true best friends. Dont let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, theyll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you cant give up because if you give up, youll never find your soulmate. Youll never find that half who makes you whole and that goes for everything. Just because you fail once, doesnt mean youre gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you dont, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because lifes a beautiful thing and theres so much to smile about.",
    },
    {
        "tag": ["courage", "friends"],
        "author": "J.K. Rowling",
        "quote": "It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.",
    },
    {
        "tag": ["simplicity", "understand"],
        "author": "Albert Einstein",
        "quote": "If you cant explain it to a six year old, you dont understand it yourself.",
    },
    {
        "tag": ["love"],
        "author": "Bob Marley",
        "quote": "You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? Shes not perfect—you arent either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So dont hurt her, dont change her, dont analyze and dont expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when shes not there.",
    },
    {
        "tag": ["fantasy"],
        "author": "Dr. Seuss",
        "quote": "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.",
    },
    {
        "tag": ["life", "navigation"],
        "author": "Douglas Adams",
        "quote": "I may not have gone where I intended to go, but I think I have ended up where I needed to be.",
    },
    {
        "tag": [
            "activism",
            "apathy",
            "hate",
            "indifference",
            "inspirational",
            "love",
            "opposite",
            "philosophy",
        ],
        "author": "Elie Wiesel",
        "quote": "The opposite of love is not hate, its indifference. The opposite of art is not ugliness, its indifference. The opposite of faith is not heresy, its indifference. And the opposite of life is not death, its indifference.",
    },
    {
        "tag": [
            "friendship",
            "lack-of-friendship",
            "lack-of-love",
            "love",
            "marriage",
            "unhappy-marriage",
        ],
        "author": "Friedrich Nietzsche",
        "quote": "It is not a lack of love, but a lack of friendship that makes unhappy marriages.",
    },
    {
        "tag": ["books", "contentment", "friends", "friendship", "life"],
        "author": "Mark Twain",
        "quote": "Good friends, good books, and a sleepy conscience: this is the ideal life.",
    },
    {
        "tag": ["fate", "life", "misattributed-john-lennon", "planning", "plans"],
        "author": "Allen Saunders",
        "quote": "Life is what happens to us while we are making other plans.",
    },
    {
        "tag": ["love", "poetry"],
        "author": "Pablo Neruda",
        "quote": "I love you without knowing how, or when, or from where. I love you simply, without problems or pride: I love you in this way because I do not know any other way of loving but this, in which there is no I or you, so intimate that your hand upon my chest is my hand, so intimate that when I fall asleep your eyes close.",
    },
    {
        "tag": ["happiness"],
        "author": "Ralph Waldo Emerson",
        "quote": "For every minute you are angry you lose sixty seconds of happiness.",
    },
    {
        "tag": ["attributed-no-source"],
        "author": "Mother Teresa",
        "quote": "If you judge people, you have no time to love them.",
    },
    {
        "tag": ["humor", "religion"],
        "author": "Garrison Keillor",
        "quote": "Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.",
    },
    {
        "tag": ["humor"],
        "author": "Jim Henson",
        "quote": "Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.",
    },
    {
        "tag": ["comedy", "life", "yourself"],
        "author": "Dr. Seuss",
        "quote": "Today you are You, that is truer than true. There is no one alive who is Youer than You.",
    },
    {
        "tag": ["children", "fairy-tales"],
        "author": "Albert Einstein",
        "quote": "If you want your children to be intelligent, read them fairy tales. If you want them to be more intelligent, read them more fairy tales.",
    },
    {
        "tag": [],
        "author": "J.K. Rowling",
        "quote": "It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all - in which case, you fail by default.",
    },
    {
        "tag": ["imagination"],
        "author": "Albert Einstein",
        "quote": "Logic will get you from A to Z; imagination will get you everywhere.",
    },
    {
        "tag": ["music"],
        "author": "Bob Marley",
        "quote": "One good thing about music, when it hits you, you feel no pain.",
    },
    {
        "tag": ["learning", "reading", "seuss"],
        "author": "Dr. Seuss",
        "quote": "The more that you read, the more things you will know. The more that you learn, the more places youll go.",
    },
    {
        "tag": ["dumbledore"],
        "author": "J.K. Rowling",
        "quote": "Of course it is happening inside your head, Harry, but why on earth should that mean that it is not real?",
    },
    {
        "tag": ["friendship"],
        "author": "Bob Marley",
        "quote": "The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.",
    },
    {
        "tag": ["misattributed-to-mother-teresa", "paraphrased"],
        "author": "Mother Teresa",
        "quote": "Not all of us can do great things. But we can do small things with great love.",
    },
    {
        "tag": ["death", "inspirational"],
        "author": "J.K. Rowling",
        "quote": "To the well-organized mind, death is but the next great adventure.",
    },
    {
        "tag": ["chocolate", "food", "humor"],
        "author": "Charles M. Schulz",
        "quote": "All you need is love. But a little chocolate now and then doesnt hurt.",
    },
    {
        "tag": ["misattributed-to-c-s-lewis", "reading"],
        "author": "William Nicholson",
        "quote": "We read to know were not alone.",
    },
    {
        "tag": ["knowledge", "learning", "understanding", "wisdom"],
        "author": "Albert Einstein",
        "quote": "Any fool can know. The point is to understand.",
    },
    {
        "tag": ["books", "library"],
        "author": "Jorge Luis Borges",
        "quote": "I have always imagined that Paradise will be a kind of library.",
    },
    {
        "tag": ["inspirational"],
        "author": "George Eliot",
        "quote": "It is never too late to be what you might have been.",
    },
    {
        "tag": ["read", "readers", "reading", "reading-books"],
        "author": "George R.R. Martin",
        "quote": "A reader lives a thousand lives before he dies, said Jojen. The man who never reads lives only one.",
    },
    {
        "tag": ["books", "inspirational", "reading", "tea"],
        "author": "C.S. Lewis",
        "quote": "You can never get a cup of tea large enough or a book long enough to suit me.",
    },
    {
        "tag": [],
        "author": "Marilyn Monroe",
        "quote": "You believe lies so you eventually learn to trust no one but yourself.",
    },
    {
        "tag": ["girls", "love"],
        "author": "Marilyn Monroe",
        "quote": "If you can make a woman laugh, you can make her do anything.",
    },
    {
        "tag": ["life", "simile"],
        "author": "Albert Einstein",
        "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    },
    {
        "tag": ["love"],
        "author": "Marilyn Monroe",
        "quote": "The real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.",
    },
    {
        "tag": ["attributed-no-source"],
        "author": "Marilyn Monroe",
        "quote": "A wise girl kisses but doesnt love, listens but doesnt believe, and leaves before she is left.",
    },
    {
        "tag": ["hope", "inspirational"],
        "author": "Martin Luther King Jr.",
        "quote": "Only in the darkness can you see the stars.",
    },
    {
        "tag": ["dumbledore"],
        "author": "J.K. Rowling",
        "quote": "It matters not what someone is born, but what they grow to be.",
    },
    {
        "tag": ["love"],
        "author": "James Baldwin",
        "quote": "Love does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.",
    },
    {
        "tag": ["friendship", "love"],
        "author": "Jane Austen",
        "quote": "There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.",
    },
    {
        "tag": ["attributed", "fear", "inspiration"],
        "author": "Eleanor Roosevelt",
        "quote": "Do one thing every day that scares you.",
    },
    {
        "tag": ["attributed-no-source"],
        "author": "Marilyn Monroe",
        "quote": "I am good, but not an angel. I do sin, but I am not the devil. I am just a small girl in a big world trying to find someone to love.",
    },
    {
        "tag": ["music"],
        "author": "Albert Einstein",
        "quote": "If I were not a physicist, I would probably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.",
    },
    {
        "tag": ["books", "thought"],
        "author": "Haruki Murakami",
        "quote": "If you only read the books that everyone else is reading, you can only think what everyone else is thinking.",
    },
    {
        "tag": ["misattributed-to-einstein"],
        "author": "Alexandre Dumas fils",
        "quote": "The difference between genius and stupidity is: genius has its limits.",
    },
    {
        "tag": ["drug", "romance", "simile"],
        "author": "Stephenie Meyer",
        "quote": "Hes like a drug for you, Bella.",
    },
    {
        "tag": ["books", "friends", "novelist-quotes"],
        "author": "Ernest Hemingway",
        "quote": "There is no friend as loyal as a book.",
    },
    {
        "tag": ["inspirational"],
        "author": "Helen Keller",
        "quote": "When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.",
    },
    {
        "tag": ["inspirational", "life", "yourself"],
        "author": "George Bernard Shaw",
        "quote": "Life isnt about finding yourself. Life is about creating yourself.",
    },
    {
        "tag": ["alcohol"],
        "author": "Charles Bukowski",
        "quote": "Thats the problem with drinking, I thought, as I poured myself a drink. If something bad happens you drink in an attempt to forget; if something good happens you drink in order to celebrate; and if nothing happens you drink to make something happen.",
    },
    {
        "tag": ["the-hunger-games"],
        "author": "Suzanne Collins",
        "quote": "You don’t forget the face of the person who was your last hope.",
    },
    {
        "tag": ["humor"],
        "author": "Suzanne Collins",
        "quote": "Remember, were madly in love, so its all right to kiss me anytime you feel like it.",
    },
    {
        "tag": ["love"],
        "author": "C.S. Lewis",
        "quote": "To love at all is to be vulnerable. Love anything and your heart will be wrung and possibly broken. If you want to make sure of keeping it intact you must give it to no one, not even an animal. Wrap it carefully round with hobbies and little luxuries; avoid all entanglements. Lock it up safe in the casket or coffin of your selfishness. But in that casket, safe, dark, motionless, airless, it will change. It will not be broken; it will become unbreakable, impenetrable, irredeemable. To love is to be vulnerable.",
    },
    {
        "tag": ["bilbo", "journey", "lost", "quest", "travel", "wander"],
        "author": "J.R.R. Tolkien",
        "quote": "Not all those who wander are lost.",
    },
    {
        "tag": ["live-death-love"],
        "author": "J.K. Rowling",
        "quote": "Do not pity the dead, Harry. Pity the living, and, above all those who live without love.",
    },
    {
        "tag": ["good", "writing"],
        "author": "Ernest Hemingway",
        "quote": "There is nothing to writing. All you do is sit down at a typewriter and bleed.",
    },
    {
        "tag": ["life", "regrets"],
        "author": "Ralph Waldo Emerson",
        "quote": "Finish each day and be done with it. You have done what you could. Some blunders and absurdities no doubt crept in; forget them as soon as you can. Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense.",
    },
    {
        "tag": ["education"],
        "author": "Mark Twain",
        "quote": "I have never let my schooling interfere with my education.",
    },
    {
        "tag": ["troubles"],
        "author": "Dr. Seuss",
        "quote": "I have heard there are troubles of more than one kind. Some come from ahead and some come from behind. But Ive bought a big bat. Im all ready you see. Now my troubles are going to have troubles with me!",
    },
    {
        "tag": ["friendship", "love"],
        "author": "Alfred Tennyson",
        "quote": "If I had a flower for every time I thought of you...I could walk through my garden forever.",
    },
    {
        "tag": ["humor"],
        "author": "Charles Bukowski",
        "quote": "Some people never go crazy. What truly horrible lives they must lead.",
    },
    {
        "tag": ["humor", "open-mind", "thinking"],
        "author": "Terry Pratchett",
        "quote": "The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it.",
    },
    {
        "tag": ["humor", "philosophy"],
        "author": "Dr. Seuss",
        "quote": "Think left and think right and think low and think high. Oh, the thinks you can think up if only you try!",
    },
    {
        "tag": ["authors", "books", "literature", "reading", "writing"],
        "author": "J.D. Salinger",
        "quote": "What really knocks me out is a book that, when youre all done reading it, you wish the author that wrote it was a terrific friend of yours and you could call him up on the phone whenever you felt like it. That doesnt happen much, though.",
    },
    {
        "tag": ["humor", "insanity", "lies", "lying", "self-indulgence", "truth"],
        "author": "George Carlin",
        "quote": "The reason I talk to myself is because I’m the only one whose answers I accept.",
    },
    {
        "tag": [
            "beatles",
            "connection",
            "dreamers",
            "dreaming",
            "dreams",
            "hope",
            "inspirational",
            "peace",
        ],
        "author": "John Lennon",
        "quote": "You may say Im a dreamer, but Im not the only one. I hope someday youll join us. And the world will live as one.",
    },
    {
        "tag": ["humor", "sinister"],
        "author": "W.C. Fields",
        "quote": "I am free of all prejudice. I hate everyone equally. ",
    },
    {
        "tag": [],
        "author": "Ayn Rand",
        "quote": "The question isnt who is going to let me; its who is going to stop me.",
    },
    {
        "tag": ["books", "classic", "reading"],
        "author": "Mark Twain",
        "quote": "′Classic′ - a book which people praise and dont read.",
    },
    {
        "tag": ["mistakes"],
        "author": "Albert Einstein",
        "quote": "Anyone who has never made a mistake has never tried anything new.",
    },
    {
        "tag": ["humor", "love", "romantic", "women"],
        "author": "Jane Austen",
        "quote": "A ladys imagination is very rapid; it jumps from admiration to love, from love to matrimony in a moment.",
    },
    {
        "tag": ["integrity"],
        "author": "J.K. Rowling",
        "quote": "Remember, if the time should come when you have to make a choice between what is right and what is easy, remember what happened to a boy who was good, and kind, and brave, because he strayed across the path of Lord Voldemort. Remember Cedric Diggory.",
    },
    {
        "tag": ["books", "library", "reading"],
        "author": "Jane Austen",
        "quote": "I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! -- When I have a house of my own, I shall be miserable if I have not an excellent library.",
    },
    {
        "tag": ["elizabeth-bennet", "jane-austen"],
        "author": "Jane Austen",
        "quote": "There are few people whom I really love, and still fewer of whom I think well. The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency of all human characters, and of the little dependence that can be placed on the appearance of merit or sense.",
    },
    {
        "tag": ["age", "fairytales", "growing-up"],
        "author": "C.S. Lewis",
        "quote": "Some day you will be old enough to start reading fairy tales again.",
    },
    {
        "tag": ["god"],
        "author": "C.S. Lewis",
        "quote": "We are not necessarily doubting that God will do the best for us; we are wondering how painful the best will turn out to be.",
    },
    {
        "tag": ["death", "life"],
        "author": "Mark Twain",
        "quote": "The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.",
    },
    {
        "tag": ["misattributed-mark-twain", "truth"],
        "author": "Mark Twain",
        "quote": "A lie can travel half way around the world while the truth is putting on its shoes.",
    },
    {
        "tag": ["christianity", "faith", "religion", "sun"],
        "author": "C.S. Lewis",
        "quote": "I believe in Christianity as I believe that the sun has risen: not only because I see it, but because by it I see everything else.",
    },
    {
        "tag": ["truth"],
        "author": "J.K. Rowling",
        "quote": 'The truth." Dumbledore sighed. "It is a beautiful and terrible thing, and should therefore be treated with great caution.',
    },
    {
        "tag": ["death", "life"],
        "author": "Jimi Hendrix",
        "quote": "Im the one thats got to die when its time for me to die, so let me live my life the way I want to.",
    },
    {
        "tag": ["adventure", "love"],
        "author": "J.M. Barrie",
        "quote": "To die will be an awfully big adventure.",
    },
    {
        "tag": ["courage"],
        "author": "E.E. Cummings",
        "quote": "It takes courage to grow up and become who you really are.",
    },
    {
        "tag": ["life"],
        "author": "Khaled Hosseini",
        "quote": "But better to get hurt by the truth than comforted with a lie.",
    },
    {
        "tag": ["better-life-empathy"],
        "author": "Harper Lee",
        "quote": "You never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it.",
    },
    {
        "tag": [
            "books",
            "children",
            "difficult",
            "grown-ups",
            "write",
            "writers",
            "writing",
        ],
        "author": "Madeleine LEngle",
        "quote": "You have to write the book that wants to be written. And if the book will be too difficult for grown-ups, then you write it for children.",
    },
    {
        "tag": ["truth"],
        "author": "Mark Twain",
        "quote": "Never tell the truth to people who are not worthy of it.",
    },
    {
        "tag": ["inspirational"],
        "author": "Dr. Seuss",
        "quote": "A persons a person, no matter how small.",
    },
    {
        "tag": ["books", "mind"],
        "author": "George R.R. Martin",
        "quote": "... a mind needs books as a sword needs a whetstone, if it is to keep its edge.",
    },
]

json_quotes = json.dumps(dict_h10)
# print(json_quotes)



with open('C:/Users/Oleg/OneDrive/GOIT_cloud/hw_10_dj/hw_10_dj/hw_10_django/utils/qoutes.json', 'w') as fd:
    # for el in dict_h10:
    json.dump(dict_h10, fd)
    
    
# # for qoute in quotes:
# #     print(qoute)
# #     print(qoute['author'])
# #     print(qoute['qoute'])
# #     print(qoute['tags'])
# #     print('---------------------------------')
# with open('C:/Users/Oleg/OneDrive/GOIT_cloud/hw_10_dj/hw_10_dj/hw_10_django/utils/qoutes_1.json', 'r', encoding='utf-8') as fd:
#     # for el in dict_h10:
#     unpacked_data = json.loads(fd)
 
 
with open('C:/Users/Oleg/OneDrive/GOIT_cloud/hw_10_dj/hw_10_dj/hw_10_django/utils/qoutes.json', 'r') as fd:
    # for el in dict_h10:
    unpacked_data = json.load(fd)   
    
for el in unpacked_data:
    print(el)
    print(el['author'])
    print(el['quote'])
    print(el['tag'])
    print('---------------------------------')