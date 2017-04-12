# -*- coding: UTF-8 -*-

import os
import sys

buildType = sys.argv[1]
buildPath = os.getcwd()

def clean():
    os.system('gradle clean')

def build(buildType):
    os.chdir(buildPath)
    os.system('gradle' + ' ' + buildType)

def uploadapk():
    os.chdir(buildPath + '/app/build/outputs/apk/')
    os.system("fir publish *.apk -T 379fd0c4df5ccc5b3bb0c1807b53b093")

def uploadmap():
    os.chdir(buildPath + '/app/build/outputs/mapping/release/')
    os.system('''curl --header "Content-Type: text/plain" --data-binary @mapping.txt 'http://bugly.qq.com/upload/map?pid=1&app=900015324&key=ccVjOGaszM6ag2hW&bid=com.beastbikes.android&ver=v2.6.0&n=mapping.txt' --verbose''')


def main():

    clean()

    build(buildType)

    uploadapk()

    if buildType == 'assembleRelease':
        uploadmap()


if __name__ == '__main__':
	main()
