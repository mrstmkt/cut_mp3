import glob
import pathlib
import os
from pydub import AudioSegment

#inフォルダ配下のmp3ファイルの一覧を取得
files = glob.glob("./in/*.mp3")

for file in files:
    sound = AudioSegment.from_file(pathlib.Path(file).resolve(), format="mp3")
    #mp3ファイルの前500ミリ秒を捨てる
    sound1 = sound[500:]

    fname = pathlib.Path(file).name
    outFileName = os.path.join("./out/", fname)
    #outフォルダーにmp3ファイルを書き出す
    sound1.export(outFileName, format="mp3", bitrate="128k")
    print(outFileName)
    