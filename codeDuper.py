

result = ""
aninmals = [
    "Perry the Platypus",
    "Steve Irwin aka Crocodile Dun-Dee",
    "Weeping Angels",
    "Sarlac",
    "Pheonix",
    "Silence",
    "Nya Cat",
    "MiniMinotaur",
    "Unicorn",
    "Centaur",

]
descriptions = {
    "Pheonix" : "A mythical bird that lives for about 100 years.  Only one exists at a time, when it dies, it burns and from the ashes a baby is born.",
    "Centaur" : "A man torso in the place of a horses neck.  They are known for being fierce warriors.",
    "Steve Irwin aka Crocodile Dun-Dee" : "An absolute legend of a man who can take on any beast, big or small.  These are super rare, and unfortunatly the one that we knew about was killed in action, may he rest in peace.",
    "MiniMinotaur" : "A half man half bull creature, that is about 2 feet tall.  MiniMinotaurs cannot eat tartar sauce, it makes them explode.",
    "Perry the Platypus" : "He's a semi aquatic egg laying mammal of action.  He's a furry little flat foot who's never flinched from a fray.  He's got more than just mad skills, he's got a beaver tail and a bill.  And the women swoon whenever they hear him say (grdrdrdrdrdrd).  He's Perry the Platypus......................Oh special note from one Major Monogram, you can call him Agent P.",
    "Nya Cat" : "Yes, yes, I know, everyone wants this 8-bit rainbow farting space strawberry poptart cat to be a real thing, but it is not.",
    "Unicorn" : "We are told as children that unicorns are peaceful, sometimes even that they are protectors, using their horn to shoot rainbow lasers at fearsome foes.  This is simply not the case, unicorns are a beast straight from Hell, their goal is to impale humans with their sharp horn, so they can consume our soul as it exits our dying body.  If you ever see one, don't move, they have poor eyesight, you must stand still until they decide to charge, wait as long as possible then jump out of the way.  They will lose you for a time, and the only defence against one is safety in numbers.",
    "Silence" : "These freeaky lookin' creatures have a pretty nice fashion taste, boasting a black business suit, nice white shirt and black tie.  Though, their fashion is made up for by their looks, being about 7 feet tall, with 4 fingers on each hand, the second from the inside being excessivly large.  They also have some abilities, such as when you see one, you may only percieve it whilst looking, once you look away you cannot see them, and they can harness electrical energy around them and focus it on people, essentially dissentagrating the person.  During the moon landing, Niel Armstrong said \"That's one small step for (blip where he later said that he said a) man, one giant leap for mankind.\" During that blip, there was a broadcast of a Silent (a singular Silence Creature, it is both a religion and a species) saying \"you should kill us all on sight!\"  So any time you see one, you kill it, because you remember the previous encounters.",
    "Weeping Angels" : "These creatures are even more scary than the last, usually taking the form of a weeping angel statue, though they can inhabit any statue, even Lady Liberty herself.  The way they get you is when you can't see them, they turn into their true form, and can move insanely fast, crossing an entire gymnasium in the literal blink of an eye.  They feed on temporal potential energy, or the energy of your future, they send you back in time however many years you have left to live.  There is no way to defeat them either, just temporarily stop them from moving.  And, making things worse, that which bears the image of an angel.  This means that if you look one in the eyes, you become one, and if you take a picture or video, it becomes one.",
    "Sarlac" : "These are mega creatures with many tentacles, they can be found on the planet Tatoine, in pits.  The are great for throwing your enemies into, they position themselves so that their mouth covers the entrance to the hole.  They are a bit risky to be around though, their tentacles are long and strong enough to break ships apart."
}
imgs = list()
extensions = (
    ".jpg",
    ".jpeg",
    ".jpe",
    ".jif",
    ".jfif",
    ".jfi",
    ".png",
    ".gif",
)

def testForFile(fileName):
    for ext in extensions:
        try:
            open("images/" + fileName + ext).close()
            imgs.append("images/" + fileName + ext)
            return False
        except:
            "you didin't succeed"
    return True 

for i in aninmals:
    if testForFile(i):
        raise Exception(f"{i} is not a file")
for rank in range(len(aninmals)):
    result += f"<tr>\n    <td>{rank}</td>\n    <td>{aninmals[rank]}</td>\n    <td><img src = \"{imgs[rank]}\" height = 300 width = 400></td>\n    <td><p>{descriptions[aninmals[rank]]}</p></td>\n    </tr>\n"

print(result)

