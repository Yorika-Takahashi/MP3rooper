from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence

namelist = ["01 Introduction",
            "02 Poltergeist",
            "03 Battle with a Dangerous Opponent",
            "04 Phone",
            "05 Underground",
            "06 Battle with a Flippant Foe",
            "07 Hippie Battle",
            "08 You Won!",
            "09 Game Over",
            "10 Drugstore",
            "11 A Ghastly Site",
            "12 House",
            "13 Comforting Sleep",
            "14 Hotel Sleep",
            "15 Pollyanna (I Believe in You)",
            "16 Cave of the Tail",
            "17 Magicant",
            "18 Wisdom of the World (Queen Mary's Castle)",
            "19 Twinkle Elementary",
            "20 Level Up",
            "21 Factory",
            "22 Bein' Friends",
            "23 The Paradise Line",
            "24 Snowman",
            "25 Yucca Desert",
            "26 Airplane Ride",
            "27 Roving Tank",
            "28 Monkey Cave",
            "29 Youngtown",
            "30 Live House",
            "31 All That I Needed Was You",
            "32 Approaching Mt. Itoi",
            "33 Mt. Itoi",
            "34 Fallin' Love",
            "35 The Tombstone",
            "36 The Ocarina's Final Melody",
            "37 Eight Melodies",
            "38 Alien Investigation",
            "39 Versus Giegue",
            "40 The End"
            ]

#無音作る
pre_silence = AudioSegment.silent(duration=0.5*1000) #0.5秒
post_silence = AudioSegment.silent(duration=2*1000) #2秒

for name in namelist:
    souce_pass = "/Users/takahashikinei/Music/Music/Media.localized/Music/Hirokazu Tanaka, Keiichi Suzuki/MOTHER (FC) _ EarthBound Zero (NES)/" + name + ".mp3"

    #読み込み
    source = AudioSegment.from_mp3(souce_pass)

    #出力
    output_sound = pre_silence + source
    name = name + ".mp3"
    output_sound.export(name, format='mp3')