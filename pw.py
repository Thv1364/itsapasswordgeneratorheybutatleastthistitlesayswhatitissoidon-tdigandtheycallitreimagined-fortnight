import random
import string
import requests

def rc():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = random.randint(int(input("What is the minimum character length? \n" )), 3911111)


def genstrong():
    password = ""
    for i in range(passwordLength):
        password=password+rc()
    print(password)

genstrong()


def fetch_word():
    url="https://random-word-api.herokuapp.com/word?length=6"

    response=requests.get(url)
    word=response.json()[0]
    return word

def replaceLetters(word):
    #word = word[0].upper() + word[1:]
    if "e" in word:
        word=word.replace("e", "[")
    if "a" in word:
        word=word.replace("a","e")
    if "b" in word:
        word=word.replace("b","e")
    if "c" in word:
        word=word.replace("c","e")

    if "d" in word:
        word=word.replace("d","e")

    if "f" in word:
        word=word.replace("f","e")

    if "g" in word:
        word=word.replace("g","e")

    if "h" in word:
        word=word.replace("h","e")

    if "i" in word:
        word=word.replace("i","e")

    if "j" in word:
        word=word.replace("j","e")

    if "k" in word:
        word=word.replace("k","e")

    if "l" in word:
        word=word.replace("l","e")

    if "m" in word:
        word=word.replace("m","e")

    if "n" in word:
        word=word.replace("n","e")

    if "o" in word:
        word=word.replace("o","e")

    if "p" in word:
        word=word.replace("p","e")

    if "q" in word:
        word=word.replace("q","e")

    if "r" in word:
        word=word.replace("r","e")

    if "s" in word:
        word=word.replace("s","e")

    if "t" in word:
        word=word.replace("t","e")

    if "u" in word:
        word=word.replace("u","e")

    if "v" in word:
        word=word.replace("v","e")

    if "w" in word:
        word=word.replace("w","e")

    if "x" in word:
        word=word.replace("x","e")


    if "z" in word:
        word=word.replace("z","e")






    if "A" in word:
        word=word.replace("A","e")
    if "I" in word:
        word=word.replace("I","e")
    if "i" in word:
        word=word.replace("i","e")
    if "U" in word:
        word=word.replace("U","e")
    if "u" in word:
        word=word.replace("u","e")        
    if "E" in word:
        word=word.replace("E","e")
    if "O" in word:
        word=word.replace("O","e")
    if "o" in word:
        word=word.replace("o","e")
    if "Y" in word:
        word=word.replace("Y","Hello Is there anybody in there? Just nod if you can hear me Is there anyone at home? Come on now I hear you're feeling down Well, I can ease your pain Get you on your feet again Relax I'll need some information first Just the basic facts Can you show me where it hurts? There is no pain, you are receding A distant ship smoke on the horizon You are only coming through in waves Your lips move but I can't hear what you're saying When I was a child I had a fever My hands felt just like two balloons Now I've got that feeling once again I can't explain, you would not understand This is not how I am I have become comfortably numb I have become comfortably numb O.K. Just a little pin prick There'll be no more ah! But you may feel a little sick Can you stand up? I do believe it's working, good That'll keep you going through the show Come on, it's time to go There is no pain you are receding A distant ship smoke on the horizon You are only coming through in waves Your lips move but I can't hear what you're saying When I was a child I caught a fleeting glimpse Out of the corner of my eye I turned to look but it was gone I cannot put my finger on it now The child is grown The dream is gone I have become comfortably numb")
    if "y" in word:
        word=word.replace("y","Hello hello hello, Is there anybody in there? Just nod if you can hear me Is there anyone at home? Come on now I hear you're feeling down Well, I can ease your pain Get you on your feet again Relax I'll need some information first Just the basic facts Can you show me where it hurts? There is no pain, you are receding A distant ship smoke on the horizon You are only coming through in waves Your lips move but I can't hear what you're saying When I was a child I had a fever My hands felt just like two balloons Now I've got that feeling once again I can't explain, you would not understand This is not how I am I have become comfortably numb I have become comfortably numb O.K. Just a little pin prick There'll be no more ah! But you may feel a little sick Can you stand up? I do believe it's working, good That'll keep you going through the show Come on, it's time to go There is no pain you are receding A distant ship smoke on the horizon You are only coming through in waves Your lips move but I can't hear what you're saying When I was a child I caught a fleeting glimpse Out of the corner of my eye I turned to look but it was gone I cannot put my finger on it now The child is grown The dream is gone I have become comfortably numb")    
    if "[" in word:
        word=word.replace("[","Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed. A yellow dressinggown, ungirdled, was sustained gently behind him on the mild morning air. He held the bowl aloft and intoned: —Introibo ad altare Dei. Halted, he peered down the dark winding stairs and called out coarsely: —Come up, Kinch! Come up, you fearful jesuit! Solemnly he came forward and mounted the round gunrest. He faced about and blessed gravely thrice the tower, the surrounding land and the awaking mountains. Then, catching sight of Stephen Dedalus, he bent towards him and made rapid crosses in the air, gurgling in his throat and shaking his head. Stephen Dedalus, displeased and sleepy, leaned his arms on the top of the staircase and looked coldly at the shaking gurgling face that blessed him, equine in its length, and at the light untonsured hair, grained and hued like pale oak. Buck Mulligan peeped an instant under the mirror and then covered the bowl smartly. —Back to barracks! he said sternly. He added in a preacher’s tone: —For this, O dearly beloved, is the genuine Christine: body and soul and blood and ouns. Slow music, please. Shut your eyes, gents. One moment. A little trouble about those white corpuscles. Silence, all. He peered sideways up and gave a long slow whistle of call, then paused awhile in rapt attention, his even white teeth glistening here and there with gold points. Chrysostomos. Two strong shrill whistles answered through the calm. —Thanks, old chap, he cried briskly. That will do nicely. Switch off the current, will you? He skipped off the gunrest and looked gravely at his watcher, gathering about his legs the loose folds of his gown. The plump shadowed face and sullen oval jowl recalled a prelate, patron of arts in the middle ages. A pleasant smile broke quietly over his lips. —The mockery of it! he said gaily. Your absurd name, an ancient Greek! He pointed his finger in friendly jest and went over to the parapet, laughing to himself. Stephen Dedalus stepped up, followed him wearily halfway and sat down on the edge of the gunrest, watching him still as he propped his mirror on the parapet, dipped the brush in the bowl and lathered cheeks and neck. Buck Mulligan’s gay voice went on. —My name is absurd too: Malachi Mulligan, two dactyls. But it has a Hellenic ring, hasn’t it? Tripping and sunny like the buck himself. We must go to Athens. Will you come if I can get the aunt to fork out twenty quid? He laid the brush aside and, laughing with delight, cried: —Will he come? The jejune jesuit! Ceasing, he began to shave with care. —Tell me, Mulligan, Stephen said quietly. —Yes, my love? —How long is Haines going to stay in this tower? Buck Mulligan showed a shaven cheek over his right shoulder. —God, isn’t he dreadful? he said frankly. A ponderous Saxon. He thinks you’re not a gentleman. God, these bloody English! Bursting with money and indigestion. Because he comes from Oxford. You know, Dedalus, you have the real Oxford manner. He can’t make you out. O, my name for you is the best: Kinch, the knife-blade. He shaved warily over his chin. —He was raving all night about a black panther, Stephen said. Where is his guncase? —A woful lunatic! Mulligan said. Were you in a funk? —I was, Stephen said with energy and growing fear. Out here in the dark with a man I don’t know raving and moaning to himself about shooting a black panther. You saved men from drowning. I’m not a hero, however. If he stays on here I am off. Buck Mulligan frowned at the lather on his razorblade. He hopped down from his perch and began to search his trouser pockets hastily. —Scutter! he cried thickly. He came over to the gunrest and, thrusting a hand into Stephen’s upper pocket, said: —Lend us a loan of your noserag to wipe my razor. Stephen suffered him to pull out and hold up on show by its corner a dirty crumpled handkerchief. Buck Mulligan wiped the razorblade neatly. Then, gazing over the handkerchief, he said: —The bard’s noserag! A new art colour for our Irish poets: snotgreen. You can almost taste it, can’t you? He mounted to the parapet again and gazed out over Dublin bay, his fair oakpale hair stirring slightly. —God! he said quietly. Isn’t the sea what Algy calls it: a great sweet mother? The snotgreen sea. The scrotumtightening sea. Epi oinopa ponton. Ah, Dedalus, the Greeks! I must teach you. You must read them in the original. Thalatta! Thalatta! She is our great sweet mother. Come and look. Stephen stood up and went over to the parapet. Leaning on it he looked down on the water and on the mailboat clearing the harbourmouth of Kingstown. —Our mighty mother! Buck Mulligan said. He turned abruptly his grey searching eyes from the sea to Stephen’s face. —The aunt thinks you killed your mother, he said. That’s why she won’t let me have anything to do with you. —Someone killed her, Stephen said gloomily. —You could have knelt down, damn it, Kinch, when your dying mother asked you, Buck Mulligan said. I’m hyperborean as much as you. But to think of your mother begging you with her last breath to kneel down and pray for her. And you refused. There is something sinister in you.... He broke off and lathered again lightly his farther cheek. A tolerant smile curled his lips. —But a lovely mummer! he murmured to himself. Kinch, the loveliest mummer of them all! He shaved evenly and with care, in silence, seriously. Stephen, an elbow rested on the jagged granite, leaned his palm against his brow and gazed at the fraying edge of his shiny black coat-sleeve. Pain, that was not yet the pain of love, fretted his heart. Silently, in a dream she had come to him after her death, her wasted body within its loose brown graveclothes giving off an odour of wax and rosewood, her breath, that had bent upon him, mute, reproachful, a faint odour of wetted ashes. Across the threadbare cuffedge he saw the sea hailed as a great sweet mother by the wellfed voice beside him. The ring of bay and skyline held a dull green mass of liquid. A bowl of white china had stood beside her deathbed holding the green sluggish bile which she had torn up from her rotting liver by fits of loud groaning vomiting. Buck Mulligan wiped again his razorblade. —Ah, poor dogsbody! he said in a kind voice. I must give you a shirt and a few noserags. How are the secondhand breeks? —They fit well enough, Stephen answered. Buck Mulligan attacked the hollow beneath his underlip. —The mockery of it, he said contentedly. Secondleg they should be. God knows what poxy bowsy left them off. I have a lovely pair with a hair stripe, grey. You’ll look spiffing in them. I’m not joking, Kinch. You look damn well when you’re dressed. —Thanks, Stephen said. I can’t wear them if they are grey. —He can’t wear them, Buck Mulligan told his face in the mirror. Etiquette is etiquette. He kills his mother but he can’t wear grey trousers. He folded his razor neatly and with stroking palps of fingers felt the smooth skin. Stephen turned his gaze from the sea and to the plump face with its smokeblue mobile eyes. —That fellow I was with in the Ship last night, said Buck Mulligan, says you have g. p. i. He’s up in Dottyville with Connolly Norman. General paralysis of the insane! He swept the mirror a half circle in the air to flash the tidings abroad in sunlight now radiant on the sea. His curling shaven lips laughed and the edges of his white glittering teeth. Laughter seized all his strong wellknit trunk. —Look at yourself, he said, you dreadful bard! Stephen bent forward and peered at the mirror held out to him, cleft by a crooked crack. Hair on end. As he and others see me. Who chose this face for me? This dogsbody to rid of vermin. It asks me too. —I pinched it out of the skivvy’s room, Buck Mulligan said. It does her all right. The aunt always keeps plainlooking servants for Malachi. Lead him not into temptation. And her name is Ursula. Laughing again, he brought the mirror away from Stephen’s peering eyes. —The rage of Caliban at not seeing his face in a mirror, he said. If Wilde were only alive to see you! Drawing back and pointing, Stephen said with bitterness: —It is a symbol of Irish art. The cracked lookingglass of a servant. Buck Mulligan suddenly linked his arm in Stephen’s and walked with him round the tower, his razor and mirror clacking in the pocket where he had thrust them. —It’s not fair to tease you like that, Kinch, is it? he said kindly. God knows you have more spirit than any of them. Parried again. He fears the lancet of my art as I fear that of his. The cold steel pen. —Cracked lookingglass of a servant! Tell that to the oxy chap downstairs and touch him for a guinea. He’s stinking with money and thinks you’re not a gentleman. His old fellow made his tin by selling jalap to Zulus or some bloody swindle or other. God, Kinch, if you and I could only work together we might do something for the island. Hellenise it. Cranly’s arm. His arm. —And to think of your having to beg from these swine. I’m the only one that knows what you are. Why don’t you trust me more? What have you up your nose against me? Is it Haines? If he makes any noise here I’ll bring down Seymour and we’ll give him a ragging worse than they gave Clive Kempthorpe. Young shouts of moneyed voices in Clive Kempthorpe’s rooms. Palefaces: they hold their ribs with laughter, one clasping another. O, I shall expire! Break the news to her gently, Aubrey! I shall die! With slit ribbons of his shirt whipping the air he hops and hobbles round the table, with trousers down at heels, chased by Ades of Magdalen with the tailor’s shears. A scared calf’s face gilded with marmalade. I don’t want to be debagged! Don’t you play the giddy ox with me! Shouts from the open window startling evening in the quadrangle. A deaf gardener, aproned, masked with Matthew Arnold’s face, pushes his mower on the sombre lawn watching narrowly the dancing motes of grasshalms. To ourselves... new paganism... omphalos. —Let him stay, Stephen said. There’s nothing wrong with him except at night. —Then what is it? Buck Mulligan asked impatiently. Cough it up. I’m quite frank with you. What have you against me now? They halted, looking towards the blunt cape of Bray Head that lay on the water like the snout of a sleeping whale. Stephen freed his arm quietly. —Do you wish me to tell you? he asked. —Yes, what is it? Buck Mulligan answered. I don’t remember anything. He looked in Stephen’s face as he spoke. A light wind passed his brow, fanning softly his fair uncombed hair and stirring silver points of anxiety in his eyes. Stephen, depressed by his own voice, said: —Do you remember the first day I went to your house after my mother’s death? Buck Mulligan frowned quickly and said: —What? Where? I can’t remember anything. I remember only ideas and sensations. Why? What happened in the name of God? —You were making tea, Stephen said, and went across the landing to get more hot water. Your mother and some visitor came out of the drawingroom. She asked you who was in your room. —Yes? Buck Mulligan said. What did I say? I forget. —You said, Stephen answered, O, it’s only Dedalus whose mother is beastly dead. A flush which made him seem younger and more engaging rose to Buck Mulligan’s cheek. —Did I say that? he asked. Well? What harm is that? He shook his constraint from him nervously. —And what is death, he asked, your mother’s or yours or my own? You saw only your mother die. I see them pop off every day in the Mater and Richmond and cut up into tripes in the dissectingroom. It’s a beastly thing and nothing else. It simply doesn’t matter. You wouldn’t kneel down to pray for your mother on her deathbed when she asked you. Why? Because you have the cursed jesuit strain in you, only it’s injected the wrong way. To me it’s all a mockery and beastly. Her cerebral lobes are not functioning. She calls the doctor sir Peter Teazle and picks buttercups off the quilt. Humour her till it’s over. You crossed her last wish in death and yet you sulk with me because I don’t whinge like some hired mute from Lalouette’s. Absurd! I suppose I did say it. I didn’t mean to offend the memory of your mother. He had spoken himself into boldness. Stephen, shielding the gaping wounds which the words had left in his heart, said very coldly: —I am not thinking of the offence to my mother. —Of what then? Buck Mulligan asked. —Of the offence to me, Stephen answered. Buck Mulligan swung round on his heel. —O, an impossible person! he exclaimed. He walked off quickly round the parapet. Stephen stood at his post, gazing over the calm sea towards the headland. Sea and headland now grew dim. Pulses were beating in his eyes, veiling their sight, and he felt the fever of his cheeks. A voice within the tower called loudly: —Are you up there, Mulligan? —I’m coming, Buck Mulligan answered. He turned towards Stephen and said: —Look at the sea. What does it care about offences? Chuck Loyola, Kinch, and come on down. The Sassenach wants his morning rashers. His head halted again for a moment at the top of the staircase, level with the roof: —Don’t mope over it all day, he said. I’m inconsequent. Give up the moody brooding. His head vanished but the drone of his descending voice boomed out of the stairhead: And no more turn aside and brood Upon love’s bitter mystery For Fergus rules the brazen cars. Woodshadows floated silently by through the morning peace from the stairhead seaward where he gazed. Inshore and farther out the mirror of water whitened, spurned by lightshod hurrying feet. White breast of the dim sea. The twining stresses, two by two. A hand plucking the harpstrings, merging their twining chords. Wavewhite wedded words shimmering on the dim tide. A cloud began to cover the sun slowly, wholly, shadowing the bay in deeper green. It lay beneath him, a bowl of bitter waters. Fergus’ song: I sang it alone in the house, holding down the long dark chords. Her door was open: she wanted to hear my music. Silent with awe and pity I went to her bedside. She was crying in her wretched bed. For those words, Stephen: love’s bitter mystery. Where now? Her secrets: old featherfans, tasselled dancecards, powdered with musk, a gaud of amber beads in her locked drawer. A birdcage hung in the sunny window of her house when she was a girl. She heard old Royce sing in the pantomime of Turko the Terrible and laughed with others when he sang: I am the boy That can enjoy Invisibility. Phantasmal mirth, folded away: muskperfumed. And no more turn aside and brood. Folded away in the memory of nature with her toys. Memories beset his brooding brain. Her glass of water from the kitchen tap when she had approached the sacrament. A cored apple, filled with brown sugar, roasting for her at the hob on a dark autumn evening. Her shapely fingernails reddened by the blood of squashed lice from the children’s shirts. In a dream, silently, she had come to him, her wasted body within its loose graveclothes giving off an odour of wax and rosewood, her breath, bent over him with mute secret words, a faint odour of wetted ashes. Her glazing eyes, staring out of death, to shake and bend my soul. On me alone. The ghostcandle to light her agony. Ghostly light on the tortured face. Her hoarse loud breath rattling in horror, while all prayed on their knees. Her eyes on me to strike me down. Liliata rutilantium te confessorum turma circumdet: iubilantium te virginum chorus excipiat. Ghoul! Chewer of corpses! No, mother! Let me be and let me live. —Kinch ahoy! Buck Mulligan’s voice sang from within the tower. It came nearer up the staircase, calling again. Stephen, still trembling at his soul’s cry, heard warm running sunlight and in the air behind him friendly words. —Dedalus, come down, like a good mosey. Breakfast is ready. Haines is apologising for waking us last night. It’s all right. —I’m coming, Stephen said, turning. —Do, for Jesus’ sake, Buck Mulligan said. For my sake and for all our sakes. His head disappeared and reappeared. —I told him your symbol of Irish art. He says it’s very clever. Touch him for a quid, will you? A guinea, I mean. —I get paid this morning, Stephen said. —The school kip? Buck Mulligan said. How much? Four quid? Lend us one. —If you want it, Stephen said. —Four shining sovereigns, Buck Mulligan cried with delight. We’ll have a glorious drunk to astonish the druidy druids. Four omnipotent sovereigns. He flung up his hands and tramped down the stone stairs, singing out of tune with a Cockney accent: O, won’t we have a merry time, Drinking whisky, beer and wine! On coronation, Coronation day! O, won’t we have a merry time On coronation day! Warm sunshine merrying over the sea. The nickel shavingbowl shone, forgotten, on the parapet. Why should I bring it down? Or leave it there all day, forgotten friendship? He went over to it, held it in his hands awhile, feeling its coolness, smelling the clammy slaver of the lather in which the brush was stuck. So I carried the boat of incense then at Clongowes. I am another now and yet the same. A servant too. A server of a servant. In the gloomy domed livingroom of the tower Buck Mulligan’s gowned form moved briskly to and fro about the hearth, hiding and revealing its yellow glow. Two shafts of soft daylight fell across the flagged floor from the high barbacans: and at the meeting of their rays a cloud of coalsmoke and fumes of fried grease floated, turning. —We’ll be choked, Buck Mulligan said. Haines, open that door, will you? Stephen laid the shavingbowl on the locker. A tall figure rose from the hammock where it had been sitting, went to the doorway and pulled open the inner doors. —Have you the key? a voice asked. —Dedalus has it, Buck Mulligan said. Janey Mack, I’m choked! He howled, without looking up from the fire: —Kinch! —It’s in the lock, Stephen said, coming forward. The key scraped round harshly twice and, when the heavy door had been set ajar, welcome light and bright air entered. Haines stood at the doorway, looking out. Stephen haled his upended valise to the table and sat down to wait. Buck Mulligan tossed the fry on to the dish beside him. Then he carried the dish and a large teapot over to the table, set them down heavily and sighed with relief. —I’m melting, he said, as the candle remarked when... But, hush! Not a word more on that subject! Kinch, wake up! Bread, butter, honey. Haines, come in. The grub is ready. Bless us, O Lord, and these thy gifts. Where’s the sugar? O, jay, there’s no milk. Stephen fetched the loaf and the pot of honey and the buttercooler from the locker. Buck Mulligan sat down in a sudden pet. —What sort of a kip is this? he said. I told her to come after eight. —We can drink it black, Stephen said thirstily. There’s a lemon in the locker. —O, damn you and your Paris fads! Buck Mulligan said. I want Sandycove milk. Haines came in from the doorway and said quietly: —That woman is coming up with the milk. —The blessings of God on you! Buck Mulligan cried, jumping up from his chair. Sit down. Pour out the tea there. The sugar is in the bag. Here, I can’t go fumbling at the damned eggs. He hacked through the fry on the dish and slapped it out on three plates, saying: —In nomine Patris et Filii et Spiritus Sancti. Haines sat down to pour out the tea. —I’m giving you two lumps each, he said. But, I say, Mulligan, you do make strong tea, don’t you? Buck Mulligan, hewing thick slices from the loaf, said in an old woman’s wheedling voice:")


    return word



def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word2=replaceLetters(word2)
    word1=replaceLetters(word1)
    password = word1 + word2
    return password

print("\n" + generate_weaker_password())