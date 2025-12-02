import requests
import sys

cookie2024 ='53616c7465645f5f5e7f7cd76fc571f5b56232342d3e6a5bcb5f2e552d151481c05761eaf929089192162ef59f3bdda20769c4a0f1e94ffaa0956c37352c50c9'
cookie = '53616c7465645f5f19feb4eef9bea3ecca942bee5bf9cf49b4dfe4cc22fc1f24369b19092fcc73de2049a30bc8d5830d497ad3316cd96d08af757943f3177df2'

def main(dan,piskot=cookie):
    f = requests.get('https://adventofcode.com/2025/day/{day}/input'.format(day=str(dan)),cookies={'session':piskot})
    with open('inputs/day{day}.txt'.format(day = str(dan)), 'w') as file:
        file.write(f.text)
    with open('day{day}.py'.format(day=str(dan)),'x') as file:
        file.write("with open('inputs/day{day}.txt', 'r') as file:".format(day=str(dan)))
    
if __name__== "__main__":
    main(int(sys.argv[1]))

#uporabiš python get_input.py dan    v terminalu